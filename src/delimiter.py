from textnode import TextNode, TextType
import re

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
            raise ValueError("invalid markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_list.extend(split_nodes)
    return new_list

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        line = node.text
        images = extract_markdown_images(line)
        if len(images) == 0:
            new_list.append(node)
            continue
        for tuple in images:
            image_alt, image_link = tuple
            sections = line.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown")
            if sections[0] != "":
                new_list.append(TextNode(sections[0], TextType.TEXT))
            new_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
            line = sections[1]
        if line != "":
            new_list.append(TextNode(line, TextType.TEXT))
    return new_list
    

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        line = node.text
        links = extract_markdown_links(line)
        if len(links) == 0:
            new_list.append(node)
            continue
        for tuple in links:
            link_text, link_url = tuple
            sections = line.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown")
            if sections[0] != "":
                new_list.append(TextNode(sections[0], TextType.TEXT))
            new_list.append(TextNode(link_text, TextType.LINK, link_url))
            line = sections[1]
        if line != "":
            new_list.append(TextNode(line, TextType.TEXT))
    return new_list

def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]
    parsed_nodes = split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_image(
                    split_nodes_link(nodes)
                ),
            "`", TextType.CODE),
        "_", TextType.ITALIC),
    "**", TextType.BOLD)
    return parsed_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
"""
        if "\n" in line:
            newsplit = line.split("\n")
            stripped = list(map(lambda x: x.strip(), newsplit))
            joined = "\n".join(stripped).rstrip("\n").lstrip("\n")
            new_list.append(joined)
            continue"
        """