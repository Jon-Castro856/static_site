import unittest

from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_func(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "blank"})
        self.assertTrue(node.props_to_html())

    def test_html(self):
        node = HTMLNode(tag="w", value="x", children=[], props={})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_eq(self):
        node1 = HTMLNode(tag="h1", value="text", children=[], props={"Target:" "blank"})
        node2 = HTMLNode(tag="h1", value="text", children=[], props={"Target:" "blank"})
        self.assertEqual(node1, node2)

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node2 = TextNode("this is a link node", TextType.LINK, "https://www.google.com")
        link_node = text_node_to_html_node(node2)
        self.assertEqual(link_node.tag, "a")
        self.assertEqual(link_node.to_html(), '<a href="https://www.google.com">this is a link node</a>')

        node3 = TextNode("this is an image", TextType.IMAGE, "picture.jpg")
        image_node = text_node_to_html_node(node3)
        self.assertEqual(image_node.tag, "img")
        self.assertEqual(image_node.to_html(), '<img src="picture.jpg" alt="this is an image"></img>')
    

if __name__ == "__main__":
    unittest.main()

