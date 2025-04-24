
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
    
    def recurse_the_tags(a_node):
        the_tag = a_node.tag
        
        for child in a_node.children:
            the_string = ParentNode.recurse_the_tags(child)

    def non_recursive_html(parent_node):
        # Verified this non recursive version works
        '''
            from htmlnode import HTMLNode
            from htmlnode import LeafNode
            from htmlnode import ParentNode

            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            In [3]: node.to_html()
            Out[3]: '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
            # That is the expected output... but its not recursive... 
        '''
        result = ""
        
        tag = parent_node.tag
        result += f"<{tag}>"
        
        for child in parent_node.children:
            
            inner_result = child.to_html()
            result += inner_result
        
        return result + f"</{tag}>"
            
        
    