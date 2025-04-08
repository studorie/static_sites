from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_links

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
