# src/markdown_to_blocks.py

def markdown_to_blocks(markdown):
    # Split the raw markdown string by double newlines, which separates blocks
    blocks = markdown.split('\n\n')
    
    # Strip whitespace from each block and filter out any empty blocks
    blocks = [block.strip() for block in blocks if block.strip()]
    
    return blocks
