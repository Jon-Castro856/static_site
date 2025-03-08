import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("a","Hello, world!", props={"href": "https://www.google.com"})
        node2 = LeafNode(None, "Hello, World!")
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Hello, world!</a>')
        self.assertEqual(node2.to_html(), "Hello, World!")

    def test_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
