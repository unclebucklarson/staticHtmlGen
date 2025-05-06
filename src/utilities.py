from htmlnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from htmlnode import TextType
from htmlnode import text_node_to_html_node

import re

def split_nodes_delimiter_initial(old_nodes, delimiter, text_type):
    
    # There are multiple things going on here...m
    # We are converting raw markdown??? or not??? what is going on...
    
    type_of_node = str()
    new_nodes = list()
    
    for node in old_nodes:
        
        # split markdown into nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # how to get the indexes of the delimiters...
        # Ensure there is an opening and a closing delimiter 
        
        if delimiter in node.text:
            split_text = node.text.split(delimiter)
            
            for index, text in enumerate(split_text):
                if index == 1:
                    new_node = TextNode(node.text, text_type)
                    new_nodes.append(new_node)
                else:
                    new_nodes.append(node)
        else:
            new_nodes.append(node)
    
    return new_nodes


def find_all_occurrences(string, substring):
    # break the occurance of the delimiter into start and stops..
    
    occurrences = []
    start_position = 0
    
    while True:
        
        position = string.find(substring, start_position)
        
        if position == -1:
            break
        
        occurrences.append(position)
        
        start_position = position + len(substring)  # Start search from the next character
    
    chunk_size = 2
    
    # Return a list of lists with start and stop, and if there is an unmatched tag a boolean
    unmatched = False
    
    start_and_stops = [occurrences[i:i + chunk_size] for i in range(0, len(occurrences), chunk_size)]
    
    for occurence in start_and_stops:
        if len(occurence) < 2:
            unmatched = True
    
    return start_and_stops, unmatched

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = list()
    
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue 
        
        results, unmatched_tags = find_all_occurrences(node.text, delimiter)
        
        if unmatched_tags:
            raise UnboundLocalError("Unclosed tag found")
        
        elif len(results) < 1:
             new_nodes.append(node)
             continue
        
        # Process each segment of the node text, the pairs of the array.
        # while there are more elements read in two, thesse SHOULD be start and stop elements.

            # split the text (done above)
            # Create new nodes
            # index zero to 
        start_pos = 0
        
        if results[0][0] != 0: 
            # needed in case the tag is at the beginning of the line
            end_pos = results[0][0] # the start position of the first tag
            new_nodes.append(TextNode(node.text[start_pos:end_pos], TextType.TEXT, node.url))

        for index, reult in enumerate(results):
            
            # Process text until no more pairs
        
        