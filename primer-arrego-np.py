"""

universad autonoma de zacatecas 
programa que crea una matriz y la imprime usando numpy
12/03/2021
@author: jesus eliseo salas aguiano 

"""
import numpy as np 

#se declaran las variable a usar 
arreglo = np.array([])
filas = int
columnas = int
i=0
j=0

#se pregunta y guarda el tamañano de la matriz a imprimir 
print("bienvenido a este programa que le ayudara a crear una matriz ")
print ("¿cuántas filas va tener la matriz?")
filas = int (input())
print ("¿cuántas columnas va tener la matriz?")
columnas = int (input())  

print ("ingrese los valores uno por uno de izquierda a derecha ")
#este ciclo crea un arreglo con todos los valores que quiere el usario
for i in range( filas ):
    for j in range(columnas):
        arreglo = np.append(arreglo,[[int(input("ingrese el valor: "))]])
        j=j+1
    i=i+1

#este comando "reshape" cambia las dimensiones del arreglo a las que usuario pidio
arreglo = arreglo.reshape(filas,columnas)

print("su arreglo es:")
print (arreglo)
    
