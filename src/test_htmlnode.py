# Unit Tests for the HTML Node Class
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *
from main import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("h1","Sample text within a paragraph.", None ,{"href": "https://www.google.com"})
        node2 = HTMLNode("h1","Sample text within a paragraph.",None ,{"href": "https://www.google.com"})
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1 = HTMLNode("h1","Sample text within a paragraph.",None ,{"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode(None ,"Sample text within a paragraph.",None ,{"href": "https://www.google.com","target": "_blank"})
        self.assertNotEqual(node1, node2)

    def test_prop_convert(self):
        correct =  " href=https://www.google.com target=_blank"
        node1 = HTMLNode("h1","Sample text within a paragraph.",None ,{"href": "https://www.google.com","target": "_blank"})
        test_convert = node1.props_to_html()
        self.assertEqual(correct,test_convert)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Test String")
        self.assertEqual(node.to_html(),"<b>Test String</b>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),"<a href=https://www.google.com>Click here!</a>")

    def test_leaf_plain_text(self):
        node = LeafNode(None,"Hello World")
        self.assertEqual(node.to_html(),"Hello World")
    
    def test_leaf_tag(self):
        node = LeafNode("h1","And the Lord said let there be light")
        self.assertEqual(node.to_html(),"<h1>And the Lord said let there be light</h1>")
    
    def test_leaf_Valerror(self):
        node = LeafNode("a",None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
#

if __name__ == "__main__":
    unittest.main()