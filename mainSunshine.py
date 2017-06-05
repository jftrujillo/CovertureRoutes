import numpy as np
from matricesVacias import matricesVacias
from Graphics import Graphics
from Sunshine import Sunshine
import time as time
from DFS8 import DFS8
from Graphics import Graphics
import copy as copy

print('Script de implementacion de Sunshine 1.0')
columnas = int(raw_input('ingrese el numero de columnas: '))
filas = int(raw_input('ingrese el numero de filas: '))
matrisVacia = matricesVacias(filas,columnas)
a = matrisVacia.matrizForSunshine()
g = copy.deepcopy(a)
print(a)
sunshie = Sunshine(a)
b = sunshie.getWaveFrontFromObstacle()
c  = sunshie.getWaveFrontFromInitialPoint((0,3),(0,0))
d = sunshie.getMatrizSunshine(4)
dfs8 = DFS8(d,columnas,filas)
covertura = dfs8.getCoverRouteWitSeed()
print(covertura)

graphics = Graphics(g)
graphics.printCovertura(covertura)
graphics.numberOfTwist(covertura)
graphics.counter(covertura)



