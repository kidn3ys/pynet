#!/usr/bin/env python
'''
Create three separate lists of IP addresses. The first list should be the IP
addresses of the Houston data center routers, and it should have over ten
RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers,
and it should have at least eight RFC1918 IP addresses (including some addresses
that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers,
and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses
should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston
and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three
sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

hou_ips = ['172.16.1.1', '172.16.2.1', '172.16.3.1', '172.16.4.1',
'172.16.5.1', '172.16.6.1', '172.16.2.1', '172.16.3.1', '172.16.10.1',
'172.16.254.1', '172.16.253.1']

atl_ips = ['172.17.1.1', '172.17.2.1', '172.17.3.1', '172.17.4.1',
'172.17.5.1', '172.16.253.1', '172.16.254.1', '172.16.6.1']

chi_ips = ['172.16.254.1', '172.16.6.1', '172.16.253.1', '172.17.1.1',
'172.18.1.1', '172.18.2.1', '172.18.3.1', '172.18.4.1']

hou_ips_set = set(hou_ips)
atl_ips_set = set(atl_ips)
chi_ips_set = set(chi_ips)

print('-' * 30)
print("Duplicate addresses between Houston and Atlanta DCs:")
print(hou_ips_set & atl_ips_set & chi_ips_set)
print("Duplicate addresses between all DCs:")
print(hou_ips_set & atl_ips_set)
print("Addresses unique to Chicago:")
print(chi_ips_set - hou_ips_set - atl_ips_set)
print('-' * 30)
