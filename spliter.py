'''
Spliter
Input: 
 - Path to a markdown file with sections deliminated
Output:
- A directory of discrete markdown files.
- A CSV with the path to each file and a summary of each section.
Description:
This script will break up a monolothinc markdown file into parts.

v0.2 2021.2.15
'''

import os

InFile = r""
OutFile = ""

def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout


def get_title(inbody):
    '''With a text, get the first line.'''
    lines = inbody.split("\n")
    title = lines[0].strip()
    return title


def save_md(filename, outbody):
    '''Export the content of the current item as a markdown file.'''
    with open(filename, 'w') as f:
        try:
            f.write(outbody)
        except Exception as e:
            print(e)


def main():
    '''Open markdown file and split by `chapter` and three carriage returns.'''
    novel = get_text_from_file(InFile)
    chapters = novel.split("## ")
    chap = -1
    for chapter in chapters:
        chap += 1
        sec = 0
        sections = chapter.split("\n\n\n")
        for section in sections:
            print(chap)
            title = get_title(section)
            filename_root = title.replace(" ", "-")
            sec += 1
            filename = "{}\{}.md".format(OutFile, filename_root)
            body = "# {}".format(section)
            save_md(filename, body)


if __name__ == "__main__":
    main()