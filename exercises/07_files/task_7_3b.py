# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
mac_table = []
user_vlan = input("Enter VLAN number: ")

with open('CAM_table.txt', 'r') as r:
    for line in r:
        Line_List = line.split()
        if Line_List and Line_List[0].isdigit() and Line_List[0] == user_vlan:
            vlan, mac, _, interface = Line_List
            mac_table.append([int(vlan), mac, interface])

for vlan, mac, interface in sorted(mac_table):
    print(f"{vlan:<10}{mac:20}{interface}")  