#!/usr/bin/env python
'''
Create a YAML file that defines a list of interface names. Use the expanded form
of YAML.

Use a Python script to read in this YAML list and print it to the screen.

The output of your Python script should be: 
 
['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6',
'Ethernet7', 'Management1', 'Vlan1']
'''

import yaml
filename = "ex3a.yaml"
with open(filename) as f:
	output = yaml.load(f)

print(output)
