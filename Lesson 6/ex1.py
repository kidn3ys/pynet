#!/usr/bin/env python
'''
Using Netmiko, establish a connection to a network device and print out the
device's prompt.
'''

from netmiko import Netmiko
from getpass import getpass

def print_prompt(ip_addr, username):
	my_device = {
		'host': ip_addr,
		'username': username,
		'password': getpass(),
		'device_type': 'cisco_ios'
	}

	net_conn = Netmiko(**my_device)
	print(net_conn.find_prompt())
	net_conn.disconnect()

print_prompt('<ip_addr>', '<username>')
