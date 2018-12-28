#!/usr/bin/env python
'''
 Use send_config_set() and send_config_from_file() to make configuration
changes. 

The configuration changes should be benign. For example, on Cisco IOS I
typically change the logging buffer size. 

As part of your program verify that the configuration change occurred properly.
For example, use send_command() to execute 'show run' and verify the new
configuration.
'''
import sys
from netmiko import Netmiko
from getpass import getpass

ip_addr = sys.argv[1]
username = sys.argv[2]

my_device = {
	'host': ip_addr,
	'username': username,
	'password': getpass(),
	'device_type': 'cisco_ios'
}

cfg_commands = ['logging buffered 10000', 'no logging console']

net_conn = Netmiko(**my_device)

cfg_cmds_output = net_conn.send_config_set(cfg_commands)

cfg_file_output = net_conn.send_config_from_file('config.txt')
print(cfg_file_output)

sh_run_output = net_conn.send_command('show running-config all | i logging')

if cfg_commands[0] in sh_run_output and cfg_commands[1] in sh_run_output:
	print("Commands committed successfully!")
else:
	print("Commands not committed.")

net_conn.disconnect()
