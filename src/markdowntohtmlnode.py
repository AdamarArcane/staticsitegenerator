from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from htmlnode import *
from textnode import text_node_to_html_node
from texttotextnodes import text_to_textnodes
from texttochildren import text_to_children
from listitemtohtmlnode import list_item_to_html_node
import re



def markdown_to_html_node(markdown):
    div_children = []
    block_list = markdown_to_blocks(markdown)
    for block in block_list:
        block_type = block_to_block_type(block)
        block_content = str(block)

        if block_type == "paragraph":
            children = text_to_children(block_content)
            div_children.append(ParentNode("p", children))

        if block_type == "quote":
            clean_quote = block_content.strip("> ")
            children = text_to_children(clean_quote)
            div_children.append(ParentNode("blockquote", children))

        #TODO: SUPPORT NESTED OL/UL
        if block_type == "unordered_list":
            list_items_list = block_content.split("\n* ")
            children = list_item_to_html_node(list_items_list)
            div_children.append(ParentNode("ul", children))

        if block_type == "ordered_list":
            list_items = re.findall(r"\d+\.\s(.+)", block_content)
            children = list_item_to_html_node(list_items)
            div_children.append(ParentNode("ol", children))
        
        if block_type == "code":
            clean_code = block_content.strip("```")
            div_children.append(ParentNode("pre", [LeafNode("code", clean_code)]))

        if block_type == "heading":
            if block_content.startswith("# "):
                clean_block = block_content.strip("# ")
                div_children.append(ParentNode("h1", text_to_children(clean_block)))
            elif block_content.startswith("## "):
                clean_block = block_content.strip("## ")
                div_children.append(ParentNode("h2", text_to_children(clean_block)))
            elif block_content.startswith("### "):
                clean_block = block_content.strip("### ")
                div_children.append(ParentNode("h3", text_to_children(clean_block)))
            elif block_content.startswith("#### "):
                clean_block = block_content.strip("#### ")
                div_children.append(ParentNode("h4", text_to_children(clean_block)))
            elif block_content.startswith("##### "):
                clean_block = block_content.strip("##### ")
                div_children.append(ParentNode("h5", text_to_children(clean_block)))
            elif block_content.startswith("###### "):
                clean_block = block_content.strip("###### ")
                div_children.append(ParentNode("h6", text_to_children(clean_block)))



    return ParentNode("div", div_children)