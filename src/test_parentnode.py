# src/test_parentnode.py
import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        # Test with a simple ParentNode containing a LeafNode child
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        # Test with nested ParentNode and LeafNode
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_no_children(self):
        # Test for ParentNode with empty children list
        parent_node = ParentNode("ul", [])
        self.assertEqual(parent_node.to_html(), "<ul></ul>")

    def test_to_html_no_tag(self):
        # Test for ParentNode without a tag should raise an error
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "No tag")])

if __name__ == "__main__":
    unittest.main()
