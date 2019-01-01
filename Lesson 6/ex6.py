#!/usr/bin/env python
'''
Use send_command() to send a show command down the SSH channel. Retrieve the
results and print the results to the screen.
'''
import sys
import textfsm
from netmiko import Netmiko
from getpass import getpass


host = sys.argv
host_config = {}
username = input("Enter username: ")
password = getpass()

for ip_index in range(1, len(host)):
	my_device = {
		'host': host[ip_index],
		'username': username,
		'password': password,
		'device_type': 'cisco_ios'
	}
	net_conn = Netmiko(**my_device)
	print(ip_index)
	host_config[host[ip_index]] = net_conn.send_command('show arp')
	net_conn.disconnect()

for arg in range(1, len(host)):
	print(40 * '-')
	print(host[arg])
	print(host_config[host[arg]])
	print(40 * '-')
	
