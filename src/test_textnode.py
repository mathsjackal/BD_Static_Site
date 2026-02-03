import unittest

from textnode import *
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node3 = TextNode("This is a text node", TextType.TEXT)
        node4 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node3,node4)

    def test_url_none(self):
        node5 = TextNode("This is a new node", TextType.TEXT)
        self.assertTrue(node5.url == None)

    def test_url_real(self):
        node6 = TextNode("This is a text node", TextType.TEXT,"https:\\www.google.com")
        self.assertTrue(node6.url != None)
    
    def test_repr(self):
        node7 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node7)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_to_html_text(self):
        node1 = TextNode("Hello World", TextType.TEXT)
        node2 = text_node_to_html_node(node1)
        self.assertEqual(node2,LeafNode(None,"Hello World"))
    
    def test_text_node_to_html_bold(self):
        node1 = TextNode("Bold Text", TextType.BOLD)
        node2 = text_node_to_html_node(node1)
        self.assertEqual(node2,LeafNode("b","Bold Text"))

if __name__ == "__main__":
    unittest.main()