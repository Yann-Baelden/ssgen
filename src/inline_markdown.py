import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        images = extract_markdown_images(old_node.text)
        if not images:
            result.append(old_node)
            continue
        
        current_text = old_node.text

        for alt, link in images:
            image_markdown = f"![{alt}]({link})"
            sections = current_text.split(image_markdown, 1)
            
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
                
            result.append(TextNode(alt, TextType.IMAGE, link))
            
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
        
        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))

    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        links = extract_markdown_links(old_node.text)
        if not links:
            result.append(old_node)
            continue

        current_text = old_node.text
            
        for href, link in links:
            link_markdown = f"[{href}]({link})"
            sections = current_text.split(link_markdown, 1)
            
            if sections[0]:
                result.append(TextNode(sections[0], TextType.TEXT))
                
            result.append(TextNode(href, TextType.LINK, link))
            
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
        
        if current_text:
            result.append(TextNode(current_text, TextType.TEXT))
            
    return result
