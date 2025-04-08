#!/bin/bash
# build.sh - Build the site for GitHub Pages deployment

# Set the basepath to your GitHub repository URL
BASEPATH="https://github.com/studorie/static_sites/"

# Run the Python script to generate the site
python3 src/main.py "$BASEPATH"

# Optionally, you can include the git commands to commit and push the changes to GitHub
git add .
git commit -m "Deploy site to GitHub Pages"
git push origin main
