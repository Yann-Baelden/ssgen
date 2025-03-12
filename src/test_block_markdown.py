import unittest
import enum
from markdown_blocks import (BlockType, markdown_to_blocks, block_to_block_type)


class TestMarkdownToHTML(unittest.TestCase):
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
            ],
        )

    def test_markdown_to_blocks_newlines(self):
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
            ],
        )

    def test_block_to_block_type_heading(self):
        bt = "## Second Title"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        bt = "```code section```"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        bt = ">quote line"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        bt = "- list item"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        bt = "1. first list item"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        bt = "Normal paragraph"
        block_type = block_to_block_type(bt)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
