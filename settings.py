#!/usr/bin/env python3
# Peter Walker, January 2023

# Python standard library imports
import os
import json

# Local files
import cli_utils

TITLE = "Settings"
DESCRIPTION = "Settings handler for get_logs.py"
VERSION = 0.2


def validate_ip_address(address):
    """
    Checks if a string is a valid IPv4 address
    :param address: string
    :return: True if valid IPv4 address, else False
    """
    if not address or type(address) != str:
        return False

    address = address.split(".")
    if len(address) != 4:
        return False

    for octet in address:
        try:
            octet = int(octet)
        except ValueError:
            return False

        if octet not in range(256):
            return False

    return True


def ask_ip_address(device):
    """
    Asks user to input an IP address
    Checks input is a valid IP address, keeps asking until it is or user quits or enters blank
    :return: string - user inputted IP address, or None.
    """
    ip_address = input("Enter {} IP address: ".format(device))
    if validate_ip_address(ip_address):
        return ip_address

    while True:
        ip_address = input(f'{ip_address} is not valid. Enter {device} IP address or "quit": ')
        if ip_address.lower() in ("", "q", "quit"):
            return None
        if validate_ip_address(ip_address):
            return ip_address


def load_settings(config_file):
    """
    Check if configuration file exists
    :return: Dict of settings (empty if settings file cannot be found or parsed)
    """
    try:
        with open(config_file, "r") as config:
            return json.load(config)

    except FileNotFoundError:
        print(f'INFO - {config_file} file not found.')
        return {}

    except json.decoder.JSONDecodeError as e:
        print(f'INFO - {config_file} is invalid: {e}')
        return {}


if __name__ == '__main__':
    CONFIG_FILE = "config.json"
    cli_utils.print_header(TITLE, VERSION, DESCRIPTION)

    print("Tests...")

    print(f'{ask_ip_address("a valid")}')

    settings = load_settings(CONFIG_FILE)

    if settings:
        print("Settings:")
        for setting in settings:
            print(setting, ":", settings[setting])

    else:
        print("No Settings")

    print("Done")
