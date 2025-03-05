class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        for key in self.props:
            print(f" {key}: {self.props[key]}")
            return f" {key}: {self.props[key]}"
    
    def __repr__(self):
        return f"Tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
