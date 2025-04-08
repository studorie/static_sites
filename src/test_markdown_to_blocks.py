# src/test_markdown_to_blocks.py
import unittest
from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

    def test_empty_markdown(self):
        md = "\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_no_newlines(self):
        md = "This is just one block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is just one block"])

    def test_multiple_empty_blocks(self):
        md = "\n\n\n\nThis is a block\n\nAnother block\n\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a block", "Another block"])

if __name__ == "__main__":
    unittest.main()
