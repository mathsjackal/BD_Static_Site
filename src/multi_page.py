# This function will recursively generate pages
import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(entry_path):
            generate_pages_recursive(
                entry_path,
                template_path,
                dest_entry_path
            )
        
        elif entry.endswith(".md"):
            html_filename = entry.replace(".md", ".html")
            dest_file_path = os.path.join(dest_dir_path, html_filename)

            generate_page(
                entry_path,
                template_path,
                dest_file_path
            )