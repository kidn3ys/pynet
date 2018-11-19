#!/usr/bin/env python

ip_addr = input ("Enter an IP Address: ")
octets = ip_addr.split('.')

print("{:^15}{:^15}{:^15}{:^15}".format("Octet1","Octet2","Octet3","Octet4"))
print("-"*80)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0],10)),bin(int(octets[1],10)),bin(int(octets[2],10)),bin(int(octets[3],10))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0],10)),hex(int(octets[1],10)),hex(int(octets[2],10)),hex(int(octets[3],10))))
print("-"*80)
