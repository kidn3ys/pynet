#!/usr/bin/env python
'''
Expand on the ssh_conn function from exercise1 except add a fourth parameter
'device_type' with a default value of 'cisco_ios'. Print all four of the
function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2
function using the **kwargs technique.
'''

def ssh_conn2(ip_addr, username, password, device_type="cisco_ios"):
	print("-"*80)
	print("{:<20}{:<20}{:<20}{:<20}".format("IP Address", "Username", "Password", "Device Type"))
	print("{:<20}{:<20}{:<20}{:<20}".format(ip_addr, username, password, device_type))
	print("-"*80)

	

ssh_conn2('10.1.1.1', 'admin', 'pass123')
ssh_conn2('10.1.1.1', 'admin', 'pass123', "juniper")

my_dict = {
	"ip_addr": "10.1.1.1",
	"username": "admin",
	"password": "pass123",
	"device_type": "arista"
	}

ssh_conn2(**my_dict)
