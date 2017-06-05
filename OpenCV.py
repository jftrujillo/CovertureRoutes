import numpy as np
import cv2 as cv2
from matplotlib import pyplot as plt
import math
from matricesVacias import matricesVacias

GRAY_VALUE_MIN = 60
GRAY_VALUE_MAX = 160


def getGrayIntesistyOfImage(img):
    grayOfImage = img[:,:]
    counter = 0
    grayCounter = 0
    for (x,y),element in np.ndenumerate(grayOfImage):
        grayCounter = grayCounter + element
        counter = counter + 1
    return grayCounter/counter


regions= []
src = 'cdu_geo.tif'
img = cv2.imread(src)
#region = cv2.cvtColor(img[0:600, 0:400],cv2.COLOR_BGR2GRAY)
#print(region.shape[0])
#cv2.imshow('imagen',region)
#cv2.waitKey(0)
#cv2.destroyAllWindows
print("Manejo de imagenes usado openCv")
columnas = int(raw_input('ingrese numero de columnas: '))
sizeOfRegion = img.shape[1]/columnas
print(sizeOfRegion)
filas = math.floor(img.shape[0]/sizeOfRegion)
print(filas)
mv = matricesVacias(int(filas),columnas)
x = mv.matrizBasica()
for i in range(int(filas)):
    for j in range(columnas):
        region = cv2.cvtColor(img[i*sizeOfRegion:(i+1)*sizeOfRegion,j*sizeOfRegion:(j+1)*sizeOfRegion],cv2.COLOR_BGR2GRAY)
        regions.append(region)
        if GRAY_VALUE_MIN < getGrayIntesistyOfImage(region) and GRAY_VALUE_MAX > getGrayIntesistyOfImage(region):
             x[i,j] = 0
        else:
            x[i,j] = -1
print(x)
cv2.imshow('region',cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
cv2.destroyAllWindows


