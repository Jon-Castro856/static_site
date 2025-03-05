import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_uneq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_uneq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, url="https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
                "TextNode(This is a text node, link, https://www.boot.dev)", repr(node)
        )
if __name__ == "__main__":
    unittest.main()
