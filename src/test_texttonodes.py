# Test of text to nodes
import unittest
from text_to_nodes import text_to_textnodes
from textnode import *

class Test_Markdown_to_Nodes(unittest.TestCase):
    def test_markdown_to_textnodes(self):
        markdown = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output_set = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(output_set,text_to_textnodes(markdown))
        #print("Hello World")
    
    def test_text_to_nodes_bold(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT),
        ])

    def test_text_to_nodes_outsync(self):
        text = "This is a **bold** statement with `code blocks` and more **bold text**. "
        output_set = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" statement with ", TextType.TEXT),
            TextNode("code blocks", TextType.CODE),
            TextNode(" and more ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(". ", TextType.TEXT)
        ]
        self.assertEqual(output_set,text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()