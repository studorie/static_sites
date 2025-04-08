from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            # Extract images using the previously defined extraction function
            images = extract_markdown_images(node.text)
            
            # If no images, just append the current node as is
            if not images:
                new_nodes.append(node)
            else:
                # Split the node based on the images
                parts = node.text
                start_idx = 0
                
                for alt_text, url in images:
                    before_image = parts[:parts.find(f"![{alt_text}]({url})")]
                    after_image = parts[parts.find(f"![{alt_text}]({url})") + len(f"![{alt_text}]({url})"):]
                    
                    # Add text before the image
                    if before_image:
                        new_nodes.append(TextNode(before_image, TextType.TEXT))
                    
                    # Add image node
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    
                    # Update remaining part of the text after the image
                    parts = after_image
                
                # Add remaining part of the text after all images
                if parts:
                    new_nodes.append(TextNode(parts, TextType.TEXT))
    
    return new_nodes
