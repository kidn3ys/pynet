#!/usr/bin/env python
'''
 Import the 'datetime' library. Print out the module that is being imported by
datetime (the __file__ attribute)

Import the Python ipaddress library. Print out the module that is being imported
by ipaddress (the __file__ attribute). If you are using Python 2.7, you will
need to pip install the ipaddress library.

Import sys and use pprint to pprint sys.path
'''
import sys
import datetime
import ipaddress
from pprint import pprint

print(datetime.__file__)
print(ipaddress.__file__)

pprint(sys.path)
