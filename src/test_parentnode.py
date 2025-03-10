import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_basic_functionality(self):
        child_node = LeafNode("b", "Bold text", props={"dict": "tionary"})
        node = ParentNode("p", None, [child_node])
        self.assertTrue(node.to_html()) 


if __name__ == "__main__":
    unittest.main()