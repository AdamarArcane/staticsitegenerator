import unittest
from extractlinks import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):

    # 1. Basic Test Cases
    def test_single_image(self):
        text = "This is an image ![alt text](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_single_link(self):
        text = "This is a link [click here](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("click here", "https://example.com")]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = "Here are two images: ![first](https://example.com/1.png) and ![second](https://example.com/2.png)"
        result = extract_markdown_images(text)
        expected = [
            ("first", "https://example.com/1.png"),
            ("second", "https://example.com/2.png")
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "Links to [site one](https://site1.com) and [site two](https://site2.com)"
        result = extract_markdown_links(text)
        expected = [
            ("site one", "https://site1.com"),
            ("site two", "https://site2.com")
        ]
        self.assertEqual(result, expected)

    # 2. Edge Cases
    def test_no_images(self):
        text = "No images here, just text."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_no_links(self):
        text = "No links here, just text."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_image(self):
        text = "This is malformed ![alt text(https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_link(self):
        text = "This is malformed [click here(https://example.com)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_empty_image(self):
        text = "This is an image with no URL ![alt text]()"
        result = extract_markdown_images(text)
        expected = [("alt text", "")]
        self.assertEqual(result, expected)

    def test_empty_link(self):
        text = "This is a link with no URL [click here]()"
        result = extract_markdown_links(text)
        expected = [("click here", "")]
        self.assertEqual(result, expected)

    # 3. Special Characters
    def test_special_characters_in_image(self):
        text = "This is an image ![alt text with special chars !@#](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("alt text with special chars !@#", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_special_characters_in_link(self):
        text = "This is a link [click here!@#](https://example.com?query=value&key=val#fragment)"
        result = extract_markdown_links(text)
        expected = [("click here!@#", "https://example.com?query=value&key=val#fragment")]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()