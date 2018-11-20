#!/usr/bin/env python

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip().split()
model = show_version[1]
serial = show_version[2]

print('Serial: ' + serial + ' Model: ' + model)
print('cisco' in model.lower())
print('881' in model)
