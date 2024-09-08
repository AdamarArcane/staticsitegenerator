from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from htmlnode import *
from textnode import text_node_to_html_node
from texttotextnodes import text_to_textnodes
import re



def markdown_to_html_node(markdown):
    div_children = []
    block_list = markdown_to_blocks(markdown)
    for block in block_list:
        block_type = block_to_block_type(block)
        block_content = str(block)

        if block_type == "paragraph":
            children = text_to_children(block_content)
            div_children.append(HTMLNode("p",None,children))

        if block_type == "quote":
            clean_quote = block_content.strip("> ")
            children = text_to_children(clean_quote)
            div_children.append(HTMLNode("blockquote",None,children))

        #TODO: SUPPORT NESTED OL/UL
        if block_type == "unordered_list":
            list_items_list = block_content.split("\n* ")
            children = list_item_to_html_node(list_items_list)
            div_children.append(HTMLNode("ul",None,children))

        if block_type == "ordered_list":
            list_items = re.findall(r"\d+\.\s(.+)", block_content)
            children = list_item_to_html_node(list_items)
            div_children.append(HTMLNode("ol",None,children))
        
        if block_type == "code":
            clean_code = block_content.strip("```")
            div_children.append(HTMLNode("pre",None,[HTMLNode("code",clean_code,[],None)]))

        if block_type == "heading":
            if block_content.startswith("# "):
                clean_block = block_content.strip("# ")
                div_children.append(HTMLNode("h1", None, text_to_children(clean_block)))
            elif block_content.startswith("## "):
                clean_block = block_content.strip("## ")
                div_children.append(HTMLNode("h2", None, text_to_children(clean_block)))
            elif block_content.startswith("### "):
                clean_block = block_content.strip("### ")
                div_children.append(HTMLNode("h3", None, text_to_children(clean_block)))
            elif block_content.startswith("#### "):
                clean_block = block_content.strip("#### ")
                div_children.append(HTMLNode("h4", None, text_to_children(clean_block)))
            elif block_content.startswith("##### "):
                clean_block = block_content.strip("##### ")
                div_children.append(HTMLNode("h5", None, text_to_children(clean_block)))
            elif block_content.startswith("###### "):
                clean_block = block_content.strip("###### ")
                div_children.append(HTMLNode("h6", None, text_to_children(clean_block)))



    return HTMLNode("div",None,div_children)

def text_to_children(text):
    child_node_list = []
    child_block_list = text_to_textnodes(text)
    for block in child_block_list:
        child_node_list.append(text_node_to_html_node(block))
    return child_node_list

def list_item_to_html_node(list_items):
    list_items_html_nodes = []
    for item in list_items:
        if item.startswith("* "):
            clean_item = item.replace("* ", "")
            list_items_html_nodes.append(HTMLNode("li",None,text_to_children(clean_item)))
        elif item.startswith("1. "):
            clean_item = item.replace("1. ", "")
            list_items_html_nodes.append(HTMLNode("li",None,text_to_children(clean_item)))
        else:
            list_items_html_nodes.append(HTMLNode("li",None,text_to_children(item)))
    return list_items_html_nodes



text = "```\ndef hello():\n    print('Hello, World!')\n```"

processed = markdown_to_html_node(text)

print(processed)