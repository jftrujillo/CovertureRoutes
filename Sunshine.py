import numpy as np
import time as time
import copy as copy

class Sunshine:
    up = 0
    left = 1
    down = 2
    rigth = 3
    NO_VISITADO = 0
    VISITADO = 1
    OBSTACULO = -1
    matriz = []
    matrizWaveFrontStart = []
    matrizSunshie = []
    lugaresDisponibles = []
    lugareConPeso = []
    lugaresDisponiblesStart = []
    lugareConPesoStart = []
    
    def __init__(self, matriz):
        self.matriz = matriz
        self.matrizWaveFrontStart = copy.deepcopy(matriz)
        self.setLugaresDisponibles()
        self.setLugaresDisponiblesStart()
        self.lugareConPesoStart = []
        self.matrizSunshie = copy.deepcopy(matriz)
    
    

    def getWaveFrontFromObstacle(self):
        counter = 0
        valorDeComparacion = 0
        while (len(self.lugaresDisponibles) > len(self.lugareConPeso)):
            print(self.matriz)
            time.sleep(0.3)
            for (x,y), element in np.ndenumerate(self.matriz):
                if (counter ==  0):
                    valorDeComparacion = -1
                else:
                    valorDeComparacion = counter
                if (element == valorDeComparacion):
                    self.putWaveFrontInElement(valorDeComparacion,(x,y))
            counter = counter + 1
        print(self.matriz)
        return self.matriz
    
    def getWaveFrontFromInitialPoint(self,(x,y),(i,j)):
        counter = 2
        valorDeComparacion = 2
        self.matrizWaveFrontStart[i,j] = 2
        while (len(self.lugaresDisponiblesStart) > len(self.lugareConPesoStart) + 1):
            print(self.matrizWaveFrontStart)
            time.sleep(0.3)
            for (z,w), element in np.ndenumerate(self.matrizWaveFrontStart):
                if (counter ==  0):
                    valorDeComparacion = -1
                else:
                    valorDeComparacion = counter
                if (element == valorDeComparacion):
                    self.putWaveFrontInElementStart(valorDeComparacion,(z,w))
            counter = counter + 1
        self.matrizWaveFrontStart[x,y] = 1
        print(self.matrizWaveFrontStart)
        return self.matrizWaveFrontStart
    
    
    def getMatrizSunshine(self,incorfomidad):
        for element in self.lugaresDisponiblesStart:
            if(self.matrizWaveFrontStart[element[0],element[1]] == 2):
                self.matrizSunshie[element[0],element[1]] = 2
            elif self.matrizWaveFrontStart[element[0], element[1]] == 1:
                self.matrizSunshie[element[0],element[1]] = 1
            else:
                self.matrizSunshie[element[0],element[1]] = self.matrizWaveFrontStart[element[0],element[1]] + incorfomidad/self.matriz[element[0],element[1]]

        print(self.matrizSunshie)
        return self.matrizSunshie



    
        
    

    def putWaveFrontInElement(self,valorDeComparacion,pos):
        if (valorDeComparacion == -1):
            proximoValor = 1
        else:
            proximoValor = valorDeComparacion + 1
        ##Evaluacion con los vecinos, 8 
        
        try:
            if (self.matriz[pos[0] - 1, pos[1]] == 0 and pos[0] - 1 != -1):
                self.matriz[pos[0] - 1, pos[1]] = proximoValor
                self.lugareConPeso.append((pos[0] - 1, pos[1]))
        except:
            pass
        try:
            if (self.matriz[pos[0] - 1, pos[1] - 1] == 0 and pos[0] - 1 != -1 and pos[1] - 1 != -1):
                self.matriz[pos[0] - 1, pos[1] - 1] = proximoValor 
                self.lugareConPeso.append((pos[0] - 1, pos[1] - 1))
        except:
            pass
        try:
            if (self.matriz[pos[0] , pos[1] -1] == 0 and pos[1] -1 != -1):
                self.matriz[pos[0] , pos[1] -1] = proximoValor 
                self.lugareConPeso.append((pos[0] , pos[1] -1))
        except:
            pass
        try:
            if (self.matriz[pos[0] + 1 , pos[1] -1] == 0 and pos[0] + 1 != -1 and pos[1] -1 != -1):
                self.matriz[pos[0] + 1 , pos[1] -1] = proximoValor 
                self.lugareConPeso.append((pos[0] + 1 , pos[1] -1))
        except:
            pass
        try:
            if (self.matriz[pos[0] + 1 , pos[1]] == 0 and pos[0] + 1 != -1):
                self.matriz[pos[0] + 1 , pos[1]] = proximoValor 
                self.lugareConPeso.append((pos[0] + 1 , pos[1]))
        except:
            pass
        try:
            if (self.matriz[pos[0] + 1 , pos[1] + 1] == 0 and pos[0] + 1 !=  -1 and pos[1] + 1 != -1):
                self.matriz[pos[0] + 1, pos[1] + 1] = proximoValor 
                self.lugareConPeso.append((pos[0] + 1, pos[1] + 1))
        except:
            pass
        try:
            if (self.matriz[pos[0] , pos[1] + 1] == 0):
                self.matriz[pos[0] , pos[1] + 1] = proximoValor 
                self.lugareConPeso.append((pos[0] , pos[1] + 1))
        except:
            pass
        try:
            if (self.matriz[pos[0] - 1 , pos[1] + 1] == 0 and pos[0] - 1 != -1):
                self.matriz[pos[0] - 1 , pos[1] + 1] = proximoValor 
                self.lugareConPeso.append((pos[0] - 1 , pos[1] + 1))
        except:
            pass
        

    def putWaveFrontInElementStart(self,valorDeComparacion,pos):
        if (valorDeComparacion == -1):
            proximoValor = 1
        else:
            proximoValor = valorDeComparacion + 1
        ##Evaluacion con los vecinos, 8 
        
        try:
            if (self.matrizWaveFrontStart[pos[0] - 1, pos[1]] == 0 and pos[0] - 1 != -1):
                self.matrizWaveFrontStart[pos[0] - 1, pos[1]] = proximoValor
                self.lugareConPesoStart.append((pos[0] - 1, pos[1]))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] - 1, pos[1] - 1] == 0 and pos[0] - 1 != -1 and pos[1] - 1 != -1):
                self.matrizWaveFrontStart[pos[0] - 1, pos[1] - 1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] - 1, pos[1] - 1))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] , pos[1] -1] == 0 and pos[1] -1 != -1):
                self.matrizWaveFrontStart[pos[0] , pos[1] -1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] , pos[1] -1))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] + 1 , pos[1] -1] == 0 and pos[0] + 1 != -1 and pos[1] -1 != -1):
                self.matrizWaveFrontStart[pos[0] + 1 , pos[1] -1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] + 1 , pos[1] -1))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] + 1 , pos[1]] == 0 and pos[0] + 1 != -1):
                self.matrizWaveFrontStart[pos[0] + 1 , pos[1]] = proximoValor 
                self.lugareConPesoStart.append((pos[0] + 1 , pos[1]))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] + 1 , pos[1] + 1] == 0 and pos[0] + 1 !=  -1 and pos[1] + 1 != -1):
                self.matrizWaveFrontStart[pos[0] + 1, pos[1] + 1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] + 1, pos[1] + 1))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] , pos[1] + 1] == 0):
                self.matrizWaveFrontStart[pos[0] , pos[1] + 1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] , pos[1] + 1))
        except:
            pass
        try:
            if (self.matrizWaveFrontStart[pos[0] - 1 , pos[1] + 1] == 0 and pos[0] - 1 != -1):
                self.matrizWaveFrontStart[pos[0] - 1 , pos[1] + 1] = proximoValor 
                self.lugareConPesoStart.append((pos[0] - 1 , pos[1] + 1))
        except:
            pass

   
    def setLugaresDisponibles(self):
        for (x,y),element in np.ndenumerate(self.matriz):
            if(element != -1):
                self.lugaresDisponibles.append((x,y))
                
    def setLugaresDisponiblesStart(self):
        self.lugaresDisponiblesStart = []
        for (x,y),element in np.ndenumerate(self.matrizWaveFrontStart):
            if(element != -1):
                self.lugaresDisponiblesStart.append((x,y))

