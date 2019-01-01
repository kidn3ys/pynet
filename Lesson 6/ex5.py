#!/usr/bin/env python
'''
Optional, use send_command() in conjunction with ntc-templates to execute a show
command. Have TextFSM automatically convert this show command output to
structured data.
'''
import textfsm
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
	output = net_conn.send_command(cmd, use_textfsm=True)
	print(output)
	net_conn.disconnect()

