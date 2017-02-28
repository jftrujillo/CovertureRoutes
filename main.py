import numpy as np
from matricesVacias import matricesVacias
from Util.graphic import Graphic
from waveFront import WaveFront
from DFS import DFS
from Graphics import Graphics

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
b = x.matrizConObstaculos()
print(a)
inicio = raw_input("Defina la posicion de inicion, separando las posiciones con ',': ")
fin = raw_input("Defina la posicion de fin, separando las posiciones con ',': ")
matrizInicioFin = x.definirOrigenFin(inicio,fin,a)
print(matrizInicioFin)
wf = WaveFront(matrizInicioFin,filas,columnas)
matrizWithWaveFront = wf.aplyWaveFrontToMatrix()
print(matrizWithWaveFront)
df = DFS(matrizWithWaveFront,filas,columnas)
covertura = df.getCoverRouteWitSeed()
print("----------------------------------------")
grap = Graphics(b)
grap.printCovertura(covertura)
grap.counter()
grap.numberOfTwist(covertura)






