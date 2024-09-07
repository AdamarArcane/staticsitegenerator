import unittest
from textnode import TextNode
from splitnodesimages import *

link_text = "click here"
link_url = "https://example.com"

class TestSplitNodesLink(unittest.TestCase):
    #Basic Tests
    def test_single_link(self):
        node = TextNode(f"This is an image ![{link_text}]({link_url})", text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is an image ", text_type_text, None),
            TextNode(link_text, text_type_image, link_url)
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        node = TextNode(f"This is a link ![{link_text}]({link_url}) and this is another ![{link_text}]({link_url})",text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is a link ",text_type_text),
            TextNode(link_text, text_type_image, link_url),
            TextNode(" and this is another ", text_type_text),
            TextNode(link_text, text_type_image, link_url)
        ]
        self.assertEqual(result,expected)
    def test_multiple_nodes(self):
        node1 = TextNode(f"This is a link ![{link_text}]({link_url})", text_type_text)
        node2 = TextNode(f"This is a link ![{link_text}]({link_url})", text_type_text)
        result = split_nodes_image([node1, node2])
        expected = [
            TextNode("This is a link ", text_type_text, None),
            TextNode(link_text, text_type_image, link_url),
            TextNode("This is a link ", text_type_text, None),
            TextNode(link_text, text_type_image, link_url)
        ]
        self.assertEqual(result, expected)

    #Edge Cases
    def test_no_links(self):
        node = TextNode("There is no link in this test", text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode("There is no link in this test", text_type_text)
        ]
        self.assertEqual(result, expected)

    def test_malformed_link(self):
        node = TextNode(f"This is a link ![{link_text}({link_url})", text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode(f"This is a link ![{link_text}({link_url})", text_type_text)
        ]
        self.assertEqual(result,expected)


    def test_complex_link(self):
        node = TextNode(f"This is a link to this ![boot.dev lesson](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da)", text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is a link to this ", text_type_text),
            TextNode("boot.dev lesson", text_type_image, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da")
        ]
        self.assertEqual(result, expected)

    def test_complex_link_with_special_chars(self):
        node = TextNode(f"This is a link to this ![boot.dev@lesson](https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da)", text_type_text)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is a link to this ", text_type_text),
            TextNode("boot.dev@lesson", text_type_image, "https://www.boot.dev/lessons/bd4a35b7-e7a5-4ae3-96d7-051695ebd3da")
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()