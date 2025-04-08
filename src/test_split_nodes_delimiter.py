import unittest
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter

def test_split_nodes_delimiter(self):
    # Example with text and code
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a ")
    self.assertEqual(new_nodes[1].text, "code block")
    self.assertEqual(new_nodes[2].text, " word")

    # Example with bold text
    node = TextNode("This is a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[1].text, "bold")

    # Example with no delimiter found
    node = TextNode("No delimiter here", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0].text, "No delimiter here")

    # Example with unmatched delimiter (should raise an error)
    node = TextNode("This is an invalid delimiter case", TextType.TEXT)
    with self.assertRaises(ValueError):
        split_nodes_delimiter([node], "**", TextType.BOLD)
