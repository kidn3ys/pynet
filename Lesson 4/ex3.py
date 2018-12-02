#!/usr/bin/env python
'''
Read in the 'show_version.txt' file. From this file, use regular expressions to
extract the OS version, serial number, and configuration register values.

Your output should look as follows: 
 
OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
'''
import re

with open ("show_version.txt") as f:
	sh_ver = f.read()

match = re.search(r"^Cisco (.*), Version (.*),", sh_ver, flags=re.M)
if match:
	os_version = match.group(2)

match = re.search(r"^Processor board ID (.*)", sh_ver, flags=re.M)
if match:
	ser_num = match.group(1)

match = re.search(r"^Configuration register is (.*)", sh_ver, flags=re.M)
if match:
	config_reg = match.group(1)

print("{:>20}: {:15}".format("OS Version", os_version))
print("{:>20}: {:15}".format("Serial Number", ser_num))
print("{:>20}: {:15}".format("Config Register", config_reg))

