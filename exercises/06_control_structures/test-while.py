#!/usr/bin/env python3
# probar el While. 


resp = True
lista_Nombre = []
while resp:
    lista_Nombre.append(input ('Escriba un nombre a la lista: '))
    print(len(lista_Nombre))
    resp_Imp = input("Desea imprimir un numero expecifico introduca el numero:  o ALL para toda la lista: " ).lower()
    if resp_Imp == 'all':
        for recorrelista in lista_Nombre.index():
            print('\n', lista_Nombre[recorrelista])
    if int(resp_Imp):
        print( 'El nombre es: ', lista_Nombre[resp_Imp])
    else:
        print("no es un numero valido")
resp = input("Escriba no o n, para salir : ")
if resp == 'n' or resp == 'no':
    resp = False
