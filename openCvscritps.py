import numpy as np
import cv2 as cv2
import math
import time
from matricesVacias import matricesVacias


class openCvscritps:
    GRAY_VALUE_MIN = 60
    GRAY_VALUE_MAX = 115
    columnas = 0
    filas = 0
    src = ""
    sizeOfRegion = 0

    def __init__(self,columnas,src):
        self.columnas = columnas
        self.src = src

    def getCentralPixel(self,covertura):
        coverturaCentralPixels = []
        for (x,y) in covertura:
            coverturaCentralPixels.append((x*self.sizeOfRegion + self.sizeOfRegion/2,y*self.sizeOfRegion + self.sizeOfRegion/2))       
        return coverturaCentralPixels

    
    def getGrayIntesistyOfImage(self,img):
        grayOfImage = img[:,:]
        counter = 0
        grayCounter = 0
        for (x,y),element in np.ndenumerate(grayOfImage):
            grayCounter = grayCounter + element
            counter = counter + 1
        return grayCounter/counter

    
    def getMatrizFromImage(self):
        print("Obteniendo matriz de posicion de imagen")
        img = cv2.imread(self.src)
        self.sizeOfRegion = img.shape[1]/self.columnas
        self.filas = int(math.floor(img.shape[0]/self.sizeOfRegion))
        mv = matricesVacias(self.filas,self.columnas)
        matriz = mv.matrizBasica()
        for i in range(self.filas):
            for j in range(self.columnas):
                region = cv2.cvtColor(img[i*self.sizeOfRegion:(i+1)*self.sizeOfRegion,j*self.sizeOfRegion:(j+1)*self.sizeOfRegion],cv2.COLOR_BGR2GRAY)
                if self.GRAY_VALUE_MIN < self.getGrayIntesistyOfImage(region) and self.GRAY_VALUE_MAX > self.getGrayIntesistyOfImage(region):
                    matriz[i,j] = 0
                else:
                    matriz[i,j] = -1
        print(matriz)
        cv2.imshow('region',cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
        cv2.destroyAllWindows
        return matriz
    
    def getFilasFromImage(self):
        return self.filas
                
   
    

    
    
    
