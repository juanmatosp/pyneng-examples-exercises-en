# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
respboleano = True
while True:
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
                break
            elif IP_Input == "0.0.0.0":
                print("unassigned")
                break
            elif 1 <= int(IP_Input[0]) <= 223:
                print("unicast")
                break
            elif 224 <= (IP_Input[0]) <= 239:
                print("Multicast")
                break
'''            
resp = input("Para salir escribir n o No: ").lower()
if resp == 'n' or resp == 'no':
    respboleano = False
    '''