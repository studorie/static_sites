# src/textnode_to_html.py
from leafnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)  # No tag, just raw text
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)  # Bold text in <b> tag
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)  # Italic text in <i> tag
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)  # Code text in <code> tag
    
    elif text_node.text_type == TextType.LINK:
        # Link text with anchor tag and href prop
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        # Image with <img> tag, src and alt props
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    else:
        raise ValueError(f"Unrecognized TextType: {text_node.text_type}")
