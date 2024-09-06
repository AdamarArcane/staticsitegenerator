from textnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

def split_nodes_delimiter(old_nodes=[], delimiter='', text_type=''):
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            split_text_list = node.text.split(delimiter)
            if len(split_text_list) % 2 == 0:
                raise Exception("This is not valid markdown")
            else:
                for index, item in enumerate(split_text_list):
                    if index % 2 == 0:
                        new_nodes.append(TextNode(item,text_type_text))
                    else:
                        new_nodes.append(TextNode(item,text_type))
    return new_nodes
    
