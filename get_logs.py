#!/usr/bin/env python3
# Peter Walker, Jan 2023

# Python standard library imports
import os
import sys
import subprocess
import time

# Local files
import cli_utils
import cli_arg_parser
import settings


TITLE = "Argo Log Collector"
VERSION = 1.0

USER = 'root'
LIVE_LOG_LOCATION = '/var/lib/calrec/log/live'

#  - External configuration file
CONFIG = 'config.json'


def get_address(cli_args, conf):
    # If no address or key passed from cli, check for a default in the config file
    if not cli_args.address:
        try:
            if settings.validate_ip_address(conf['addresses']['default']):
                return conf['addresses']["default"]
            else:
                print(f'Default address in {CONFIG}: {conf["addresses"]["default"]} is not a valid IPv4 address')
        except KeyError as e:
            print(f'No default address found in {CONFIG}. Key Error: {e}')

        # If no default address in config, get user to input one
        return settings.ask_ip_address("target device")

    # Else user has passed an argument, let's see if it's a valid IP address
    if settings.validate_ip_address(cli_args.address):
        return cli_args.address
    # Else check if they passed a valid key to lookup and address from json config file
    try:
        if settings.validate_ip_address(conf['addresses'][cli_args.address]):
            return conf['addresses'][cli_args.address]
        else:
            print(f'Address key {cli_args.address} in {CONFIG}: '
                  f'{conf["addresses"][cli_args.address]} is not a valid IPv4 address')

    except KeyError as e:
        print(f'{e} is not a valid IPv4 address or key for an address in {CONFIG}')

    # Address/key passed as cli argument cannot be validated so get user input
    return settings.ask_ip_address("target device")


def get_log_location(cli_args, conf):
    if cli_args.all:
        try:
            return conf["logs_to_get"]["all"]
        except KeyError as e:
            print(f'key error in {CONFIG}, cannot find {e}')
    try:
        return conf["logs_to_get"]["live"]
    except KeyError as e:
        print(f'key error in {CONFIG}, cannot find {e}')
    # If cannot parse from settings use default
    return LIVE_LOG_LOCATION


def copy_to_clipboard(txt):
    # This is probably Windows only, could use pyperclip but then relies on installing an external non-standard lib
    cmd = 'echo ' + txt.strip() + ' | clip'
    try:
        subprocess.check_call(cmd, shell=True)
        print("save location path is copied to your clipboard (control+v it into Jira!)")
    except:
        print("failed to copy to clipboard, what OS is this?")


if __name__ == '__main__':
    cli_utils.print_header(TITLE, VERSION)

    # Setup & parse command line arguments
    arg_parser = cli_arg_parser.configure_argparse()
    args = arg_parser.parse_args()

    # Load settings
    config = settings.load_settings(CONFIG)
    save_to = settings.get_save_location(config)

    if save_to == '.':
        save_to = os.getcwd()  # Just so we can inform the user of the full path to the local folder
        
    save_to = os.path.realpath(save_to) # Fix back/forward slashes

    # Get target device's IP address
    address = get_address(args, config)

    log_location = get_log_location(args, config)

    # If user did not pass a folder name as an argument
    if not args.folder:
        args.folder = input(f'Save logs to (enter or add existing or new sub folder): {save_to}\\')

    save_to += "\\" + args.folder

    # - Get user to confirm
    if cli_utils.user_confirm(f'Get logs from: {address}:{log_location} \nSave to: {save_to} '
                              f'\nConfirm '):

        # - If the sub-folder does not exist, create it
        if not os.path.exists(save_to):
            os.makedirs(save_to)

        timestamp = time.strftime('%Y-%m-%d_%H-%M', time.localtime())
        save_as = '"' + os.path.realpath(save_to + "/" + address + "__" + timestamp) + '"'

        scp_command = 'scp -r '  # - Use '-r' "recursive" to be able to transfer folders/contents not just a single file
        scp_command += USER + '@' + address + ":" + log_location + " " + save_as

        try:
            # Send SCP command from windows to copy target folder to local location
            # subprocess.check_output(scp_command, shell=True)  # TODO check the shell=True part needed/purpose
            subprocess.check_output(scp_command)
            # If successful, user may be prompted to accept/trust
            # (if the IP address had a different MAC address last time?),
            # and to enter password... I don't seem to be able to do either automatically using subprocess.check_output
            print('Done.')

        except subprocess.CalledProcessError as e:
            # print(e)  # Not needed for timeout, ssh exception prints error
            # TODO, if scp is using an underlying ssh lib, make sure my ssh module does not create a naming conflict
            sys.exit()

        copy_to_clipboard(save_as)

        if cli_utils.user_confirm("View in explorer? "):
            # - Open file explorer, showing the folder just copied
            subprocess.Popen(f'explorer {save_as}')
    else:
        print("Cancelled transfer")
        sys.exit()

