#!/usr/bin/env python
'''
Create a dictionary representing a network device. The dictionary should have
key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password'
fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the
'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary
should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value
pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the
dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the
dictionary keys and values.
'''

net_device = {'ip_addr': '1.1.1.1', 'vendor': 'cisco', 'username': 'admin',
'password': 'pa55word'}

print(net_device['ip_addr'])

if net_device['vendor'] is 'cisco':
	net_device['platform'] = 'ios'
elif net_device ['vendor'] is 'juniper':
	net_device['platform'] = 'junos'

bgp_fields = {'bgp_as': '65001', 'peer_as': '65010', 'peer_ip': '2.2.2.2'}

net_device.update(bgp_fields)

for v in net_device.values():
	print(v)

for k, v in net_device.items():
	print(k)
	print(v)
	print('-' * 30)


