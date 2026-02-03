# Split Nodes File
import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if old_nodes == None or old_nodes == []:
        raise Exception("Node list cannot be empty or none")

    new_nodes = []
#
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            split_string = node.text.split(delimiter)
            if len(split_string) % 2 == 0:
                raise ValueError("Unbalanced delimiter")

            for i in range(len(split_string)):
                if split_string[i] == "":
                    continue

                if i % 2 == 0:
                    new_type = TextType.TEXT
                else:
                    new_type = text_type
                
                new_nodes.append(TextNode(split_string[i],new_type))
    
    return new_nodes

def split_nodes_image(old_nodes):
    if old_nodes == None or old_nodes == []:
        raise Exception("Node list cannot be empty or none")
    
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        image_list = extract_markdown_images(text)
        if image_list == []:
            new_nodes.append(node)
            continue
        
        current_text = text
        for alt,url in image_list:
            text_split = current_text.split(f"![{alt}]({url})", 1)
            prior_text = text_split[0]
            current_text = text_split[1]

            if prior_text != "":
                prior_node = TextNode(prior_text,TextType.TEXT)
                new_nodes.append(prior_node)

          
            new_node = TextNode(alt,TextType.IMAGE,url)
            new_nodes.append(new_node)
        
        if current_text != "":
            new_node = TextNode(current_text,TextType.TEXT)
            new_nodes.append(new_node)

        
    return new_nodes






def split_nodes_link(old_nodes):
    if old_nodes == None or old_nodes == []:
        raise Exception("Node list cannot be empty or none")
    
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        links_list = extract_markdown_links(text)
        if links_list == []:
            new_nodes.append(node)
            continue
        
        current_text = text
        for alt,url in links_list:
            text_split = current_text.split(f"[{alt}]({url})", 1)
            prior_text = text_split[0]
            current_text = text_split[1]

            if prior_text != "":
                prior_node = TextNode(prior_text,TextType.TEXT)
                new_nodes.append(prior_node)
          
            new_node = TextNode(alt,TextType.LINK,url)
            new_nodes.append(new_node)
        
        if current_text != "":
            new_node = TextNode(current_text,TextType.TEXT)
            new_nodes.append(new_node)

        
    return new_nodes





def extract_markdown_images(text):
    image_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_match


def extract_markdown_links(text):
    link_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return link_match



