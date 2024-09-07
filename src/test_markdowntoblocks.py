import unittest
from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def init_test(self):
        text = "# This is a heading\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n* This is the first list item in a list block* This is a list item* This is another list item"
        result = markdown_to_blocks(text)
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block* This is a list item* This is another list item"]
        self.assertEqual(result, expected)
    def test_heading_and_paragraph(self):
        text = "# This is a heading\nThis is a paragraph of text."
        result = markdown_to_blocks(text)
        expected = ["# This is a heading", "This is a paragraph of text."]
        self.assertEqual(result, expected)

    def test_multiple_paragraphs(self):
        text = "This is the first paragraph.\n\nThis is the second paragraph."
        result = markdown_to_blocks(text)
        expected = ["This is the first paragraph.", "This is the second paragraph."]
        self.assertEqual(result, expected)

    def test_paragraph_with_bold_and_italic(self):
        text = "This is a paragraph with **bold** and *italic* text."
        result = markdown_to_blocks(text)
        expected = ["This is a paragraph with **bold** and *italic* text."]
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        text = "* Item 1\n* Item 2\n* Item 3"
        result = markdown_to_blocks(text)
        expected = ["* Item 1\n* Item 2\n* Item 3"]
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        text = "1. First item\n2. Second item\n3. Third item"
        result = markdown_to_blocks(text)
        expected = ["1. First item\n2. Second item\n3. Third item"]
        self.assertEqual(result, expected)

    def test_code_block(self):
        text = "```Code block```"
        result = markdown_to_blocks(text)
        expected = ["```Code block```"]
        self.assertEqual(result, expected)

    def test_mixed_blocks(self):
        text = "# Heading\n\nThis is a paragraph.\n\n* List item 1\n* List item 2\n\n1. Ordered item 1\n2. Ordered item 2\n\n```Code block```"
        result = markdown_to_blocks(text)
        expected = [
            "# Heading",
            "This is a paragraph.",
            "* List item 1\n* List item 2",
            "1. Ordered item 1\n2. Ordered item 2",
            "```Code block```"
        ]
        self.assertEqual(result, expected)

    def test_empty_input(self):
        text = ""
        result = markdown_to_blocks(text)
        expected = []
        self.assertEqual(result, expected)

    def test_heading_with_no_content(self):
        text = "# "
        result = markdown_to_blocks(text)
        expected = ["# "]
        self.assertEqual(result, expected)

    def test_paragraph_with_images_and_links(self):
        text = "Here is an image ![alt text](https://example.com/image.png) and a link [example](https://example.com)."
        result = markdown_to_blocks(text)
        expected = ["Here is an image ![alt text](https://example.com/image.png) and a link [example](https://example.com)."]
        self.assertEqual(result, expected)

    def test_malformed_markdown(self):
        text = "This is **bold text with a missing closing delimiter."
        result = markdown_to_blocks(text)
        expected = ["This is **bold text with a missing closing delimiter."]
        self.assertEqual(result, expected)
        
    def test_mixed_content_with_heading(self):
        text = "# Heading\n\n1. First item\n2. Second item\n\n```\nCode block\n```\n\nParagraph"
        result = markdown_to_blocks(text)
        expected = [
        "# Heading",
        "1. First item\n2. Second item",
        "```\nCode block\n```",
        "Paragraph"
    ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()