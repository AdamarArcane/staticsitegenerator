from textnode import TextNode
from splitnodes import split_nodes_delimiter
from splitnodeslinks import split_nodes_link
from splitnodesimages import *

def text_to_textnodes(text):
    init_node = [TextNode(text, text_type_text)]
    
    code_nodes = split_nodes_delimiter(init_node, "`", text_type_code)
    link_nodes = split_nodes_link(code_nodes)
    image_nodes = split_nodes_image(link_nodes)
    bold_nodes = split_nodes_delimiter(image_nodes, "**", text_type_bold)
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", text_type_italic)
    
    return italic_nodes
