# Text to TextNodes
#Takes markdown text and converts it into text nodes.

from textnode import *
from split_nodes import *

def text_to_textnodes(text):
    if text is None or text == "":
        raise ValueError("Text cannot be None or an empty string")

    #convert text into a single text node list
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)

    return nodes

# Write tests to continue lesson. 