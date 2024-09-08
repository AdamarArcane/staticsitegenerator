import os
import shutil
from generatepage import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for item in files:
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, dest_dir_path)
        else:
            new_dir_path_content = os.path.join(dir_path_content, item)
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)
