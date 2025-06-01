from textnode import TextType, TextNode
import os, shutil
from utility_block import markdown_to_blocks, markdown_to_html_node

def main():
    deep_copy("static","public",0)
    #generate_page("content/index.md","template.html","public/index.html")
    generate_pages("content","template.html","public")

def deep_copy(src,dest,depth):
    if not os.path.isabs(src):
        src = os.path.join(os.getcwd(),src)
    if not os.path.isabs(dest):
        dest = os.path.join(os.getcwd(),dest)
    if not os.path.exists(src):
        raise Exception("Invalid Source Path")
    
    if os.path.isfile(src):
        shutil.copy(src,dest)
        return
    
    if not os.path.exists(dest):
        os.mkdir(dest)
    else:
        if depth == 0:
            shutil.rmtree(dest)
            os.mkdir(dest)

    files = os.listdir(src)
    for file in files:
        if file.startswith("."):
            continue
        deep_copy(os.path.join(src,file),os.path.join(dest,file),depth+1)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line.replace("#","").strip()
    raise Exception("No Title")

def generate_pages(from_path, template_path, dest_path):
    if os.path.isdir(from_path):
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        files = os.listdir(from_path)
        for file in files:
            if file.startswith("."):
                continue
            generate_pages(os.path.join(from_path,file),template_path,os.path.join(dest_path,file))
    

    if os.path.isfile(from_path):
        if not from_path.endswith(".md"):
            return

        dest_path = dest_path.replace(".md",".html")
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        with open(template_path) as f:
            html_content = f.read()
        with open(from_path) as f:
            markdown_content = f.read()
        nodes = markdown_to_html_node(markdown_content)
        html = nodes.to_html()
        title = extract_title(markdown_content)
        #html_content = html_content.format(Title=title,Content=html)
        html_content = html_content.replace("{{ Title }}",title).replace("{{ Content }}",html)
        dest_folder_path = os.path.dirname(dest_path)
        if not os.path.exists(dest_folder_path):
            os.mkdir(dest_folder_path)
        with open(dest_path,"w") as f:
            f.write(html_content)
        return html_content
            
    

if __name__ == "__main__":
    main()