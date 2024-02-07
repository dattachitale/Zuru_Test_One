# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import argparse

def main(args):
    # Your script logic here
    print(f"Main script logic with arguments: {args}")

def subcommand1(args):
    # Logic for the first subcommand
    print(f"Subcommand 1 logic with arguments: {args}")

def subcommand2(args):
    # Logic for the second subcommand
    print(f"Subcommand 2 logic with arguments: {args}")

if __name__ == "__main__":
    # Main parser
    parser = argparse.ArgumentParser(description="Main script description")

    # Add arguments for the main script
    parser.add_argument("--main_arg", help="Main script argument")

    # Create subparsers
    subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand")

    # Subparser for subcommand1
    parser_sub1 = subparsers.add_parser("subcommand1", help="Subcommand 1 help")
    parser_sub1.add_argument("--sub1_arg", help="Subcommand 1 argument")

    # Subparser for subcommand2
    parser_sub2 = subparsers.add_parser("subcommand2", help="Subcommand 2 help")
    parser_sub2.add_argument("--sub2_arg", help="Subcommand 2 argument")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check which subcommand was selected and call the corresponding function
    if args.subcommand == "subcommand1":
        subcommand1(args)
    elif args.subcommand == "subcommand2":
        subcommand2(args)
    else:
        main(args)


        def main():
            parser = argparse.ArgumentParser(description='Script with module name and arguments')

            # Positional argument for module name
            parser.add_argument('module_name', type=str, help='Name of the module to run')

            # All remaining arguments after the module name
            parser.add_argument('module_arguments', nargs=argparse.REMAINDER, help='Arguments for the module')

            args = parser.parse_args()

            module_name = args.module_name
            module_arguments = args.module_arguments

            print(f"Module Name: {module_name}")
            print(f"Module Arguments: {module_arguments}")

            # Your code to import and run the specified module goes here
            # For example:
            # module = __import__(module_name)
            # module.main(module_arguments)


        if __name__ == '__main__':
            main()













