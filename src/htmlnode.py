
class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        tag = self.tag
        value = self.value
        children = self.children 
        props = self.props
    
    def __repr__(self):
        # print some stuff here about the object... 
        
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
  
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        
        return_string = str()
        
        for key in self.props:
            return_string += f' "{key}"={self.props[key]}'

        return return_string

    