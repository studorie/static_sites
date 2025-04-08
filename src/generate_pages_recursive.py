import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Crawl the content directory and generate HTML pages for all markdown files.
    Preserve the directory structure when writing to the public directory.
    """
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):  # Only process markdown files
                # Construct the full path of the markdown file
                md_path = os.path.join(root, file)
                
                # Generate the destination path for the HTML file, preserving directory structure
                relative_path = os.path.relpath(md_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')
                
                # Ensure the destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Generate the page using the template
                generate_page(md_path, template_path, dest_path)
                print(f"Generated {dest_path} from {md_path}")
