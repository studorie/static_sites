from src.blocktype import BlockType

def block_to_block_type(block: str) -> BlockType:
    # Strip leading and trailing whitespace from the block
    block = block.strip()

    # Check if the block is empty, treat it as a paragraph
    if not block:
        return BlockType.PARAGRAPH

    # Check for heading (1-6 # followed by space)
    if block.startswith('#'):
        return BlockType.HEADING

    # Check for code block (start and end with 3 backticks, allow for leading/trailing spaces)
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE

    # Check for quote (each line starts with '>')
    elif block.startswith('>'):
        return BlockType.QUOTE

    # Check for unordered list (starts with '- ')
    elif block.startswith('- '):
        return BlockType.UNORDERED_LIST

    # Check for ordered list (starts with '1. ', '2. ', etc.)
    elif block[0].isdigit() and block[1] == '.' and block[2] == ' ':
        return BlockType.ORDERED_LIST

    # If none of the above, it must be a paragraph
    else:
        return BlockType.PARAGRAPH
