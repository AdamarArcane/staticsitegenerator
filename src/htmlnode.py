


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