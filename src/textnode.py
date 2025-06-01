from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url =  url
    
    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(value=self.text)
            case TextType.BOLD:
                return LeafNode("b",self.text)
            case TextType.ITALIC:
                return LeafNode("i",self.text)
            case TextType.CODE:
                return LeafNode("code",self.text)
            case TextType.LINK:
                return LeafNode("a",self.text,props={"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img",value=self.text,props={"src": self.url,"alt": ""})
            case _:
                raise Exception("Invalid TEXT NODE")
        

    def __eq__(self,other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"