# This function will actually generate the page. 
from pathlib import Path
from block_to_html import markdown_to_html_node
from extract_title import extract_title
from htmlnode import *
import re

def generate_page(from_path, template_path, dest_path, basepath):
    # Print a status message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)

    title = extract_title(markdown)

    content_html = html_node.to_html()

    page_html = template.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", content_html)

    # Use re.sub instead of str.replace
    page_html = re.sub(r'href="/?', f'href="{basepath}', page_html)
    page_html = re.sub(r'src="/?', f'src="{basepath}', page_html)



    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page_html + "\n")

#