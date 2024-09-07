from textnode import *
from extractlinks import extract_markdown_links

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"

def split_nodes_link(old_nodes=[]):
    
    new_nodes = []
    for node in old_nodes:
        links_list = extract_markdown_links(node.text)
        if links_list ==  []:
            new_nodes.append(node)
        else:
            string = node.text
            delimiters = []
            for link in links_list:
                delimiters.append(f"[{link[0]}]({link[1]})")
            for delimiter in delimiters:
                string = " ".join(string.split(delimiter,1))
            string_list = string.split("  ")
            string_list.remove("")
            new_lst = []
            for string in string_list:
                string += " "
                new_lst.append(string)
            combolist = zip(new_lst,links_list)
            for text, link in combolist:
                new_nodes.append(TextNode(text,text_type_text))
                new_nodes.append(TextNode(link[0],text_type_link,link[1]))
    return new_nodes
