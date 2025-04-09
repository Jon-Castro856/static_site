import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_basic_functionality(self):
        child_node = LeafNode("b", "Bold text", props={"dict": "tionary"})
        node = ParentNode("p", [child_node])
        self.assertTrue(node.to_html())

    def test_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_multiple_children(self):
        child1 = LeafNode("b", "text")
        child2 = LeafNode("i", "more text")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(parent.to_html(), "<p><b>text</b><i>more text</i></p>")


if __name__ == "__main__":
    unittest.main()