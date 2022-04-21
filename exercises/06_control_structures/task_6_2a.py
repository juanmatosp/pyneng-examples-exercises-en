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




resp = True
while resp:
#    try:
    IP_Input = input("Introduca la IP Address: ").split(".")
    newListIP = []

    if len(IP_Input) == 4 and str(IP_Input).isdigit():
        print("test")
        #print(IP_Input)
        for ValidaIP in IP_Input:
            #print(ValidaIP)
            if ValidaIP.isdigit():
                if int(ValidaIP) <= 255:
                    newListIP.append(ValidaIP)
                else:
                    print('Digito mayor a 255: ', ValidaIP)
    #    except():
            else:
                print("Los datos Introducido no son valido ", IP_Input)
                resp = False
        print(newListIP)
    else:
        print("salio falso")