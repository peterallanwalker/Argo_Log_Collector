# Argo Log Collector

[Download Argo Log Collector V1.1.zip](https://github.com/peterallanwalker/Argo_Log_Collector/archive/refs/heads/V1.1.zip)

## get_logs.py - The main script, copies log files from Argo systems.

A Python3 script, tested on Windows 10 & 11.

Alternatively, get the full `dist\get_logs` folder and use the `get_logs.exe` within to run on Windows without Python 
(same usage/args etc as below, just substitute "python get_logs.py" with "get_logs").

### Dependencies
PuTTy/PSCP - Windows does not have support for SCP by default. PSCP gets installed as part of PuTTy installation 
so get_logs.py will work on Windows machines that have PuTTy installed. Download from https://putty.org/ Alternatively, 
if not wanting to install PuTTy, you should be able to just install pscp.exe on its own (but I've not tested that). 

(Argo section processors do not currently support SFTP, hence need to use SCP.)

This script uses standard Python - no external external modules need installing 
(just need the local files below in the same folder).

Local file imports - cli_utils.py, cli_arg_parser.py, settings.py

Optional - config.json


### Usage: 
get_logs.py can be run with no arguments, with or without a config.json file. 
If no arguments are passed, it will check if a config.json file exists in the same folder and contains a 
default IP address to use. If a default address is not found, the user is prompted to enter one.

pass `-h` or `--help` to get usage info. 

Pass an IP address when running the program to get logs from a specific IP address, 
e.g. `python get_logs.py 192.168.24.101`

Alternatively pass a key to lookup an address from config.json, 
e.g. `python get_logs.py 1` to use the address with the key "1" in config.json.
Note, the keys in config.json for IP addresses are arbitrary, you can change the keys
to be more relatable (and add or remove address entries).

Optionally pass a second argument to save the logs to a specific sub-folder, 
e.g. `python get_logs.py 192.168.24.101 issue-1` will save the logs to a folder named "issue-1", 
creating it if it does not already exist. If no sub-folder name is passed from the CLI the user can add 
one when prompted to confirm the save location.

Preferred and alternative save locations can be specified in config.json. The default config.json file defaults 
to Product Test's "Logs & Attachments" folder on the Calrec network, so e.g. `python get_logs.py 192.168.24.101 CE-1234`
would save to a location with the bug ticket reference of "CE-1234", creating the folder if it does not exist. 
If the preferred save location does not exist or is not accessible (e.g not connected to the network) 
then the alternative save location is checked. If no config.json or valid save location within, it will default to 
saving to the same location as the script (within a sub-folder if specified from CLI a argument or user prompt).

log files are saved within the save location / sub-folder in a folder named with the IP address of the device,
and suffixed with a timestamp of when they were copied. 

Log files to save can be specified in config.json. By default, only the "live" logs are 
saved. pass the argument `"-a"` or `"--all"` to copy the full archive, e.g. `python get_logs.py 192.168.24.101 -a`

The "default" save to location in the supplied config.json is a network location. If you want to save to the "alt"
location pass the argument `"-l"` or `"--local"`. This will speed things up if you are not connected to the network 
location by skipping the connectivity check. You can edit the default save location in config.json to avoid needing this

On completing the log transfer, the save location is copied to the clipboard (so if saving to Calrec network can 
control+v/paste it into a Jira ticket), and will open file explorer at that location if user accepts.

## config.json
An optional configuration file containing IP address/es, locations of "live" and "all" log files, as well as the 
preferred and alternative save locations. Note, the keys for IP addresses are arbitrary, you can change the keys
to be more relatable.

## settings.py
Settings handler, loads config settings from separate JSON file, with user input/prompt & validation

## cli_arg_parser
Setup for Python argparse library to handle CLI arguments

## cli_utils
Some CLI formatting and user input handling

