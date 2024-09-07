import unittest
from blocktoblocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), "heading")
        self.assertEqual(block_to_block_type("## This is a sub-heading"), "heading")
        self.assertEqual(block_to_block_type("###### This is a small heading"), "heading")

    def test_code_block(self):
        code_block = "```\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

    def test_quote_block(self):
        quote_block = "> This is a quote\n> It spans multiple lines"
        self.assertEqual(block_to_block_type(quote_block), "quote")

    def test_mixed_quote_and_paragraph(self):
        mixed_quote = "> This starts as a quote\nbut this line is not a quote"
        self.assertEqual(block_to_block_type(mixed_quote), "paragraph")

    def test_unordered_list(self):
        ulist_block = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_to_block_type(ulist_block), "unordered_list")

        ulist_block_with_dash = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(ulist_block_with_dash), "unordered_list")

    def test_mixed_unordered_list_and_paragraph(self):
        mixed_ulist = "* Item 1\nNot a list item"
        self.assertEqual(block_to_block_type(mixed_ulist), "paragraph")

    def test_ordered_list(self):
        olist_block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(olist_block), "ordered_list")

    def test_mixed_ordered_list_and_paragraph(self):
        mixed_olist = "1. First item\nNot a list item"
        self.assertEqual(block_to_block_type(mixed_olist), "paragraph")

    def test_paragraph(self):
        paragraph = "This is a regular paragraph of text."
        self.assertEqual(block_to_block_type(paragraph), "paragraph")

    def test_code_block_with_fence(self):
        code_block = "```\nprint('Code block inside fence')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

    def test_invalid_unordered_list(self):
        invalid_ulist = "* Item 1\nNo star here"
        self.assertEqual(block_to_block_type(invalid_ulist), "paragraph")

    def test_invalid_ordered_list(self):
        invalid_olist = "1. Item 1\nNot a numbered item"
        self.assertEqual(block_to_block_type(invalid_olist), "paragraph")

if __name__ == '__main__':
    unittest.main()