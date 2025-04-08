import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def copy_static_files():
    # Clear the 'dir' directory first
    dir_path = 'dir'  # Using 'dir' as per your request
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print("Deleted existing 'dir' directory.")

    # Copy static files from static to 'dir'
    shutil.copytree('static', dir_path)  # Copy from 'static' to 'dir'
    print("Static files copied to 'dir'.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """
    Crawl the content directory and generate HTML pages for all markdown files.
    Preserve the directory structure when writing to the 'dir' directory.
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
                generate_page(md_path, template_path, dest_path, basepath)
                print(f"Generated {dest_path} from {md_path}")

def main():
    # Get basepath from command-line arguments or default to '/'
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'  
    print(f"Using basepath: {basepath}")

    # Step 1: Copy static files to 'dir'
    copy_static_files()

    # Step 2: Generate pages recursively for all markdown files in content directory
    generate_pages_recursive('content', 'template.html', 'dir', basepath)  # Using 'dir' as the output folder

if __name__ == "__main__":
    main()