import numpy as np
from matricesVacias import matricesVacias
from STC import STC


print("Script de implementacion de STC")
columnas = int(raw_input('ingrese numero de columnas: '))
filas = int(raw_input("ingerese filas: "))
matrisVacia = matricesVacias(filas,columnas)
a = matrisVacia.matrizForStc()
print(a)
inicio = raw_input("Defina la posicion de inicion, separando las posiciones con ',': ")
matrizInicio = matrisVacia.defineOrigin(inicio,a)
print(matrizInicio)
stc = STC(matrizInicio)
stc.getSTCoverture()