from enum import Enum

class TextType(Enum):
    # Not really sure what should be represented here... 
    BOLD = "bold"
    ITALIC = "Italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"
    
class TextNode():
    
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type # this is supposed to be a TextType enum
        self.url = url
    
    def __eq__(self, value: TextType) -> bool:
        
        if self.text == value.text and self.text_type == value.text_type and self.url == value.url:
            return True
        
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        # print some stuff here about the object... 
        
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
  
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        
        return_string = str()
        
        for key in self.props:
            return_string += f' {key}="{self.props[key]}"'

        return return_string

class LeafNode(HTMLNode):
    
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

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("tag cannot be  none")
        
        if self.children == None:
            raise ValueError("Children canot be none")

        result = f"<{self.tag}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        
        return result


def text_node_to_html_node(text_node: TextNode):
    
    if text_node.text_type == TextType.TEXT:
        # return a leaf node with no tag just raw text 
        return LeafNode(None, value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.url})
    else:
        raise ValueError("That is not a valid Text Type")