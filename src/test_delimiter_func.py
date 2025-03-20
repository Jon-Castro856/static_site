import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):
    def test_functionality(self):
        node = TextNode("This is text with a `code block` word", TextType.CODE)
        self.assertTrue(split_nodes_delimiter([node], "`", TextType.CODE))
    
    def test_err(self):
        node = TextNode("This is text with a 'code block' word", TextType.CODE)
        with self.assertRaises( ValueError):
            err_node = split_nodes_delimiter([node], ",", TextType.CODE)

if __name__ == "__main__":
    unittest.main()