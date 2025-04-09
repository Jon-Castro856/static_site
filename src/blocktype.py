from enum import Enum
from delimiter import markdown_to_blocks, text_to_textnode
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"

def block_to_block_type(md):
    split = md.split("\n")
   
    if md.startswith("```") and md.endswith("```"):
        return BlockType.CODE
    elif md.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEAD
    elif md.startswith(">"):
        for line in split:
            if not line.startswith(">"):
                return BlockType.PARA
        return BlockType.QUOTE
    elif md.startswith("- "):
        for line in split:
            if not line.startswith("- "):
                return BlockType.PARA
        return BlockType.U_LIST
    elif md.startswith("1. "):
        i = 1
        for line in split:
            if not line.startswith(f"{i}. "):
                return BlockType.PARA
            i += 1
        return BlockType.O_LIST
    else:
        return BlockType.PARA
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = ParentNode("div", [])
    for block in blocks:
        if block == "":
            continue
        match block_to_block_type(block):
            case(BlockType.CODE):
                pass
            case(BlockType.QUOTE):
                new_node = ParentNode("blockquote", [])
                children = text_to_children(block)
                new_node.children = children
                parent.children.append(new_node)
            case(BlockType.HEAD):
                heading = block.count("#")
                stripped = block.lstrip("# ")
                new_node = ParentNode(f"h{heading}", [])
                children = text_to_children(stripped)
                new_node.children = children
                parent.children.append(new_node)
            case(BlockType.U_LIST):
                new_node = ParentNode("ul", [])
                lines = block.split("\n")
                for line in lines:
                   stripped = line.lstrip("- ")
                   children = text_to_children(stripped)
                   list_node = ParentNode("li", children)
                   new_node.children.append(list_node)
                parent.children.append(new_node)
            case(BlockType.O_LIST):
                i = 1
                new_node = ParentNode("ol", [])
                lines = block.split("\n")
                for line in lines:
                   stripped = line.lstrip(f"{i}. ")
                   i += 1
                   children = text_to_children(stripped)
                   list_node = ParentNode("li", children)
                   new_node.children.append(list_node)
                parent.children.append(new_node)
            case(BlockType.PARA):
                new_node = ParentNode("p", [])
                children = text_to_children(block)
                new_node.children = children
                parent.children.append(new_node)
            case _:
                raise Exception("invalid blocktype")
    return parent
        

def text_to_children(text):
    node_text = text_to_textnode(text)
    html_text = []
    for node in node_text:
        html_text.append(text_node_to_html_node(node))
    return html_text