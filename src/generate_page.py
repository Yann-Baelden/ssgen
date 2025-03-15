import os
import markdown_blocks
from copystatic import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as md_file:
        md_content = md_file.read()
    
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    title = extract_title(md_content)
    html_node = markdown_blocks.markdown_to_html_node(md_content)
    html_content = html_node.to_html()

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)