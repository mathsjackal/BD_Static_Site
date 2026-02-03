# Tests for the split blocks function
import unittest
from split_blocks import *

class Test_MarkdownBlock_Split(unittest.TestCase):
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

class Test_Split_Blocks(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph of text."
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

    def test_heading_level_1(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)
    
    def test_heading_level_6(self):
        block = "###### Heading Level 6"
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)
    
    def test_code_block_not_heading(self):
        block = "```\n# not a heading \n```"
        self.assertEqual(block_to_block_type(block),BlockType.CODE)
    
    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)