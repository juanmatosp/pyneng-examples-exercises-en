# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

    #    try:
IP_Input = input("Introduca la IP Address: ").split(".")
# newListIP = []
IP_Correct = True

if len(IP_Input) != 4:
    IP_Correct = False
else:
    for ValidaIP in IP_Input:
        if not (ValidaIP.isdigit() and int(ValidaIP) in range(256)):
            IP_Correct = False
            break
    if not IP_Correct:
        print("Invalida IP Adrees")
    else:
        if IP_Input == '255.255.255.255':
            print("Local Broadcast")
        elif IP_Input == "0.0.0.0":
            print("unassigned")
        elif 1 <= int(IP_Input[0]) <= 223:
            print("unicast")
        elif 224 <= (IP_Input[0]) <= 239:
            print("Multicast")