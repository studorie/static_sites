import os
import shutil
from src.generate_page import generate_page

def copy_static_files():
    # Clear the public directory first
    public_dir = 'public'
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
        print("Deleted existing 'public' directory.")

    # Copy static files from static to public
    shutil.copytree('static', 'public')
    print("Static files copied to 'public'.")

def main():
    # Step 1: Copy static files
    copy_static_files()

    # Step 2: Generate page
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
    main()
