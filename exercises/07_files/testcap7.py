#!/usr/bin/env python3
#file = open('file_name.txt', 'r')
#print(file.read())
#print(file.readlines())
import readline


suma =0
leerArchivo = open('file_name.txt')

for line in leerArchivo:
    print(line)
    suma += 1
print("numero de lineas", line)
