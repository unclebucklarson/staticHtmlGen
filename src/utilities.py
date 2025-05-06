from htmlnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import TextType
from htmlnode import text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    type_of_node = str()
    new_nodes = list()
    
    if delimiter == "**":
        type_of_node = TextType.BOLD
    elif delimiter ==  "`":
        type_of_node = TextType.CODE
    elif delimiter == "_":
        type_of_node = TextType.ITALIC
    else:
        typte_of_text = TextType.TEXT
    
    for node in old_nodes:
        
        if node.TextType != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)
        
        
    pass

