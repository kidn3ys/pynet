#!/usr/bin/env python
'''
Find a command on your device that has additional prompting. Use
send_command_timing to send the command down the SSH channel. Capture the output
and handle the additional prompting.
'''

from netmiko import Netmiko
from getpass import getpass

def print_cmd(ip_addr, username, cmd):
	my_device = {
		'host': ip_addr,
		'username': username,
		'password': getpass(),
		'device_type': 'cisco_ios'
	}

	net_conn = Netmiko(**my_device)
	output = net_conn.send_command_timing(cmd)
	if 'Delete' in output:
		output += net_conn.send_command_timing('\n')
	if 'confirm' in output:
		output += net_conn.send_command_timing('\n')
	print(output)
	net_conn.disconnect()

