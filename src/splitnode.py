from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_images
from src.extract_markdown import extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []  # This will hold our new TextNode objects

    for old_node in old_nodes:
        # If the node is not a TEXT type, add it to our result as is
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
        else:
            text = old_node.text
            parts = text.split(delimiter)  # Split the text based on the delimiter

            if len(parts) == 1:  # No delimiter found
                result.append(old_node)  # Keep the original node
            else:
                for i, part in enumerate(parts):
                    if i % 2 == 0:  # Even indices are regular text
                        result.append(TextNode(part, TextType.TEXT))
                    else:  # Odd indices are the part wrapped by the delimiter
                        result.append(TextNode(part, text_type))

    return result


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

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            # Extract links using the previously defined extraction function
            links = extract_markdown_links(node.text)
            
            # If no links, just append the current node as is
            if not links:
                new_nodes.append(node)
            else:
                # Split the node based on the links
                parts = node.text
                start_idx = 0
                
                for anchor_text, url in links:
                    before_link = parts[:parts.find(f"[{anchor_text}]({url})")]
                    after_link = parts[parts.find(f"[{anchor_text}]({url})") + len(f"[{anchor_text}]({url})"):]
                    
                    # Add text before the link
                    if before_link:
                        new_nodes.append(TextNode(before_link, TextType.TEXT))
                    
                    # Add link node
                    new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
                    
                    # Update remaining part of the text after the link
                    parts = after_link
                
                # Add remaining part of the text after all links
                if parts:
                    new_nodes.append(TextNode(parts, TextType.TEXT))
    
    return new_nodes