#!/usr/bin/env python3
# Peter Walker, January 2023

TITLE = 'CLI Utils'
DESCRIPTION = 'TUI formatting & simple user input handling'
VERSION = 0.1

PADDING = 1  # spaces/indent for heading


def print_header(title, version=None, description=""):
    """
    Print a formatted heading
    :param title: string, generally program name
    :param version: string, int or float. Optional, will be appended to title prefixed with " v"
    :param description: string, optional, generally a brief description of the program
    :return: none
    """
    if version:
        version = " v" + str(version)

    heading = f' -- {title} {version} -- '

    if description:
        description = f' {description} '

    width = max(len(heading), len(description))

    # Print formatted heading
    print(width * '#')
    print(heading)
    if description:
        print(description)
    print(width * '-')


def user_confirm(prompt, enter=True):
    """
    Prompt user to confirm an action
    :param prompt: string, text to question/prompt the user for confirmation
    :param enter: bool, if True user can simply press enter as affirmative/confirmation
    :return: bool, True if user provide affirmative, False otherwise
    """
    response = input(f'{prompt} (y/n)?: ')
    if response.lower().strip() in ("y", "yes") or (response == "" and enter):
        return True
    return False


if __name__ == '__main__':
    print_header(TITLE, VERSION, DESCRIPTION)
    print("Unit tests...")

    print("Done")

