from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    limiters = ["**", "_", "`"]
    new_list = []
    if delimiter not in limiters:
        raise ValueError("Incorrect delimiter")
    for node in old_nodes:
        if node.text_type != text_type.TEXT:
           new_list.append(node)
           continue
    split_nodes = []
    sections = node.text.split(delimiter)
    if len(sections) % 2 == 0:
        raise ValueError("invalid martkdown")
    for i in range(len(sections)):
        if sections[i] == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(sections[i], TextType.TEXT))
        else:
            split_nodes.append(TextNode(sections[i], text_type))
    new_list.extend(split_nodes)
    return new_list