# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

from ntpath import join


Tipo_Interface = input("Interface tipo(access/trunk): ")
if Tipo_Interface == "access" :
    inter = input("Enter interfaces type and nomber: ")
    vlan = input("Enter Vlan nubmer Access: ")
    access_template = [
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    print('interface {}'.format(inter))
    print("\n".join(access_template).format(vlan))

elif Tipo_Interface == "trunk":
    inter = input("Enter interfaces type and nomber: ")
    vlan = input("Enter Allowed Vlan: ")
    trunk_template = [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}",
    ]
    print('interface {}'.format(inter))
    print("\n".join(trunk_template).format(vlan))

else:
    print("Opcion no valida ")