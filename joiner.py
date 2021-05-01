'''
Joiner
Input: 
 - Path to a directory of markdown files.
Output:
-  Path to the joined markdown file
- A CSV with the path to each file and a summary of each section.
Description:
This script will collect markdown files and join them into a single file.

v0.1 2019.3.26
'''

import os

InDir = ""
Outfile = r""

def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r")
    for line in fh:
        textout += line
    fh.close()
    return textout

def get_files(inpath):
    '''With the directory path, returns a list of markdown file paths.'''
    outlist = []
    for (path, dirs, files) in os.walk(inpath):
        for filename in files:
            ext_index = filename.find(".")
            if filename[ext_index+1:] == "md":
                entry = path + "\\" + filename
                outlist.append(entry)
    return outlist


def save_md(filename, outbody):
    '''Export the content of the current item as a markdown file.'''
    with open(filename, 'w') as f:
        try:
            f.write(outbody)
        except Exception as e:
            print(e)


def main():
    '''Open markdown file and join each file.'''
    print("Rolling files.")
    listoffiles = get_files(InDir)
    novel = ""
    for f in listoffiles:
        filebody = ""
        try:
            filebody = get_text_from_file(f)
        except Exception as e:
            print(e)
        novel += filebody + "\n"
    save_md(Outfile, novel)
    print("Collected files and saved to : " + Outfile)


if __name__ == "__main__":
    main()