def extract_title(markdown):
    """
    Extracts the title (H1 header) from the markdown string.
    If there is no H1 header, it raises an exception.
    """
    lines = markdown.splitlines()
    
    # Look for a line that starts with '# ' (H1 header)
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()  # Remove the '#' and strip any whitespace
    
    # If no H1 header is found, raise an exception
    raise ValueError("No H1 header found in the markdown.")
