import unittest
from extracttitle import extract_title

class TestExtractH1Title(unittest.TestCase):

    def test_single_h1_title(self):
        markdown_text = "# My Markdown Title"
        result = extract_title(markdown_text)
        expected = "My Markdown Title"
        self.assertEqual(result, expected)

    def test_h1_with_extra_spaces(self):
        markdown_text = "#    My Title With Extra Spaces   "
        result = extract_title(markdown_text)
        expected = "My Title With Extra Spaces"
        self.assertEqual(result, expected)

    def test_h1_among_other_markdown(self):
        markdown_text = """
        # My First Heading

        This is some text.

        ## This is a subheading

        Another paragraph.
        """
        result = extract_title(markdown_text)
        expected = "My First Heading"
        self.assertEqual(result, expected)

    def test_no_h1_title(self):
        markdown_text = "This is just some text without an h1 title."
        result = extract_title(markdown_text)
        expected = None
        self.assertEqual(result, expected)

    def test_empty_string(self):
        markdown_text = ""
        result = extract_title(markdown_text)
        expected = None
        self.assertEqual(result, expected)

    def test_h1_in_middle_of_text(self):
        markdown_text = """
        Some introductory text.
        
        # My Heading In The Middle

        More content below the heading.
        """
        result = extract_title(markdown_text)
        expected = "My Heading In The Middle"
        self.assertEqual(result, expected)

    def test_multiple_h1_titles(self):
        markdown_text = """
        # First Title

        Some content.

        # Second Title
        """
        result = extract_title(markdown_text)
        expected = "First Title"
        self.assertEqual(result, expected)

    def test_h1_with_special_characters(self):
        markdown_text = "# Title with !@#$%^&*() special characters"
        result = extract_title(markdown_text)
        expected = "Title with !@#$%^&*() special characters"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()