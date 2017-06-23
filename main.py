from openCvscritps import openCvscritps
from DFS8 import DFS8
from STC import STC
from DFS import DFS
from Sunshine import Sunshine
from matricesVacias import matricesVacias
from Graphics import Graphics
from waveFront import WaveFront
from Espiral import Espiral
import numpy as np
import cv2 as cv2
import math
import copy
import csv

# Se definen las siguientes constantes para el manejo de matrices
#     -9 =  obstaculo.
#     0 = posicion posible de visitar
#     1 = posicion visitada.
#     2 =  origen
#     3 = meta 



print("imagenes reoferencias con algoritmos de busqueda")
srcImage = 'cdu_image.tif'
columnas = int(raw_input("ingrese el numero de columnas "))

matrizVacia = matricesVacias(0,0)
openCvScript = openCvscritps(columnas,srcImage)
matrizFromImage = openCvScript.getMatrizFromImage()
filas = openCvScript.getFilasFromImage()
while True:
        i = raw_input("Entrar nuevo obstaculo, separados por coma: ")
        if not i:
                break
        obstaculo = map(lambda x: int(x),i.split(","))
        matrizFromImage[obstaculo[0]][obstaculo[0]] = -1
        print(obstaculo)
        print(matrizFromImage)

inicio = raw_input("Defina la posicion de inicion, separando las posiciones con ',': ")
fin = raw_input("Defina la posicion de fin, separado las posiciones con ,")
inicio = (int(inicio.split(",")[0]),int(inicio.split(",")[1]))
fin = (int(fin.split(",")[0]),int(fin.split(",")[1]))
print(inicio)
print(fin)

matrizFromImageForDfs = matrizFromImage
g = copy.deepcopy(matrizFromImageForDfs)
matrizVacia = matricesVacias(0,0)
matrizFin = matrizVacia.defineFin(fin,matrizFromImageForDfs)
print(matrizFin)
wf = WaveFront(matrizFin,filas,columnas)
matrizWithWaveFront = wf.aplyWaveFrontToMatrix()
matrizInicioFin = matrizVacia.definirOrigenFin(inicio,fin,matrizWithWaveFront)
print(matrizInicioFin)
df = DFS(matrizInicioFin,columnas,filas)
coverturaDFS = df.getCoverRouteWitSeed()
i = 0
dupe = False
i = 0
dupe = False

while i < len(coverturaDFS)-1:
    if coverturaDFS[i] == coverturaDFS[i+1]:
        del coverturaDFS[i]
        dupe = True
    else:
        i += 1

graphicsDFS = Graphics(g)
graphicsDFS.printCovertura(coverturaDFS)
coverturaPixelsDFS = openCvScript.getCentralPixel(coverturaDFS)
np.savetxt("coverturaDFS.txt",coverturaPixelsDFS,delimiter=',')
with open("coverturaDFS.txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(coverturaPixelsDFS)







