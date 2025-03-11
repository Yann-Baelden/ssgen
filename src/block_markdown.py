

def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        lines = block.split("\n")
        cleaned_lines = [line.strip() for line in lines]
        cleaned_block = "\n".join(cleaned_lines)
        
        if cleaned_block: 
            clean_blocks.append(cleaned_block)
    return clean_blocks