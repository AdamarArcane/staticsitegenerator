import re

def markdown_to_blocks(markdown):
    block_list = []
    markdown_list = markdown.split("\n")
    in_code_block = False
    current_block = []

    for line in markdown_list:
        stripped_line = line.strip()

        # Check if we are entering or exiting a code block
        if stripped_line.startswith("```"):
            if in_code_block:
                current_block.append(line)  # Add the closing fence
                block_list.append("\n".join(current_block))  # Add the entire code block
                current_block = []
            else:
                if current_block:
                    block_list.append("\n".join(current_block))  # Add any accumulated block
                    current_block = []
                current_block.append(line)  # Start the new code block
            in_code_block = not in_code_block
        elif in_code_block:
            # Inside code block, keep adding lines
            current_block.append(line)
        elif re.match(r"^\d+\.\s", stripped_line):  # Ordered list item
            # Detect ordered list items
            if current_block and not re.match(r"^\d+\.\s", current_block[0].strip()):
                block_list.append("\n".join(current_block))
                current_block = []
            current_block.append(line)
        elif re.match(r"^[\*\-\+]\s", stripped_line):  # Unordered list item
            # Detect unordered list items
            if current_block and not re.match(r"^[\*\-\+]\s", current_block[0].strip()):
                block_list.append("\n".join(current_block))
                current_block = []
            current_block.append(line)
        elif stripped_line.startswith(">"):  # Quote block
            # Detect quote blocks
            if current_block and not current_block[0].startswith(">"):
                block_list.append("\n".join(current_block))
                current_block = []
            current_block.append(line)
        elif re.match(r"^#+\s", stripped_line):  # Heading detection
            # Detect headings
            if current_block:
                block_list.append("\n".join(current_block))  # Finalize the current block
                current_block = []
            block_list.append(line)  # Add heading as a separate block
        elif stripped_line != "":
            # For non-empty lines outside of special blocks, treat as normal text
            if current_block and (re.match(r"^\d+\.\s", current_block[0].strip()) or
                                  re.match(r"^[\*\-\+]\s", current_block[0].strip()) or
                                  current_block[0].startswith(">")):
                block_list.append("\n".join(current_block))
                current_block = []
            current_block.append(line)
        else:
            # Empty lines indicate the end of a block
            if current_block:
                block_list.append("\n".join(current_block))
                current_block = []

    # Add any remaining block
    if current_block:
        block_list.append("\n".join(current_block))

    return block_list
