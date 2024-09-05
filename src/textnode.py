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