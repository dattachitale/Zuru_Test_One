"""
This module takes a json file (which contains the information of a directory in nested structure) and
prints out its content in the console in the style of ls (linux utility)

This provides various flags and sub flags and on the basis on those flag, you will get the result

following is the detail information about the flags:
usage: pyls.py [-h] [-l [LIST]] [-A] [-r] [-t] [-filter FILTER_OPTION]
               [-p PATH] [-H [HUMAN]]

options:
  -h, --help                                        show this help message and exit.
  -l [LIST], --list [LIST]                          list ot directories with additional information.
  -A, --all                                         list all the files and directories (including files starting with .).
  -r, --reverse                                     Reverse list of directories with additional information.
  -t, --time_modify                                 Show directories on time modified filter but in reversed order.
  -filter FILTER_OPTION, --filter FILTER_OPTION     filter the output on the basis of (file or dir).
  -p PATH, --path PATH                              Handle Paths - it gives a full or relative path if the given file/directory.
  -H [HUMAN], --human [HUMAN]                       Human readable format for Size parameter of the file or dir provided by user.
"""


import json
import argparse
import time
import os


def main_function(list_format=False, all_files=False, reverse=False, time_modify=False, filter=False, human=False):
    """

    This is a main function where it decides which function to call depending on the filter used by user.

    Args:
    - list_format (bool/string): -l flag if provied by user, it will be False by default.
    - all_files (bool): -A flag if provied by user, it will be False by default.
    - reverse (bool): -r flag if provied by user, it will be False by default.
    - time_modify (bool): -t flag if provied by user, it will be False by default.
    - filter (None Type/string): -filter flag if provied by user, it will be False by default.

    Returns:
    None
    """
    if list_format:
        if list_format and time_modify and reverse and filter==None:    # If -l -r -t flags are given by user
            sort_on_time_modified()
        elif list_format and reverse and filter==None:      # If -l -r flags are given by user
            detail_directory_reverseinfo()
        elif list_format and time_modify and isinstance(list_format,str) or reverse:    # If -l -r -t and --filter flags are given by user
            search_on_filter_wth_args(filter, time_modify, reverse)
        elif isinstance(list_format,str):       # If -l and file/dir name are given by user
            handle_path(list_format)
        elif list_format and filter==None and human==None:      # If just -l flag is given by user e.g. pyls -l
            detail_directoryinfo()
        elif list_format and isinstance(human,str):         # If user uses -l with -H command and file/dir name
            print("Please only use -H command (not -l) and file/dir name which will give you size parameter of your file/dir ")
        else:
            # If user misplace or swap the flag just in case this is specially in --filter case
            print("invalid command, or you may have swapped or missed any flag, check the help using -h or --h flag")
    elif all_files:       # If just -A flag is given by user e.g. pyls -A
        all_directory()
    elif isinstance(human,str):       # If -H human-readable flag is given by user with file/dir name e.g. pyls -H parser
        human_readable_size(human)
    else:
        # If user misplace or swap the flag just in case this
        print("invalid command, or you may have swapped or missed any flag, check the help using -h or --h flag")


def top_directory():
    """

    This function will print all top level directory excluding '.gitignore'.

    Args:
    None

    Returns:
    None
    """
    print("This is top directory excluding '.gitignore' \n")
    # First open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)
        for names in parsed_data['contents']:
            if names['name'].startswith("."):
                continue
            print(names['name'], end="\t\t")


def all_directory():
    """

    This function will print all top directory including '.gitignore'.

    Args:
    None

    Returns:
    None
    """
    print("This is top directory including '.gitignore' \n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)
        for names in parsed_data['contents']:
            print(names['name'], end="\t\t")


if __name__ == "__main__":
    # This is a code block that runs when the script is executed as the main program

    # Create an object for argparser
    parser = argparse.ArgumentParser()
    # Add optional arguments
    parser.add_argument('-l', '--list', nargs='?', const=True, help='list ot directories with additional information')
    parser.add_argument('-A', '--all', action='store_true', help='list all the files and directories (including files starting with .)')
    parser.add_argument('-r', '--reverse', action='store_true', help='Reverse list of directories with additional information')
    parser.add_argument('-t', '--time_modify', action='store_true', help='Show directories on time modified filter but in reversed order')
    parser.add_argument('-filter','--filter', metavar='FILTER_OPTION', type=str, choices=['file', 'dir'], help='filter the output on the basis of (file or dir)')
    parser.add_argument('-p', '--path', help='Handle Paths - it gives a full or relative path if the given file/directory')
    parser.add_argument('-H', '--human', nargs='?', const=True, help='Human readable format for Size parameter of the file or dir provided by user')

    # Parse the arguments
    args = parser.parse_args()
    print(args)     # Print args namespace just for debuging and to see which flags have True or False values

    # Check that which flags have provided by the user and according send their values to main_function
    if args.list or args.all or args.reverse or args.time_modify or args.filter  or args.path or args.human:
        main_function(list_format=args.list, all_files=args.all, reverse=args.reverse, time_modify=args.time_modify, filter=args.filter, human=args.human)
    else:
        # If no flags have provided my user means only file name "pyls" so call function which displays top level directory only
        top_directory()




