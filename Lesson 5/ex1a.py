#!/usr/bin/env python
'''
Create an ssh_conn function. This function should have three parameters:
ip_addr, username, and password. The function should print out each of these
three variables and clearly indicate which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
'''

def ssh_conn(ip_addr, username, password):
	print("-"*80)
	print("{:<20}{:<20}{:<20}".format("IP Address", "Username", "Password"))
	print("{:<20}{:<20}{:<20}".format(ip_addr, username, password))
	print("-"*80)

	

ssh_conn('10.1.1.1', 'admin', 'pass123')
ssh_conn(ip_addr = '10.1.1.1', username = 'admin', password = 'pass123')
ssh_conn('10.1.1.1', password = 'pass123', username = 'admin')

