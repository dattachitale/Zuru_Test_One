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


# Declared "format_time","print_dict_info" and "format_size" functions at global level as we need to call them multiple times
def format_time(time_modified):
    """
    This function will convert date time in human-readable format and return it.

    Args:
    - time_modified: The varibale to be converted to human-readable format.

    Returns:
    - string: representing the time in the specified format.
    """
    return time.strftime('%b %d %H:%M', time.localtime(time_modified))


def print_dict_info(file_info):
    """
    This function is to format the output in a desire way.

    Args:
    - file_info: Dictionary values to format in specified ways.

    Returns:
     None
    """
    permissions = file_info['permissions']
    size = file_info['size']
    time_modified = format_time(file_info['time_modified'])
    name = file_info['name']
    print(f"{permissions}       {size}      {time_modified}         {name}")


def format_size(size):
    """
    This function converts file size from bytes to a human-readable format.

    Args:
    - size: The size varibale to be converted to human-readable format.

    Returns:
    - float: representing the size in the specified format.
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(suffixes) - 1:
        size /= 1024.0
        index += 1
    return f"{size:.1f} {suffixes[index]}"


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


def detail_directoryinfo():
    """

    This function will display all the top direcotries with additional information.

    Args:
    None

    Returns:
    None
    """
    print("This is detail directory information with additional information \n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)

        def traverse_directory(directory):
            # Traverse directory and print file information
            for item in directory:
                if item['name'] == '.gitignore':
                    continue
                if 'contents' in item:
                    print_dict_info(item)
                else:
                    print_dict_info(item)

        # Traverse directory and print file information
        traverse_directory(parsed_data['contents'])


def detail_directory_reverseinfo():
    """

    This function will display all the top direcotries with additional information in reverse order.

    Args:
    None

    Returns:
    None
    """
    print("This is detail directory information with additional information But in Revers order\n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)

        def traverse_directory(directory):
            directory.reverse()

            # Traverse directory and print file information (by calling print_dict_info function)
            for item in directory:
                if item['name'] == '.gitignore':
                    continue
                if 'contents' in item:
                    print_dict_info(item)
                else:
                    print_dict_info(item)

        # Traverse directory and print file information
        traverse_directory(parsed_data['contents'])


def sort_on_time_modified():
    """

    This function will sort the files/directories on time_modify attribute.

    Args:
    None

    Returns:
    None
    """
    print("This is detail directory information with sort based on time_modified flag in reverse\n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)

    parsed_data['contents'] = sorted(parsed_data['contents'], key=lambda x: x['time_modified'], reverse=True)

    # Print file information in the desired format
    for item in parsed_data['contents']:
        print_dict_info(item)


def search_on_filter_wth_args(filter, time_modify=False, reverse=False):
    """

    This function will filter the files or directory on the name provided by user along with -r and -t flag.

    Args:
    - filter (String): --filter=dir/file where dir or file provided by the user on which filter has to apply.
    - time_modify (bool): -t flag where dir or file content is print based on time modified flag
    - reverse (bool): -r flag where dir or file content is print based on reverse

    Returns:
    None
    """
    print("This is search result of a dir/file on specific filter options - file/dir \n")
    # first open the file in read mode to read and load json data
    with open('structure.json', 'r') as file_data:
        directory = json.load(file_data)

    def print_file_info(file_info, full_path):
        # Print file information in the desired format
        permissions = file_info['permissions']
        size = format_size(file_info['size'])
        time_modified = format_time(file_info['time_modified'])
        print(f"{permissions} {size} {time_modified} {full_path}")

    def search_directory(directory, filter, time_modify=False, reverse=False):
        if time_modify:
            directory['contents'] = sorted(directory['contents'], key=lambda x: x['time_modified'], reverse=reverse)
        for item in directory['contents']:
            if item['name'] != '.gitignore':    # Exclude ".gitignore" from the output
                if filter == 'dir' and item['permissions'].startswith('d'):
                    print_file_info(item, item['name'])
                elif filter == 'file' and not item['permissions'].startswith('d'):
                    print_file_info(item, item['name'])
                elif filter == 'all':
                    print_file_info(item, item['name'])

    # Sort the directory by time modified (an oldest first) and reverse the order
    search_directory(directory, filter, time_modify, reverse)


def handle_path(path):
    """

    This function will handle path and print the file/dir (pass by user) and print it's subdirs or dir itself.

    Args:
    - path: String path variable which is either dir name or full path of a file

    Returns:
    None
    """
    print("This handles a path of a file or directory also \n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)

    def print_file_info(file_info, full_path):
        # Print file information in the desired format
        permissions = file_info['permissions']
        size = file_info['size']
        time_modified = format_time(file_info['time_modified'])
        print(f"{permissions} {size} {time_modified} {full_path}")

    def search_directory(directory, search_query, current_path=''):
        found = False
        # Check if the search query matches any directory name
        for item in directory:
            if item['name'] == search_query:
                found = True
                if 'contents' in item:
                    for sub_item in item['contents']:
                        print_file_info(sub_item, os.path.join(current_path, sub_item['name']))
                break
        # If the search query contains a path, check if it matches any file within a directory
        if '/' in search_query:
            directory_name, file_name = search_query.split('/', 1)
            for item in directory:
                if item['name'] == directory_name and 'contents' in item:
                    for sub_item in item['contents']:
                        if sub_item['name'] == file_name:
                            found = True
                            print_file_info(sub_item, os.path.join(current_path, search_query))
                            break
        # If no matching directory or file found, display an error message
        if not found:
            print(f"error: cannot access '{search_query}': No such file or directory")

    search_query = path

    # Search for the specific file or directory
    search_directory(parsed_data['contents'], search_query)


def human_readable_size(path):
    """

    This function will print the 'size' parameter in human-readable format of a file or dir provided by the user.

    Args:
    - path: String path variable which is either dir name or full path of a file

    Returns:
    None
    """
    print("This is human readable function where Size parameter is human readable \n")
    # first open the file in read mode to read and load json data
    with open("structure.json", 'r') as file_data:
        parsed_data = json.load(file_data)

    def print_file_info(file_info, full_path):
        # Print file information in the desired format
        permissions = file_info['permissions']
        size = format_size(file_info['size'])
        time_modified = format_time(file_info['time_modified'])
        print(f"{permissions} {size} {time_modified} {full_path}")

    def search_directory(directory, search_query, current_path=''):
        found = False

        # Check if the search query matches any directory name
        for item in directory:
            if item['name'] == search_query:
                found = True
                if 'contents' in item:
                    for sub_item in item['contents']:
                        print_file_info(sub_item, os.path.join(current_path, sub_item['name']))
                break

        # If the search query contains a path, check if it matches any file within a directory
        if '/' in search_query:
            directory_name, file_name = search_query.split('/', 1)
            for item in directory:
                if item['name'] == directory_name and 'contents' in item:
                    for sub_item in item['contents']:
                        if sub_item['name'] == file_name:
                            found = True
                            print_file_info(sub_item, os.path.join(current_path, search_query))
                            break

        # If no matching directory or file found, display an error message
        if not found:
            print(f"error: cannot access '{search_query}': No such file or directory")

    # Input search query
    search_query = path

    # Search for the specific file or directory
    search_directory(parsed_data['contents'], search_query)


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




