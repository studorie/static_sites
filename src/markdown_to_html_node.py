from src.block_to_block_type import BlockType, block_to_block_type
from src.markdown_to_blocks import markdown_to_blocks
from src.htmlnode import HTMLNode
from src.textnode import TextNode, TextType
from src.splitnode import split_nodes_image, split_nodes_link, split_nodes_delimiter
from src.text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    parent_node = HTMLNode("div", None, [])

    for block in blocks:
        block_type = block_to_block_type(block.strip())  # Determine block type

        if block_type == BlockType.PARAGRAPH:
            # For paragraphs, convert inline markdown into child nodes
            nodes = text_to_textnodes(block)
            paragraph_node = HTMLNode("p", None, [child.to_html() if isinstance(child, TextNode) else child for child in nodes])
            parent_node.children.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            heading_level = block.count('#')
            heading_node = HTMLNode(f"h{heading_level}", block[heading_level+1:].strip(), [])
            parent_node.children.append(heading_node)

        elif block_type == BlockType.CODE:
            # For code blocks, create a <pre><code> node and keep the content inside without inline parsing
            code_content = block.strip("`").strip()  # Strip backticks
            code_node = HTMLNode("pre", None, [HTMLNode("code", code_content + "\n", [])])  # Add newline before closing </code>
            parent_node.children.append(code_node)

        elif block_type == BlockType.QUOTE:
            # Strip the '>' for blockquotes
            quote_content = block[1:].strip()  # Remove the leading ">"
            quote_node = HTMLNode("blockquote", quote_content, [])
            parent_node.children.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = HTMLNode("ul", None, [])
            items = block.split("\n")
            for item in items:
                # Remove the leading `-` from markdown list items
                item_content = item.lstrip('-').strip()
                # Check for links inside list items and create <a> tags
                item_nodes = text_to_textnodes(item_content)
                li_node = HTMLNode("li", None, [child.to_html() if isinstance(child, TextNode) else child for child in item_nodes])
                ul_node.children.append(li_node)
            parent_node.children.append(ul_node)

        elif block_type == BlockType.ORDERED_LIST:
            ol_node = HTMLNode("ol", None, [])
            items = block.split("\n")
            for item in items:
                # Remove the leading number and period from ordered list items
                item_content = item.split('. ', 1)[-1].strip()
                # Check for links inside list items and create <a> tags
                item_nodes = text_to_textnodes(item_content)
                li_node = HTMLNode("li", None, [child.to_html() if isinstance(child, TextNode) else child for child in item_nodes])
                ol_node.children.append(li_node)
            parent_node.children.append(ol_node)

        else:
            raise ValueError(f"Unknown block type: {block_type}")

    return parent_node
