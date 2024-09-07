import unittest
from textnode import TextNode
from texttotextnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    #Basic Cases
    def init_test(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        self.assertEqual(result,expected)

    def test_single_image(self):
        text = "This is text with an ![image](https://example.com)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image","https://example.com")
        ]
        self.assertEqual(result,expected)


    def test_single_image_with_follow_text(self):
        text = "This is text with an ![image](https://example.com) and more text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is text with an ", "text"),
            TextNode("image", "image","https://example.com"),
            TextNode(" and more text", "text")
        ]
        self.assertEqual(result,expected)

    def text_image_and_bold(self):
        text = "Here is an image ![image](https://example.com/image.png) with **bold text**"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Here is an image ", "text"),
            TextNode("image", "image", "https://example.com/image.png"),
            TextNode(" with ", "text"),
            TextNode("bold text", "bold")
        ]
        self.assertEqual(result, expected)

    #Edge Cases
    def test_multiple_images_and_links(self):
        text = "Multiple images ![img1](https://example1.com) ![img2](https://example2.com) and links [link1](https://example1.com) [link2](https://example2.com)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Multiple images ", "text"),
            TextNode("img1", "image", "https://example1.com"),
            TextNode(" ", "text"),
            TextNode("img2", "image", "https://example2.com"),
            TextNode(" and links ", "text"),
            TextNode("link1", "link", "https://example1.com"),
            TextNode(" ", "text"),
            TextNode("link2", "link", "https://example2.com")
        ]
        self.assertEqual(result,expected)
    
if __name__ == "__main__":
    unittest.main()