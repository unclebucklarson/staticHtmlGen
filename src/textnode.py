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

def text_node_to_html_node(text_node):
    if text_node.value() == "text":
        pass

def main():
    text_type_instance = TextType.BOLD
    
    text_node_instance = TextNode("hating this", text_type_instance.value, "https:boot.dev")
    
    print(text_node_instance)

if __name__ == "__main__":
    main()