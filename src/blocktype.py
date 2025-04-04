from enum import Enum
import re

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
            if not line.startswith(f"{i}."):
                return BlockType.PARA
            i += i
        return BlockType.O_LIST
    else:
        return BlockType.PARA

