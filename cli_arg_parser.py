#!/usr/bin/env python3
# Peter Walker, January 2023
# ref : https://docs.python.org/3/howto/argparse.html
# ref for optional positional args: https://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments

# Standard Python library imports
import argparse

# Local files
import cli_utils

TITLE = "CLI ARGUMENT PARSER"
VERSION = 0.1
DESCRIPTION = "Configures argparse for get_logs.py"


def configure_argparse():
    parser = argparse.ArgumentParser()
    # Optional but positional arguments
    parser.add_argument("address", nargs='?', help="IP address of the target device", type=str)
    parser.add_argument("folder", nargs='?', help="Folder to save log files to", type=str)
    # Optional named argument, returns a bool (can come before or after the named optional args but not in the middle)
    parser.add_argument("-a", "--all", action="store_true", help="Get full log archive instead of just live")
    parser.add_argument("-l", "--local", action="store_true", help="Use the 'alt' save location of config.json rather "
                                                                   "than the 'default', e.g. default is a network "
                                                                   "location and you are connected but want to save the"
                                                                   " logs locally.")
    return parser


if __name__ == '__main__':

    cli_utils.print_header(TITLE, VERSION, DESCRIPTION)

    arg_parser = configure_argparse()
    args = arg_parser.parse_args()
    print("Unit tests...")
    print("Address:", args.address)
    print("Folder:", args.folder)
    print("Get all?:", args.all)
    print("Save to alt/local?:", args.local)
