from textnode import TextNode, TextType

print("hello world")

def main():
    new_TextNode = TextNode("This is a text", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(new_TextNode)

main()