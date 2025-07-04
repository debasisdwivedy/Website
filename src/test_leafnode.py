import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')