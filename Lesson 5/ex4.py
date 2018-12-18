#!/usr/bin/env python
'''
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and
pdb.set_trace() statement outside of your function (i.e. where you have your
function calls).

Inside of pdb, experiment with: 
· Listing your code.
· Using 'next' and 'step' to walk through your code. Make sure you understand 
  the difference between next and step.
· Experiment with 'up' and 'down' to move up and down the code stack.
· Use p <variable> to inspect a variable.
· Set a breakpoint and run your code to the breakpoint.
· Use '!command' to change a variable (for example !new_mac = [])

'''
import re

def convert_mac(mac):
	mac = mac.upper()
	if ':' in mac or '-' in mac:
		new_mac = []
		octets = re.split(r"[-:]", mac)
		for octet in octets:
			if len(octet) < 2:
				octet = octet.zfill(2)
			new_mac.append(octet)
	elif '.' in mac:
		new_mac = []
		sections = mac.split('.')
		if len(sections) != 3:
			raise ValueError("Something went wrong")
		for word in sections:
			if len(word)<4:
				word = word.zfill(4)
			new_mac.append(word[:2])
			new_mac.append(word[2:])
	return ":".join(new_mac)

assert "01:23:02:34:04:56" == convert_mac('123.234.456')
assert "AA:BB:CC:DD:EE:FF" == convert_mac('aabb.ccdd.eeff')
assert "0A:0B:0C:0D:0E:0F" == convert_mac('a:b:c:d:e:f')
assert "01:02:0A:0B:03:44" == convert_mac('1:2:a:b:3:44')
assert "0A:0B:0C:0D:0E:0F" == convert_mac('a-b-c-d-e-f')
assert "01:02:0A:0B:03:44" == convert_mac('1-2-a-b-3-44')
