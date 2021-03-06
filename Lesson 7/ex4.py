#!/usr/bin/env python
'''
Take the YAML file and corresponding data structure that you defined in
exercise3b: 
 
{'interfaces': {
    'Ethernet1': {'mode': 'access', 'vlan': 10},
    'Ethernet2': {'mode': 'access', 'vlan': 20},
    'Ethernet3': {'mode': 'trunk',
                  'native_vlan': 1,
                  'trunk_vlans': 'all'}
    }
}

From this YAML data input source, use Jinja templating to generate the following
configuration output: 
 
 
interface Ethernet1
  switchport mode access
  switchport access vlan 10
interface Ethernet2
  switchport mode access
  switchport access vlan 20
interface Ethernet3
  switchport mode trunk
  switchport trunk native vlan 1
  switchport trunk allowed vlan all

The following should all be variables in your Jinja template (the names may be
different than below, but they should be variabilized and not be hard-coded in
your template). 
 
interface_name
switchport_mode
access_vlan
native_vlan
trunk_vlans

All your Jinja2 variables should be retrieved from your YAML file. 

This exercise might be challenging.
'''
import jinja2
import yaml

filename = "ex3b.yaml"
with open(filename) as int_config:
	interface_config = yaml.load(int_config)

print(interface_config)

template_file = "ex4.j2"
with open(template_file) as int_template:
	interface_template = int_template.read()

t = jinja2.Template(interface_template)
print(t.render(interface_config))
