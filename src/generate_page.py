import os
from src.markdown_to_html_node import markdown_to_html_node
from src.extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    """
    Generates an HTML page from a markdown file using a template.
    Replaces {{ Title }} and {{ Content }} in the template.
    Also replaces href and src paths to handle the basepath, except for static files like index.css.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown content
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    content_html = markdown_to_html_node(markdown_content).to_html()

    # Extract the title from the markdown
    title = extract_title(markdown_content)
    
    # Read the template HTML
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Replace the placeholders in the template
    page_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content_html)
    
    # Only replace href="/index.css" with basepath for the CSS link
    page_content = page_content.replace('href="/index.css', 'href="index.css')

    # Replace src="/images/... with basepath for images
    page_content = page_content.replace('src="/images/', f'src="{basepath}images/')

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the generated HTML to the destination path
    with open(dest_path, 'w') as f:
        f.write(page_content)

    print(f"Page generated successfully at {dest_path}")
