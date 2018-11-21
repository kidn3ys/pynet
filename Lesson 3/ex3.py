#/usr/bin/env python
'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this
file. Keep reading the lines until you have encountered the remote "System Name"
and remote "Port id". Save these two items into variables and print them to the
screen. You should extract only the system name and port id from the lines (i.e.
your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop
once you have retrieved these two items.
'''

with open("show_lldp_neighbors_detail.txt") as f:
	show_lldp = f.read()

sys_name, port_id = '', ''

for line in show_lldp.splitlines():
	fields = line.split(":")
	# Uncomment line below to validate loop breaks at the appropriate time
	# print(line)
	if "system name" in fields[0].lower():
		sys_name = fields[1].strip()
	if "port id" in fields[0].lower():
		port_id = fields[1].strip()
	
	if sys_name and port_id:
		print(sys_name + " / " + port_id)
		break
		
