import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        # Test equality of two TextNode objects with the same properties
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_equal_text(self):
        # Test that two TextNode objects with different text are not equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_equal_text_type(self):
        # Test that two TextNode objects with different text_type are not equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        # Test that two TextNode objects with different URLs are not equal
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        # Test that the url is None by default if not provided
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_repr(self):
        # Test that the __repr__ method returns the correct string representation
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is some anchor text, link, https://www.boot.dev)")

if __name__ == "__main__":
    unittest.main()
