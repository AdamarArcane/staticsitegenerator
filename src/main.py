from textnode import TextNode
from copysrctodst import copy_src_to_dst
from generatepage import generate_page

def main():
    copy_src_to_dst("static", "public")
    generate_page("content/index.md", "template.html", "public/")

main()