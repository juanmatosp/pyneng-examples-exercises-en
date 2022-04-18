# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
from decimal import DivisionByZero


resp = True

while resp:
    try:
        IP_Address = input("introducas la IP address: ")
        listIp = int(IP_Address.split(".")[0])
        print(listIp)

        if IP_Address == '255.255.255.255':
            print("Local Broadcast")
        elif IP_Address == "0.0.0.0":
            print("unassigned")
        elif 1 <= listIp <= 223:
            print("unicast")
        elif 224 <= listIp <= 239:
            print("Multicast")
    except(ValueError, DivisionByZero):
        print("esto no se puede: ")
    finally:
        resp = input("Desea procesar otra ip: ").lower()
        if resp == 'yes' or resp == 'y':
            resp = True
           # print(resp)
        else:
            resp = False
           # print("respuesta de else: ", resp)



"""
#print(listIp[0])
binary1 = ""
#decimalToBinary = 0
for (ConverIP) in listIp[0]:
    decimalToBinary = int(ConverIP)
    #print(decimalToBinary)
    while int(decimalToBinary) >=1:
        NumeroBinario = ((int(decimalToBinary) % 2)) # sacando el dividendo del reto entero.
        decimalToBinary = (int(decimalToBinary) // 2) # sacando el reto entero 
        binary1 += str(NumeroBinario) # sumando los datos que salen de NumeroBinario.
        #print(" el numero Binario: " , NumeroBinario)
       # print(" el numero Decimal: " , decimalToBinary)
#print (decimalToBinary)
print(" el numero Binario: " , binary1)
    #binary1 = ""
    
"""