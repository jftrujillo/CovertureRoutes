import numpy as np
from matricesVacias import matricesVacias
from Util.graphic import Graphic

# Se definen las siguientes constantes para el manejo de matrices
#     -9 =  obstaculo.
#     0 = posicion posible de visitar
#     1 = posicion visitada.
#     2 =  origen
#     3 = meta 



graphic = Graphic()
graphic.printMessage()
columnas = int(raw_input('ingrese numero de columnas: '))
filas = int(raw_input("ingerese filas: "))
x = matricesVacias(columnas,filas)
a = x.matrizConObstaculos()
print(a)
inicio = raw_input("Defina la posicion de inicion, separando las posiciones con ',': ")
fin = raw_input("Defina la posicion de fin, separando las posiciones con ',': ")
matrizInicioFin = x.definirOrigenFin(inicio,fin,a)
print(matrizInicioFin)

