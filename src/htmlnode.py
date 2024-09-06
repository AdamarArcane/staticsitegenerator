


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def add_props_to_html(self):
        final_prop_string = ""
        for key, value in self.props.items():
            final_prop_string += f" {key}=\"{value}\""
        return final_prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.children = []

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag == None:
            return str(self.tag)
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.add_props_to_html()}>{self.value}</{self.tag}>"