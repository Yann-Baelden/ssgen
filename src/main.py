from textnode import TextNode, TextType
import os
import shutil


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

def copy_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    dir_list = os.listdir(source)
    for item in dir_list:
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        elif os.path.isdir(item_path):
            new_dir = os.path.join(destination, item)
            os.mkdir(new_dir)
            copy_static_to_public(item_path, new_dir)
        else:
            print(f"Unknown type ignored : {item_path}")
main()

if __name__ == "__main__":
    copy_static_to_public('static', 'public')