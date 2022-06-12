# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


from sys import prefix


Table_Ospf = {}

output = "\n{:25} {}" * 5
with open("ospf.txt", 'r') as r:
    for line in r:
        newLine = line.replace(",", " ").replace("[", "").replace("]", "")
        newLine = newLine.split()
        #print(newLine)

print(output.format(
            'prefix',newLine[1],
            'AD/Metric',newLine[2],
            'Next-Hop',newLine[3], 
            'Last update',newLine[4], 
            'Outbound Interface',newLine[5]
            )
            )

