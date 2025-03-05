import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_func(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "blank"})
        self.assertTrue(node.props_to_html())

    def test_html(self):
        node = HTMLNode(tag="w", value="x", children=[], props={})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    

if __name__ == "__main__":
    unittest.main()

