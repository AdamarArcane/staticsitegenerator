import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_diff(self):
        node = TextNode('This is a text node', "bold", "HelloWorld")
        node2 = TextNode('This is a text node', "bold", "HelloWorld2")
        self.assertNotEqual(node, node2)

class TextNodeToHTMLNodeTestCase(unittest.TestCase):
    def test_text_conversion(self):
        text_node = TextNode('Hello World', "text")
        expected_html_node = LeafNode(None, 'Hello World')
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)
    def test_bold_conversion(self):
        text_node = TextNode("Bold Text", "bold")
        expected_html_node = LeafNode("b", "Bold Text")
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)
    def test_italic_conversion(self):
        text_node = TextNode("Italic Text", "italic")
        expected_html_node = LeafNode("i", "Italic Text")
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)
    def test_code_conversion(self):
        text_node = TextNode("Code Text", "code")
        expected_html_node = LeafNode("code", "Code Text")
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_link_conversion(self):
        text_node = TextNode("Link Text", "link", url="http://example.com")
        expected_html_node = LeafNode("a", "Link Text", props={"href": "http://example.com"})
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

    def test_image_conversion(self):
        text_node = TextNode("", "image", url="http://example.com/image.png")
        expected_html_node = LeafNode("img", "", props={"src": "http://example.com/image.png", "alt": "alttext"})
        self.assertEqual(text_node_to_html_node(text_node), expected_html_node)

if __name__ == "__main__":
    unittest.main()