
#TODO: ADD SUPPORT FOR NEWLINE IN CODEBLOCK

def markdown_to_blocks(markdown):
    block_list = []
    markdown_list = markdown.split("\n")
    for string in markdown_list:
        if string.strip() != "":
            block_list.append(string.strip())
    return block_list
