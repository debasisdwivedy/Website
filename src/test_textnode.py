import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is a not text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.BOLD,"https://boot.dev")
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)

    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node1), str(node2))

    def test_text(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        html_node1 = node1.text_node_to_html_node()
        self.assertEqual(html_node1.tag, None)
        self.assertEqual(html_node1.value, "This is a text node")

        node2 = TextNode("This is a bold node", TextType.BOLD)
        html_node2 = node2.text_node_to_html_node()
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a bold node")

        node3 = TextNode("This is a italic node", TextType.ITALIC)
        html_node3 = node3.text_node_to_html_node()
        self.assertEqual(html_node3.tag, "i")
        self.assertEqual(html_node3.value, "This is a italic node")

        node4 = TextNode("This is a code node", TextType.CODE)
        html_node4 = node4.text_node_to_html_node()
        self.assertEqual(html_node4.tag, "code")
        self.assertEqual(html_node4.value, "This is a code node")

        node5 = TextNode("This is a link node", TextType.LINK,"https://google.com")
        html_node5 = node5.text_node_to_html_node()
        self.assertEqual(html_node5.tag, "a")
        self.assertEqual(html_node5.value, "This is a link node")
        self.assertEqual(html_node5.props_to_html(), f" href=\"{html_node5.props["href"]}\"")

        node6 = TextNode("This is a image node", TextType.IMAGE,"https://google.com")
        html_node6 = node6.text_node_to_html_node()
        self.assertEqual(html_node6.tag, "img")
        self.assertEqual(html_node6.value, "This is a image node")
        self.assertEqual(html_node6.props_to_html(), f" src=\"{html_node6.props["src"]}\" alt=\"\"")