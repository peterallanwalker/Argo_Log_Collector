# Argo Log Collector

get_logs.py

Gets log files from Argo surface section processors

Usage: 

Pass an IP address when running the program to get logs from  specific IP address, 
e.g. `python get_logs.py 192.168.24.101` to get the logs from a section processor on 
that address.

Or pass a key to lookup an address from config.json, e.g. `python get_logs.py 1` to get 
logs from section 1 if config.json provides an IP address with a key of "1"

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
