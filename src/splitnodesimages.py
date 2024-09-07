from textnode import *
from extractlinks import extract_markdown_images

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_image(old_nodes=[]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            images_list = extract_markdown_images(node.text)
            if not images_list:
                new_nodes.append(node)
            else:
                remaining_text = node.text
                for alt_text, url in images_list:
                    image_markdown = f"![{alt_text}]({url})"
                    before, after = remaining_text.split(image_markdown, 1)
                    if before:
                        new_nodes.append(TextNode(before, text_type_text))
                    new_nodes.append(TextNode(alt_text, text_type_image, url))
                    remaining_text = after
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, text_type_text))
    return new_nodes