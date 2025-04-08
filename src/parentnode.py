# src/parentnode.py
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        
        # Allow children to be None or an empty list
        if children is None:
            children = []
        
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        
        # Start with the opening tag
        html = f"<{self.tag}>"
        
        # Recursively add the children
        for child in self.children:
            html += child.to_html()
        
        # Close the tag
        html += f"</{self.tag}>"
        
        return html
