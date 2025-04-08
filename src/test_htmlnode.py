# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is a paragraph.", children=[], props={})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph., children=[], props={})")

    def test_empty_node(self):
        node = HTMLNode(tag="div")
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=None, children=[], props={})")

if __name__ == "__main__":
    unittest.main()
