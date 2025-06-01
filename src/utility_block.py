from blocknode import BlockNode, BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from utility_inline import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = []
    lines= markdown.split("\n\n")
    for line in lines:
        line = line.strip()
        if line:
            blocks.append(BlockNode(line))
    return blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div",None,[])
    children = []
    for block in blocks:
        type = block.block_to_block_type()
        if BlockType.CODE == type:
            nodes = get_HTMLNode(block.markdown_block,type)
        else:
            nodes = get_HTMLNode(block.markdown_block,type)
        children.append(nodes)
    parent_node.children=children
    return parent_node

def get_HTMLNode(text,type):
    children = []
    if BlockType.HEADING == type:
        count = text.count("#")
        text = text.replace("#","")
        parent_node = ParentNode(f"h{count}",None,[])
        text_nodes = text_to_textnodes(text)
        for text_node in text_nodes:
            children.append(text_node.text_node_to_html_node())
        parent_node.children=children
        return parent_node
    elif BlockType.CODE == type:
        import re
        text = text.replace("```\n","")
        text = text.replace("```","")
        parent_node = ParentNode("pre",None,[])
        text = text.replace("\n","\\n")
        text = re.sub(r'\s+', ' ', text).strip()
        child_node = LeafNode("code",text)
        parent_node.children=[child_node]
        return parent_node
    elif BlockType.QUOTE == type:
        text = text.replace(">","")
        parent_node = ParentNode("blockquote",None,[])
        text_nodes = text_to_textnodes(text)
        for text_node in text_nodes:
            children.append(text_node.text_node_to_html_node())
        parent_node.children=children
        return parent_node
    elif BlockType.UNORDERED_LIST == type:
        lines = text = text.split("\n")
        parent_node = ParentNode("ul",None,[])
        for line in lines:
            line = line.replace("- ","")
            node = ParentNode("li",None,[])
            grandchildren = []
            text_nodes = text_to_textnodes(line)
            for text_node in text_nodes:
                grandchildren.append(text_node.text_node_to_html_node())
            node.children = grandchildren
            children.append(node)
        parent_node.children=children
        return parent_node
    elif BlockType.ORDERED_LIST == type:
        import re
        lines = text = text.split("\n")
        parent_node = ParentNode("ol",None,[])
        for line in lines:
            line = re.sub(r'^\d+\.\s*', '', line, flags=re.MULTILINE)
            node = ParentNode("li",None,[])
            grandchildren = []
            text_nodes = text_to_textnodes(line)
            for text_node in text_nodes:
                grandchildren.append(text_node.text_node_to_html_node())
            node.children = grandchildren
            children.append(node)
        parent_node.children=children
        return parent_node
    elif BlockType.PARAGRAPH == type:
        import re
        parent_node = ParentNode("p",None,[])
        text = text.replace("\n"," ")
        text = re.sub(r'\s+', ' ', text).strip()
        text_nodes = text_to_textnodes(text)
        for text_node in text_nodes:
            children.append(text_node.text_node_to_html_node())
        parent_node.children=children
        return parent_node
    else:
        raise Exception("Invalid BLOCK NODE TYPE")


# if __name__ == "__main__":
#     test_codeblock()