# src/leafnode.py
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if not self.tag:  # If there's no tag, return the value as raw text
            return self.value
        # Return the HTML representation of this leaf node
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

