#!/usr/bin/env python
'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output
obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS
number.

From the last line use the string .split() method to obtain the BGP peer IP
address.

Print both local AS number and the BGP peer IP address to the screen.
'''

with open("show_ip_bgp_summ.txt") as f:
	show_bgp = f.readlines()

local_as = show_bgp[0].split()
local_as = local_as[7]

peer_address = show_bgp[3].split()
peer_address = peer_address[0]

print("Local AS: " + local_as + "\nPeer Address: " + peer_address)
