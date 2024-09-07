

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        true_quote = True
        block_list = block.split("\n")
        for item in block_list:
            if not item.startswith('>'):
                true_quote = False
        if true_quote:
            return "quote"
        else:
            return "paragraph"
    elif block.startswith("* ") or block.startswith("- "):
        true_ulist = True
        block_list = block.split("\n")
        for item in block_list:
            if not item.startswith('* ') and not item.startswith('- '):
                true_ulist = False
        if true_ulist:
            return "unordered_list"
        else:
            return "paragraph"
    elif block.startswith("1. "):
        true_olist = True
        ol_index = 0
        block_list = block.split("\n")
        for item in block_list:
            ol_index += 1
            if not item.startswith(f"{ol_index}. "):
                true_olist = False
        if true_olist:
            return "ordered_list" 
        else:
            return "paragraph"
    else:
        return "paragraph"
