from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

class BlockNode():
    def __init__(self,markdown_block):
        self.markdown_block = markdown_block
    
    def block_to_block_type(self):
        if self.markdown_block.startswith("#"):
            return BlockType.HEADING
        elif self.markdown_block.startswith("```") and self.markdown_block.endswith("```"):
            return BlockType.CODE
        elif self.markdown_block.startswith(">"):
            return BlockType.QUOTE
        elif self.markdown_block.startswith("-"):
            return BlockType.UNORDERED_LIST
        elif self.markdown_block.startswith("1."):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
        
    def __eq__(self,other):
        return self.markdown_block == other.markdown_block
