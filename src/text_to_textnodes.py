from src.splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType

def text_to_textnodes(text):
    # Step 1: Create a single TextNode for the input text
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Step 2: Split the nodes based on different delimiters
    # First handle code (backticks), bold (**), and italic (_)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Handle image and link Markdown syntax
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
