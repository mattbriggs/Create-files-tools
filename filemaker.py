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

from csv import reader

INFILE = r"C:\Users\mabrigg\OneDrive - Microsoft\Review_in\2021_06\kwic\corpus.csv"
OUTPATH = "C:\\Users\\mabrigg\\OneDrive - Microsoft\\Review_in\\2021_06\\kwic\\corpus\\"
HEADERS = []

def get_text_from_file(path):
    '''Return text from a text filename path'''
    textout = ""
    fh = open(path, "r", encoding="utf8")
    for line in fh:
        textout += line
    fh.close()
    return textout


def open_csv(filename):
    '''read csv file as a list of lists'''
    with open(filename, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        return list_of_rows


def save_md(filename, outbody):
    '''Export the content of the current item as a markdown file.'''
    with open(filename, 'w') as f:
        try:
            f.write(outbody)
        except Exception as e:
            print(e)


def main():
    '''Open markdown file and split by `chapter` and three carriage returns.'''
    global HEADERS
    parts = open_csv(INFILE)
    for indx, part in enumerate(parts):
        if indx == 0:
            HEADERS = parts[0]
        if indx > 0:
            filebody = ""
            for slot, field in enumerate(part):
                if slot == 0:
                    filebody = filebody + "# {}:{}\n\n".format(HEADERS[slot], field)
                else:
                    if field:
                        filebody = filebody + "**{}**: {}\n\n".format(HEADERS[slot], field)
            out_path = OUTPATH + str(indx) + ".md"
            print("Saving... {}".format(out_path))
            save_md(out_path, filebody)


if __name__ == "__main__":
    main()
