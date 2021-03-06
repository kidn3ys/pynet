#!/usr/bin/env python
'''
Use send_command() to send a show command down the SSH channel. Retrieve the
results and print the results to the screen.
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
	print(net_conn.send_command(cmd))
	net_conn.disconnect()

