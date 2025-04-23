import os
import shutil
from blocktype import markdown_to_html_node 
def main():
    base = os.getcwd()
    static = base + "/static"
    public = base + "/public"
    content = base + "/content"
    del_directory(public)
    copy_files(static, public)
    generate_page(content, base, public)

def del_directory(directory):
    print(f"Deleting contents of {directory}")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
           print(f"Removing {filename}")
           os.remove(file_path)
        elif os.path.isdir(file_path):
           print(f"Removing Folder: {filename}")
           shutil.rmtree(file_path)

def copy_files(copy_dir, paste_dir):
    print(f"copying files from {copy_dir} to {paste_dir}")
    for filename in os.listdir(copy_dir):
        path = os.path.join(copy_dir, filename)
        if os.path.isdir(path):
            print(f"{filename} is a folder")
            new_start = path
            new_dest = paste_dir + "/" + filename
            os.mkdir(new_dest)
            copy_files(new_start, new_dest)
        elif os.path.isfile(path):
           print(f"copying {filename} to {paste_dir}")
           shutil.copy(path, paste_dir)

def extract_title(markdown):
    lines = markdown.split("\n")
    if lines[0].startswith("# "):
        stripped_head = lines[0].strip("#").strip()
    else:
        raise Exception("No Heading")
    return stripped_head

def generate_page(from_path, template_path, dest_path):
    print(f"Beginning to read {from_path} to {dest_path} using {template_path}.")
    print("Opening content and template files")
    file = open(from_path + "/index.md", "r")
    template = open(template_path + "/template.html", "r")
    content = file.read()
    temp_copy = template.read()
    print("Extracting Header from content\n---")
    heading = extract_title(content)
    print(f"header is {heading}\n---")
    print("converting content into html\n---")
    html_content = markdown_to_html_node(content)
    print(f"content succesfully converted\n---")
    temp_copy = temp_copy.replace("{{ Title }}", heading).replace("{{ Content }}", html_content.to_html())
    file.close()
    template.close()
    print("Creating new file for webpage")
    webpage = open(dest_path + "/index.html", "w")
    webpage.write(temp_copy)


main()