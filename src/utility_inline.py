import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        text = node.text
        type = node.text_type
        if type == TextType.TEXT:
            lines = text.split(delimiter)
            i=0
            for line in lines:
                # line = line.replace('\n',' ')
                # line = re.sub(r'\s+', ' ', line).strip()
                if line:
                    try:
                        if i%2 !=0:
                            modified_node = TextNode(line, text_type)
                        else:
                            modified_node = TextNode(line, TextType.TEXT)
                        
                        i+=1
                        result.append(modified_node)
                    except Exception as e:
                        raise Exception("INVALID TEXT NODE WITH INVALID DELIMITER IN `split_nodes_delimiter`",e)
        else:
            result.append(node)
    return result

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        text = node.text
        type = node.text_type
        if type == TextType.TEXT:
            pattern = r'!\[[^\]]*\]\([^\)]*\)'
            parts = re.split(f'({pattern})', text)

            for part in parts:
                #part = part.strip()
                if part:
                    try:
                        if part.startswith("![") and part.endswith(")"):
                            x,y = extract_markdown_images(part)[0]
                            modified_node = TextNode(x, TextType.IMAGE,y)
                        else:
                            modified_node = TextNode(part, TextType.TEXT)

                        result.append(modified_node)

                    except Exception as e:
                        raise Exception("INVALID TEXT NODE WITH INVALID DELIMITER IN `split_nodes_delimiter`",e)
        
        else:
            result.append(node)

    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        text = node.text
        type = node.text_type
        if type == TextType.TEXT:
            pattern = r"\[[^\]]+\]\([^)]+\)"
            parts = re.split(f'({pattern})', text)

            for part in parts:
                #part = part.strip()
                if part:
                    try:
                        if part.startswith("[") and part.endswith(")"):
                            x,y = extract_markdown_links(part)[0]
                            modified_node = TextNode(x, TextType.LINK,y)
                        else:
                            modified_node = TextNode(part, TextType.TEXT)

                        result.append(modified_node)

                    except Exception as e:
                        raise Exception("INVALID TEXT NODE WITH INVALID DELIMITER IN `split_nodes_delimiter`",e)
        
        else:
            result.append(node)

    return result

def text_to_textnodes(text):
    node = TextNode(text,TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_image(new_nodes)
    results = split_nodes_link(new_nodes)
    return results


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

