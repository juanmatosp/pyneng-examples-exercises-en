#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.



IPs_ingresada = input("Favor introducir la IP: ").split("/")
mask = IPs_ingresada[-1]
IPs = IPs_ingresada[0]
IPs = str(IPs).replace("'","").replace("[", "").replace("]", "")
IPs = list(IPs.split("."))
#print(IPs[0])

#print(IPs, mask)

output = """
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b} {1:08b} {2:08b} {3:08b} """

print(output.format(int(IPs[0]), int(IPs[1]), int(IPs[2]), int(IPs[3])))

print('\n', output.format(int(mask[0])))

mask = IPs.split("/")
mask = mask[-1]
print(type(IPs), IPs, mask)
"""