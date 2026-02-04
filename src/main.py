# Static Site Main:
import os
import sys
import shutil
from copystatic import copy_files_recursive
from generate_page import *
from multi_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
content_index = "./content/index.md"
template_file = "./template.html"
output_index = "./docs/index.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    if not basepath.startswith("/"):
        basepath = "/" + basepath

    if not basepath.endswith("/"):
        basepath = basepath + "/"

    #print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    #print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

if __name__ == "__main__":
    main()