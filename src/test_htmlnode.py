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

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        
        expectedValue = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expectedValue)
    def no_content_no_childeren(self):
        node = ParentNode('p')
        assert node.to_html() == '<p></p>'
    def element_with_text_content(self):
        node = ParentNode('p', 'Hello, World!')
        assert node.to_html() == '<p>Hello, World!</p>'
    def element_with_props(self):
        node = ParentNode('img', attributes={'src': 'image.png', 'alt': 'An image'})
        assert node.to_html() == '<img src="image.png" alt="An image"></img>'
    def nested_elements(self):
        div = ParentNode('div')
        p = ParentNode('p', 'Nested paragraph.')
        div.add_child(p)
        self.assertEqual(div.to_html(),'<div><p>Nested paragraph.</p></div>') 
    def element_with_multiple_props(self):
        node = ParentNode('input', attributes={'type': 'text', 'value': 'Sample', 'placeholder': 'Enter text'})
        assert node.to_html() == '<input type="text" value="Sample" placeholder="Enter text"></input>'
    if __name__ == "__main__":
        unittest.main()