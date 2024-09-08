from htmlnode import ParentNode
from texttochildren import text_to_children

def list_item_to_html_node(list_items):
    list_items_html_nodes = []
    for item in list_items:
        if item.startswith("* "):
            clean_item = item.replace("* ", "")
            list_items_html_nodes.append(ParentNode("li", text_to_children(clean_item)))
        elif item.startswith("1. "):
            clean_item = item.replace("1. ", "")
            list_items_html_nodes.append(ParentNode("li", text_to_children(clean_item)))
        else:
            list_items_html_nodes.append(ParentNode("li", text_to_children(item)))
    return list_items_html_nodes