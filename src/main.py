# src/main.py
from textnode import TextNode, TextType

def main():
    # Create a TextNode instance with some dummy values
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)  # This will use the __repr__ method to print the TextNode object

if __name__ == "__main__":
    main()
