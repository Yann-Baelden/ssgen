from markdown_blocks import (markdown_to_blocks, block_to_block_type, BlockType)
from htmlnode import (HTMLNode, LeafNode, ParentNode)
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    bloks = markdown_to_blocks(markdown)
    all_nodes = []
    for block in bloks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.QUOTE:
                quote_text = block[2:].strip()
                html_node = ParentNode("blockquote", text_to_children(quote_text))
                all_nodes.append(html_node)
            case BlockType.ULIST:
                items = block.split("\n- ")
                items = [item for item in items if item]
                li_nodes = []
                for item in items:
                    li_nodes = ParentNode("li", text_to_children(item))
                    li_nodes.append(li_node)
                html_node = ParentNode("ul", li_nodes)
                all_nodes.append(html_node)
            case BlockType.OLIST:
                lines = block.split("\n")
                li_nodes = []
                for line in lines:
                    if not line.strip():
                        continue
                    pos = 0
                    while pos < len(line) and (line[pos].isdigit() or line[pos] in '. '):
                        pos +=1
                    item_text = line[pos:].strip()
                    li_node = ParentNode("li", text_to_children(item_text))
                    li_nodes.append(li_node)
                
                html_node = ParentNode("ol", li_nodes)
                all_nodes.append(html_node)
            case BlockType.CODE:
                code_content = block.strip("```")
                code_node = LeafNode("code", code_content)
                pre_node = ParentNode("pre", [code_node])
                all_nodes.append(pre_node)
            case BlockType.HEADING:
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                
                level = min(6, level)
                title_text = block[level:].strip()
                title_node = ParentNode(f"h{level}", text_to_children(title_text))
                all_nodes.append(title_node)
            case BlockType.PARAGRAPH:
                paragraph_text = block.replace("\n", " ")
                html_node = ParentNode("p", text_to_children(paragraph_text))
                all_nodes.append(html_node)
    parent_node = ParentNode("div", all_nodes)
    return parent_node

