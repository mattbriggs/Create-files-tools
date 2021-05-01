# Gordian Novel

This is a set of scripts used to work with a markdown file to both split a larger file up into parts and then rejoin them.

- Version 0.1 2019.3.26  
- Matt Briggs

I began working on this for the, hopefully final revision of _Monsters of the Air_ in the spring of 2019.

I can use PanDoc:

```command-line  
 pandoc --wrap=none -f docx -o markdown.md filetoconvert.docx
```

## Contents of the app

This project includes the following scripts:

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| spliter.py | Path to a markdown file with sections deliminated | - A directory of discrete markdown files.<br>  | This script will break up a monolothinc markdown file into parts. |
| joiner.py | Path to a directory of markdown files. | Path to the joined markdown file | This script will collect markdown files and join them into a single file. |
| summarize.py | Path to a director of markdown files. | A CSV with the path to each file and a summary of each section. | Creates a catalog and summarization of the markdown files. | 

## Release notes

| Date | Summary | Notes |
| ---  | ---     |  --   |
| 3.26.2019 | Created joined.  | First version of joiner. |
| 3.14.2019 | Created spliter and summarize | First version of spliter. |