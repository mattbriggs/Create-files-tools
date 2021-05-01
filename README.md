# File Script Tools

This is a set of scripts used to work with a markdown file to both split a larger file up into parts and then rejoin them.

- Version 0.1 2021.5.01  
- Matt Briggs

I can use PanDoc:

```command-line  
 pandoc --wrap=none -f docx -o markdown.md filetoconvert.docx
```

## Contents of the app

This project includes the following scripts:

| Name | Input | Output | Description |
| --- | --- | --- | --- |
| spliter.py | Path to a markdown file with sections delimited. | - A directory of discrete markdown files.<br>  | This script will break up a monolothinc markdown file into parts. |
| joiner.py | Path to a directory of markdown files. | Path to the joined markdown file | This script will collect markdown files and join them into a single file. |

## Release notes

| Date | Summary | Notes |
| ---  | ---     |  --   |
| 3.26.2019 | Created joined.  | First version of joiner. |
| 3.14.2019 | Created spliter | First version of spliter. |
| 5.1.2021 | Created repo | Simplified and uploaded. Part of a text analysis workflow. |