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




