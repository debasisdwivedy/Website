import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"class": "btn", "id": "submit-btn"})
        expected = ' class="btn" id="submit-btn"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr_with_all_fields(self):
        children = [HTMLNode(tag="span", value="child")]
        node = HTMLNode(tag="div", value="Hello", children=children, props={"class": "greeting"})
        repr_str = repr(node)
        self.assertIn("TAG = (div)", repr_str)
        self.assertIn("VALUE = (Hello)", repr_str)
        self.assertIn("CHILDREN =", repr_str)
        self.assertIn("PROPERTIES =  class=\"greeting\"", repr_str)

    def test_repr_with_minimal_fields(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(\n)")

    def test_repr_with_some_fields(self):
        node = HTMLNode(tag="p", value="Paragraph")
        repr_str = repr(node)
        self.assertIn("TAG = (p)", repr_str)
        self.assertIn("VALUE = (Paragraph)", repr_str)
        self.assertNotIn("CHILDREN =", repr_str)
        self.assertNotIn("PROPERTIES =", repr_str)

    def test_nested_children_repr(self):
        child1 = HTMLNode(tag="li", value="Item 1")
        child2 = HTMLNode(tag="li", value="Item 2")
        parent = HTMLNode(tag="ul", children=[child1, child2])
        repr_str = repr(parent)
        self.assertIn("TAG = (ul)", repr_str)
        self.assertIn("CHILDREN =", repr_str)
        self.assertIn("TAG = (li)", repr_str)  # From children
        self.assertIn("VALUE = (Item 1)", repr_str)


if __name__ == "__main__":
    unittest.main()