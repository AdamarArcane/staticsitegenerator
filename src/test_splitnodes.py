import unittest
from textnode import TextNode
from splitnodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def setUp(self):
        self.text_type_text = "text"
        self.text_type_bold = "bold"
        self.text_type_italic = "italic"
        self.text_type_code = "code"

    # 1. Basic Test Cases
    def test_single_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = [
            TextNode("This is text with a ", self.text_type_text),
            TextNode("code block", self.text_type_code),
            TextNode(" word", self.text_type_text),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("This is plain text", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = [node]  # No change expected
        self.assertEqual(result, expected)

    def test_delimiter_at_start(self):
        node = TextNode("`code block` at the start", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = [
            TextNode("code block", self.text_type_code),
            TextNode(" at the start", self.text_type_text),
        ]
        self.assertEqual(result, expected)

    def test_delimiter_at_end(self):
        node = TextNode("At the end `code block`", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = [
            TextNode("At the end ", self.text_type_text),
            TextNode("code block", self.text_type_code),
        ]
        self.assertEqual(result, expected)

    # 3. Invalid Test Cases
    def test_unbalanced_delimiter_raises_exception(self):
        node = TextNode("This is unbalanced `code block", self.text_type_text)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", self.text_type_code)
        self.assertEqual(str(context.exception), "This is not valid markdown")

    # 4. Edge Test Cases
    def test_empty_string(self):
        node = TextNode("", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = []
        self.assertEqual(result, expected)

    def test_delimiter_without_text(self):
        node = TextNode("Empty `` delimiters", self.text_type_text)
        result = split_nodes_delimiter([node], "`", self.text_type_code)
        expected = [
            TextNode("Empty ", self.text_type_text),
            TextNode("", self.text_type_code),
            TextNode(" delimiters", self.text_type_text),
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()