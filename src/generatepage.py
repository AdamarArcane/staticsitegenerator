import os
import shutil
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    mkd_file = open(from_path)
    template_file = open(template_path)
    mkd_txt = mkd_file.read()
    template_txt = template_file.read()
    html_nodes = markdown_to_html_node(mkd_txt).to_html()
    title = extract_title(mkd_txt)
    template_txt_title = template_txt.replace("{{ Title }}", title)
    template_txt_complete = template_txt_title.replace("{{ Content }}", html_nodes)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    index_path = os.path.join(dest_path, "index.html")

    with open(index_path, 'w') as index_file:
        index_file.write(template_txt_complete)
