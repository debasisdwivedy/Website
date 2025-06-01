from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,children=None,props=None):
        if children != None:
            raise ValueError("LeafNode should have not have Children")
        if value == None:
            raise ValueError("LeafNode have Value")
        super().__init__(tag,value,children,props)
    
    def to_html(self):
        if self.tag!=None:
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
        
        