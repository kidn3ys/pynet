#!/usr/bin/env python
'''
Use Jinja2 templating to render the following: 
 
vlan 
   name 

Your template should be inside of your Python program for simplicity.

The output from processing your template should be as follows. This should be
printed to stdout. 
 
vlan 400
   name red400

'''

import jinja2

vlan = {
	'id': 400,
	'name': 'red400',
}

vlan_template = '''
vlan {{ id }}
	name {{ name }}
'''

t = jinja2.Template(vlan_template)
print(t.render(vlan))
