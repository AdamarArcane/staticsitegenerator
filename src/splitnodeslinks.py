from textnode import *
from extractlinks import extract_markdown_links

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_link(old_nodes=[]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            links_list = extract_markdown_links(node.text)
            if not links_list:
                new_nodes.append(node)
            else:
                remaining_text = node.text
                for link_text, url in links_list:
                    link_markdown = f"[{link_text}]({url})"
                    before, after = remaining_text.split(link_markdown, 1)
                    if before:
                        new_nodes.append(TextNode(before, text_type_text))
                    new_nodes.append(TextNode(link_text, text_type_link, url))
                    remaining_text = after
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, text_type_text))
    return new_nodes