import unittest

from htmlnode import HTMLNode


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