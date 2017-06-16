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


print("imagenes reoferencias con algoritmos de busqueda")

srcImage = 'cdu_geo2.tif'
columnas = int(raw_input("ingrese el numero de columnas "))



matrizVacia = matricesVacias(0,0)
openCvScript = openCvscritps(columnas,srcImage)
matrizFromImage = openCvScript.getMatrizFromImage()
filas = openCvScript.getFilasFromImage()
b = copy.deepcopy(matrizFromImage)

inicio = raw_input("Defina la posicion de inicion, separando las posiciones con ',': ")
fin = raw_input("Defina la posicion de fin, separado las posiciones con ,")
inicio = (int(inicio.split(",")[0]),int(inicio.split(",")[1]))
fin = (int(fin.split(",")[0]),int(fin.split(",")[1]))
print(inicio)
print(fin)
matrizInicio = matrizVacia.defineOrigin(inicio,matrizFromImage)
print(matrizInicio)

stc = STC(matrizInicio)
coverturaStc = stc.getSTCoverture()
gp = Graphics(b)
gp.printCovertura(coverturaStc)
coverturaPixels = openCvScript.getCentralPixel(coverturaStc)
print(coverturaPixels)
np.savetxt("coverturaSTC.txt",coverturaPixels,delimiter=',')
with open("coverturaSTC.txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(coverturaPixels)


matrizFromImageForSunshine = openCvScript.getMatrizFromImage()
g = copy.deepcopy(matrizFromImageForSunshine)
sunshine = Sunshine(matrizFromImageForSunshine)
b = sunshine.getWaveFrontFromObstacle()
c  = sunshine.getWaveFrontFromInitialPoint(inicio,fin)
d = sunshine.getMatrizSunshine(4)
dfs8 = DFS8(d,columnas,filas)
coverturaSunshine = dfs8.getCoverRouteWitSeed()
print(coverturaSunshine)
graphicsSunshine = Graphics(g)
graphicsSunshine.printCovertura(coverturaSunshine)
coverturaPixelsSunshine = openCvScript.getCentralPixel(coverturaSunshine)
print(coverturaPixelsSunshine)
np.savetxt("coverturaSunshine.txt",coverturaPixelsSunshine,delimiter=',')
with open("coverturaSunshine.txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(coverturaPixelsSunshine)

matrizFromImageForDfs8 = openCvScript.getMatrizFromImage()
g = copy.deepcopy(matrizFromImageForDfs8)
sunshineDfs8 = Sunshine(matrizFromImageForDfs8)
b = sunshineDfs8.getWaveFrontFromInitialPoint(inicio,fin)
dfs8 = DFS8(b,columnas,filas)
coverturaDfs8 = dfs8.getCoverRouteWitSeed()
graphicsDfs8 = Graphics(g)
graphicsDfs8.printCovertura(coverturaDfs8)
coverturaPixelsDfs8 = openCvScript.getCentralPixel(coverturaDfs8)
print(coverturaPixelsDfs8)
np.savetxt("coverturaDfs8.txt",coverturaPixelsDfs8,delimiter=',')
with open("coverturaDfs8.txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(coverturaPixelsDfs8)


matrizFromImageForDfs = openCvScript.getMatrizFromImage()
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
graphicsDFS = Graphics(g)
graphicsDFS.printCovertura(coverturaDFS)
coverturaPixelsDFS = openCvScript.getCentralPixel(coverturaDFS)
np.savetxt("coverturaDFS.txt",coverturaPixelsDFS,delimiter=',')
with open("coverturaDFS.txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(coverturaPixelsDFS)

matrizFromImageForEspiral = openCvScript.getMatrizFromImage()
g = copy.deepcopy(matrizFromImageForEspiral)
espiral = Espiral()
covertura = espiral.getCoverturePath(matrizFromImageForEspiral,inicio[0],inicio[1])
graphicsCovertura = Graphics(g)
graphicsCovertura.printCovertura(covertura)
np.savetx("coverturaEspiral.txt",covertura,delimiter = ",")
with open("coverturaEspira.,txt","wb") as f:
        writer = csv.writer(f)
        writer.writerows(covertura













