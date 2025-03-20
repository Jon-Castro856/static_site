from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    limiters = ["**", "_", "`"]
    new_list = []
    if delimiter not in limiters:
        raise ValueError("Incorrect delimiter")
    for node in old_nodes:
        if node.text_type != text_type.TEXT:
           new_list.append(node)
        else:
            text = node.text.split(delimiter)
               
        


    
    return new_list