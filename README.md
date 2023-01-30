# Argo Log Collector

## get_logs.py - The main script, copies log files from Argo systems.

A Python3 script, tested on Windows 10/11.

### Dependencies
PSCP/PuTTy - Windows does not have support for SCP by default. PSCP gets installed as part of PuTTy installation, so get_logs.py will work on Windows machines that have PuTTy installed. Download from https://putty.org/ Alternatively, if not wanting to install PuTTy, you should be able to just install PSCP on its own (but I've not tested that). 

Python standard library imports - os, sys, subprocess, time.

Local file imports - cli_utils.py, cli_arg_parser.py, settings.py

Optional - config.json

[ ] Todo: consider Python Paramiko & SCP libraries instead of depending on PuTTy, can auto-accept key changes with Paramiko and might be able to auto enter password for scp transfer


### Usage: 
get_logs.py can be run with no arguments, with or without a config.json file in the same folder. If no arguments are passed, it will check if a config.json file exists in the same folder and contains a default IP address to use. If a default address is not found, the user is prompted to enter one.

Pass an IP address when running the program to get logs from a specific IP address, e.g. `python get_logs.py 192.168.24.101`. 

Alternatively pass a key to lookup an address from config.json, e.g. `python get_logs.py default` to use the address with the key "default" in config.json.  

Otionally pass a second argument to save the logs to a specific subfolder. 

If no IP address passed, will look for a default IP address in config.json, and prompt 
for input if no default found.

If passing an IP address or key, can also pass a folder name to save the logs to. 
Logs will be saved to a location specified in config.json, if not valid/available
then default to saving in same location as the script is located in. If a second 
argument is passed after the IP address then that will be used as the sub-folder
within the save location, creating it if it does not already exist.

if program run without arguments will be prompted for info

Pass an IP address or a key 


settings.py
Settings handler, loads config settings from separate JSON file, with user input/prompt & validation

## TODO
[ ] Compile an .exe
[ ] Consider using Python Paramiko & SCP libraries to remove the need to have PuTTy or PSCP installed
