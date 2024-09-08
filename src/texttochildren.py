from texttotextnodes import text_to_textnodes
from textnode import text_node_to_html_node

def text_to_children(text):
    child_node_list = []
    child_block_list = text_to_textnodes(text)
    for block in child_block_list:
        child_node_list.append(text_node_to_html_node(block))
    return child_node_list