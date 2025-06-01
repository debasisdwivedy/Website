from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,value=None,children=None,props=None):
        if children == None:
            raise ValueError("ParentNode Should have Children")
        if value != None:
            raise ValueError("ParentNode Should Not have Value")
        if tag == None:
            raise ValueError("ParentNode Should have Tag")
        super().__init__(tag,value,children,props)
         
    
    def to_html(self):
        s = []
        s.append(f"<{self.tag}>")
        for child in self.children:
            x = child.to_html()
            s.append(x)
                
        s.append(f"</{self.tag}>")
        return "".join(s)
        