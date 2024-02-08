# Zuru_Test_One
This is a repository of first test "Write a Python program, that takes a json file (which contains the information of a directory in nested structure) and prints out its content in the console in the style of ls (linux utility)"

# Zuru Command line utilities
This module or program takes json (which contains the information of a directory in nested structure) file data as input and gives the output in the console as per the command form or pass by the user in the style of ls (linux utility)
Here user has to type different commands and program will give output as per the command. 
Let's take an examples if user types "pyls", it will list out the top level (in the directory interpreter) directories and files. Notice it does not list .gitignore,
because that is the default behaviour of ls, i.e. files and directories whose names start with . are omitted by default. it is as follows:
LICENSE         README.md           ast go.mod          lexer           main.go         parser          token

## Table of Contents
- [Installation](#installation)
- [Usage](#usage) - Commands
- [Functions](#functions)
- [Test Functions -Pytes](#functions)


## Installation
### Dependencies

- Python 3.x
- Pytest

### Steps

1. Clone the repository: "https://github.com/dattachitale/Zuru_Test_One"
2. Open Pycharm and load the script 
3. run the scrip by using Pycharm runner (form neccessary command) or using terminal type "python -m pyls"
4. Form neccessary command combination which is explained in "Usage" section


## Usage

### Commands
for all the command, use "pyls" at the beginning and the flags if you are using it in terminal e.g "pyls -l"
if you are running using Pycharm "run" button then in "Edit configuaration -> Parameters add your flags (-l -r) but no need to add "pyls"

#### python -m pyls : gives list of top level (in the directory interpreter) directories and files. Notice it does not list .gitignore,
LICENSE         README.md           ast go.mod          lexer           main.go         parser          token

#### python -m pyls -A : gives all the files and directories (including files starting with '.')
.gitignore      LICENSE         README.md           ast go.mod          lexer           main.go         parser          token

#### python -m pyls -l : list out all top level directories and files with detail information
-rw-r--r-- 1071 Nov 14 11:27 LICENSE
-rw-r--r-- 83 Nov 14 11:27 README.md
drwxr-xr-x 4096 Nov 14 15:58 ast
-rw-r--r-- 60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 17 12:51 parser
drwxr-xr-x 4096 Nov 14 14:57 token

#### python -m pyls -l -r: list out all top level directories and files with detail information in reverse order
drwxr-xr-x 4096 Nov 14 14:57 token
drwxr-xr-x 4096 Nov 17 12:51 parser
-rw-r--r-- 74 Nov 14 13:57 main.go
drwxr-xr-x 4096 Nov 14 15:21 lexer
-rw-r--r-- 60 Nov 14 13:51 go.mod
drwxr-xr-x 4096 Nov 14 15:58 ast
-rw-r--r-- 83 Nov 14 11:27 README.md
-rw-r--r-- 1071 Nov 14 11:27 LICENSE

#### python -m pyls -l -r -t: list out all top level directories and files with detail information in reverse order of reverse order of "time_modified" filter
drwxr-xr-x 4096 Nov 17 12:51 parser
drwxr-xr-x 4096 Nov 14 15:58 ast
drwxr-xr-x 4096 Nov 14 15:21 lexer
drwxr-xr-x 4096 Nov 14 14:57 token
-rw-r--r-- 74 Nov 14 13:57 main.go
-rw-r--r-- 60 Nov 14 13:51 go.mod
-rw-r--r-- 1071 Nov 14 11:27 LICENSE
-rw-r--r-- 83 Nov 14 11:27 README.md


#### python -m pyls -l -r -t --filter=<option>: list out either file or dir as per filter option (file dir)
python -m pyls -l -r -t --filter=dir
drwxr-xr-x 4.0 KB Nov 17 12:51 parser
drwxr-xr-x 4.0 KB Nov 14 15:21 lexer
drwxr-xr-x 60.0 B Nov 14 13:51 go.mod
drwxr-xr-x 1.0 KB Nov 14 11:27 LICENSE
drwxr-xr-x 83.0 B Nov 14 11:27 README.md

python -m pyls -l -r -t --filter=file
-rw-r--r-- 4.0 KB Nov 14 15:58 ast
-rw-r--r-- 4.0 KB Nov 14 14:57 token
-rw-r--r-- 74.0 B Nov 14 13:57 main.go

python -m pyls -l -r -t --filter=folder
error: 'folder' is not a valid filter criteria. Available filters are 'dir' and 'file'


#### python -m pyls -l (file/dir name): this will handle file/dir path properly and gives all sub files if it is dir and file itself if it is a file 
python -m pyls -l parser
drwxr-xr-x 1342 Nov 17 12:51 parser_test.go
-rw-r--r-- 1622 Nov 17 12:05 parser.go
drwxr-xr-x 533 Nov 14 16:03 go.mod

python -m pyls -l parser/parser.go
-rw-r--r-- 1622 Nov 17 12:05 parser/parser.go

python -m pyls -l lexer
drwxr-xr-x 1729 Nov 14 15:15 lexer_test.go
-rw-r--r-- 227 Nov 14 12:23 go.mod
drwxr-xr-x 2886 Nov 14 15:21 lexer.go

python -m pyls -l non_existent_path
error: cannot access 'non_existent_path': No such file or directory


#### python -H (file/dir name): this is new -H flag which I implemented along with file name, so you have to pass "pyls -H <filename>" only. This does not work with pyls -l -H <filename>
This command will give "Size" parameter in human-readable form as below

python -m pyls -H lexer  (use only like pyls -H <filename>)
drwxr-xr-x 1.7 KB Nov 14 15:15 lexer_test.go
-rw-r--r-- 227.0 B Nov 14 12:23 go.mod
drwxr-xr-x 2.8 KB Nov 14 15:21 lexer.go

####  python -m pyls --help (-h): this is a help flag which will show you all help related to all flags. This is in-build function of argparser class
usage: pyls.py [-h] [-l [LIST]] [-A] [-r] [-t] [-filter FILTER_OPTION]
               [-p PATH] [-H [HUMAN]]

options:
  -h, --help                                        show this help message and exit
  -l [LIST], --list [LIST]                          list ot directories with additional information
  -A, --all                                         list all the files and directories (including files starting with .)
  -r, --reverse                                     Reverse list of directories with additional information
  -t, --time_modify                                 Show directories on time modified filter but in reversed order
  -filter FILTER_OPTION, --filter FILTER_OPTION     filter the output on the basis of (file or dir)
  -p PATH, --path PATH                              Handle Paths - it gives detail info about subfiles if filter-option is dir and file itself of the filter-option is file
  -H [HUMAN], --human [HUMAN]                       Human readable format for Size parameter of the file or dir provided by user


## Functions
#### if __name__ == "__main__":  entry point of a program

#### main_function(): This function is for adding new command arguments to argparser class. 
This checks which all flags are set to true and calls decision_function() or top_directory() accordingly

#### decision_function(): This is a decision function where it decides which function to call depending on the filter used by user

#### top_directory(): This function will print all top level directory excluding '.gitignore'.

#### detail_directoryinfo(): This function will display all the top direcotries with additional information.

#### detail_directory_reverseinfo(): This function will display all the top direcotries with additional information in reverse order.

#### sort_on_time_modified(): This function will sort the files/directories on time_modify attribute.

#### search_on_filter_wth_args(): This function will filter the files or directory on the name provided by user along with -r and -t flag.

#### handle_path(): This function will handle path and print the file/dir (pass by user) and print it's subdirs or dir itself.

#### human_readable_size(): This function will print the 'size' parameter in human-readable format of a file or dir provided by the user.

#### format_time(): This function will convert date time in human-readable format and return it.

#### print_dict_info(): This function is to format the output in a desire way.

#### format_size(): This function converts file size from bytes to a human-readable format.


## Test Functions -Pytes: There is s seperate folder "Test" for Unit testing which has few file to test the code

### Test Functions: 
#### test_all_directory.py
#### test_format_size.py
#### test_format_time.py
#### test_handle_path.py
#### test_main_function.py
#### test_print_dict_info.py
#### test_search_on_filter_wth_args.py
#### test_top_directory.py
