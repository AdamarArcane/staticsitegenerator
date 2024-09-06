


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

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        return False



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.children = []

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode needs value")
        if self.tag == None:
            return str(self.value)
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.add_props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        self.tag = tag
        self.value = ""
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def add_child(self, child_node):
        self.children.append(child_node)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode needs tag")
        if self.children == None:
            raise ValueError("ParentNode needs children")


        opening_tag = f"<{self.tag}"

        props_string = self.add_props_to_html()
        if props_string:
            opening_tag += f" {props_string}"

        opening_tag += ">"


        content = self.value
        for child in self.children:
            content += child.to_html()
        
        closing_tag = f"</{self.tag}>"

        return f"{opening_tag}{content}{closing_tag}"