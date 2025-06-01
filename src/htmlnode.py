class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = []
        for k,v in self.props.items():
            result.append(f" {k}=\"{v}\"")
        return "".join(result)
    
    def __repr__(self):
        result = ["HTMLNode("]
        if self.tag is not None:
            result.append(f"TAG = ({self.tag})")
        if self.value is not None:
            result.append(f"VALUE = ({self.value})")
        if self.children is not None:
            result.append(f"CHILDREN = ({self.children})")
        if self.props is not None:
            result.append(f"PROPERTIES = {self.props_to_html()}")
        
        result.append(")")
        return "\n".join(result)