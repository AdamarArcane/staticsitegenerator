from htmlnode import LeafNode, HTMLNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text is other.text) and (self.text_type is other.text_type) and (self.url is other.url):
            return True
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None,text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, props={"href": f"{text_node.url}"})
    elif text_node.text_type == "image":
        return LeafNode("img", "", props={"src" : f"{text_node.url}", "alt" : "alttext"})
    else:
        raise Exception(f"Not valid text_type: {text_node.text_type}")