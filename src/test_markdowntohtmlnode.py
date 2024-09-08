import unittest
from markdowntohtmlnode import *
from htmlnode import HTMLNode


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraph(self):
        markdown = "This is a simple paragraph."
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [HTMLNode("p", None, text_to_children("This is a simple paragraph."))])
        self.assertEqual(result, expected)

    def test_heading(self):
        markdown = "# This is a heading"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [HTMLNode("h1", None, text_to_children("This is a heading"))])
        self.assertEqual(result, expected)

    def test_subheading(self):
        markdown = "### This is a subheading"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [HTMLNode("h3", None, text_to_children("This is a subheading"))])
        self.assertEqual(result, expected)

    def test_quote(self):
        markdown = "> This is a blockquote"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [HTMLNode("blockquote", None, text_to_children("This is a blockquote"))])
        self.assertEqual(result, expected)

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [
            HTMLNode("ul", None, [
                HTMLNode("li", None, text_to_children("Item 1")),
                HTMLNode("li", None, text_to_children("Item 2")),
                HTMLNode("li", None, text_to_children("Item 3"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [
            HTMLNode("ol", None, [
                HTMLNode("li", None, text_to_children("First item")),
                HTMLNode("li", None, text_to_children("Second item")),
                HTMLNode("li", None, text_to_children("Third item"))
            ])
        ])
        self.assertEqual(result, expected)

    def test_code_block(self):
        markdown = "```\ndef hello():\n    print('Hello, World!')\n```"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [
            HTMLNode("pre", None, [
                HTMLNode("code", "\ndef hello():\n    print('Hello, World!')\n", [], None)
            ])
        ])
        self.assertEqual(result, expected)

    def test_combined_blocks(self):
        markdown = "# Heading\n\nThis is a paragraph.\n\n* Item 1\n* Item 2\n\n> This is a quote"
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [
            HTMLNode("h1", None, text_to_children("Heading")),
            HTMLNode("p", None, text_to_children("This is a paragraph.")),
            HTMLNode("ul", None, [
                HTMLNode("li", None, text_to_children("Item 1")),
                HTMLNode("li", None, text_to_children("Item 2"))
            ]),
            HTMLNode("blockquote", None, text_to_children("This is a quote"))
        ])
        self.assertEqual(result, expected)

    def test_empty_markdown(self):
        markdown = ""
        result = markdown_to_html_node(markdown)
        expected = HTMLNode("div", None, [])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()