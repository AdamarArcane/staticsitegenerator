import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p","Hello World",[1],{"href": "https://www.google.com", "target": "_blank"})
        expectedValue = "HTMLNode(p, Hello World, [1], {\'href\': \'https://www.google.com\', \'target\': \'_blank\'})"
        self.assertEqual(node.__repr__(), expectedValue)

    def test_props_to_html(self):
        node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})   
        expectedValue = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.add_props_to_html(), expectedValue)

    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode("p",None,None,None)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expectedValue = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expectedValue)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expectedValue = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), expectedValue)

    if __name__ == "__main__":
        unittest.main()