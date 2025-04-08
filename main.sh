#!/bin/bash
# main.sh - Automate site generation and serve the page

# Run the Python script to generate the page
python3 src/main.py

# Serve the page using Python's HTTP server
cd public && python3 -m http.server 8888
