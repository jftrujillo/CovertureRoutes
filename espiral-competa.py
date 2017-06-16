import numpy as np
import copy
from matricesVacias import matricesVacias
from Graphics import Graphics
from Espiral import Espiral

A = np.matrix([[0,-1],
              [1,0]])
B = np.matrix([[0,1],
              [-1,0]])

visitado = 1
obstaculo = -1
nothing = 0

#camino
visitados = []


print("dimensiones de la matriz")

hm,gm = input()
mapa = np.zeros((hm,gm))
mv = matricesVacias(hm,gm)
a = mv.matrizForSunshine()
b = copy.deepcopy(a)


##mapa = np.array([[0,0,0,0,-1], \
##                 [0,0,0,0,-1], \
##                 [0,0,0,-1,-1], \
##                 [-1,-1,-1,-1,-1] ])

hm,gm = mapa.shape
print(hm,gm)
print(a)
print("posicion Inicial ")
pi_x = int(input())
pi_y = int(input())
espiral = Espiral()
covertura = espiral.getCoverturePath(a,pi_x,pi_y)
graphis = Graphics(b)
graphis.printCovertura(covertura)


##print("anterior")
##ps_x = int(input())
##ps_y = int(input())
