from htmlnode import HTMLNode

class LEAFNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def __repr__(self):
        # Override the parent __repr__ method
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"

    def to_html(self):
        # no value, raise a ValueError
        if self.value == None:
            raise ValueError
        # no tag (ie None), value shoudl be returned as raw text
        elif self.tag == None:
            return self.value
        # other wise return the leaf
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"