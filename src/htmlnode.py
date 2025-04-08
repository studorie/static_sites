class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        """Convert props to HTML attributes string."""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def to_html(self):
        """This should be implemented in subclasses if needed"""
        if self.children:
            # If the node has children, render the tag and its children
            children_html = "".join([child.to_html() if isinstance(child, HTMLNode) else child for child in self.children])
            # Remove extra newlines between children for paragraphs
            if self.tag == "p":
                children_html = children_html.replace("\n", " ")  # Replace newlines with space
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        elif self.value:
            # If it's a leaf node or a node with a value
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return ""
    
    def __repr__(self):
        """Return a string representation of the node."""
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
