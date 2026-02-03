# Unit Tests for the split nodes function.
import unittest

from textnode import *
from split_nodes import *

class TestSplitNode(unittest.TestCase):

    
    def test_single_bold(self):
        node = [TextNode("This is **bold** text", TextType.TEXT)]
        new_list = split_nodes_delimiter(node,"**",TextType.BOLD)
        
        self.assertEqual(len(new_list),3)

        self.assertEqual(new_list[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(new_list[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_list[2], TextNode(" text", TextType.TEXT))
        
    def test_first_bold(self):
        node = [TextNode("**Bold** at the start", TextType.TEXT)]
        new_list = split_nodes_delimiter(node,"**",TextType.BOLD)
        
        self.assertEqual(len(new_list),2)

        self.assertEqual(new_list[0], TextNode("Bold", TextType.BOLD))
        self.assertEqual(new_list[1], TextNode(" at the start", TextType.TEXT))     

    def test_multiple_bold(self):
        node = [TextNode("**Bold** at **the** start", TextType.TEXT)]
        new_list = split_nodes_delimiter(node,"**",TextType.BOLD)

        self.assertEqual(len(new_list),4)
        self.assertEqual(new_list[0],TextNode("Bold", TextType.BOLD))
        self.assertEqual(new_list[1],TextNode(" at ", TextType.TEXT))
        self.assertEqual(new_list[2],TextNode("the", TextType.BOLD))
        self.assertEqual(new_list[3],TextNode(" start", TextType.TEXT))

    def test_plain_split(self):
        node = [TextNode("This is a plain text string", TextType.TEXT)]
        new_list = split_nodes_delimiter(node,"**",TextType.BOLD)
        self.assertEqual(node,new_list)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.youtube.com"
                ),
            ],
            new_nodes,
        )

class TestMarkdownImages(unittest.TestCase):

    def test_imagemarkdown(self):
        markdown_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        #print(extract_markdown_images(markdown_image))
        output_set = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(output_set,extract_markdown_images(markdown_image))
    
    def test_no_image(self):
        input_text = "This is just plain text without any image link"
        output_set = []
        self.assertEqual(output_set,extract_markdown_images(input_text))
    
    def test_single_image(self):
        markdown_image = "![test image](https://www.not_real_link.com)"
        output_set = [('test image', 'https://www.not_real_link.com')]
        self.assertEqual(output_set,extract_markdown_images(markdown_image))
    
    def test_broken_image(self):
        markdown_image = "![test image]"
        output_set = []
        self.assertEqual(output_set,extract_markdown_images(markdown_image))


class TestMarkdownLinks(unittest.TestCase):

    def test_linkmarkdown(self):
        markdown_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        #print(extract_markdown_images(markdown_image))
        output_set = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(output_set,extract_markdown_links(markdown_link))
    
    def test_no_link(self):
        input_text = "This is just plain text without any image link"
        output_set = []
        self.assertEqual(output_set,extract_markdown_links(input_text))
    
    def test_single_link(self):
        markdown_link = "[to boot dev](https://www.boot.dev)"
        output_set = [('to boot dev', 'https://www.boot.dev')]
        self.assertEqual(output_set,extract_markdown_links(markdown_link))
    
    def test_broken_link(self):
        markdown_link = "[to boot dev]"
        output_set = []
        self.assertEqual(output_set,extract_markdown_links(markdown_link))

if __name__ == "__main__":
    unittest.main()
