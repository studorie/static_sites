# src/test_leafnode.py
import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")
    
    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()
