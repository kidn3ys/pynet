#!/usr/bin/env python

#Create a list of five IP addresses.
#
#Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.
#
#Use list concatenation to add two more IP addresses to the end of the list.
#
#Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.
#
#Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
#
#Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

ip_addr = ['192.168.1.1', '192.168.2.1', '192.168.3.1', '192.168.4.1', '192.168.5.1']
ip_addr.append('192.168.6.1')
ip_addr.extend(['192.168.7.1', '192.168.8.1'])
ip_addr = ip_addr + ['192.168.9.1', '192.168.10.1']

print(ip_addr)
print(ip_addr[0])
print(ip_addr[-1])
ip_addr.pop()
ip_addr.pop(0)
ip_addr[0] = '2.2.2.2'
print(ip_addr[0])
