import numpy as np

class matricesVacias:
    columns = 0
    filas = 0
    def __init__(self,columnas,filas):
        self.columns = columnas
        self.filas = filas
    def matrizBasica(self):
        a = np.zeros((self.columns,self.filas))
        return a
    def matrizConObstaculos(self):
        a = np.zeros((self.columns,self.filas))
        a[2,2] = -1    
        a[2,3] = -1
        a[2,4] = -1
        a[3,2] = -1
        a[3,3] = -1
        a[3,4] = -1
        
        a[6,6] = -1 
        a[7,6] = -1 
        a[8,6] = -1 
        a[9,7] = -1
        a[8,7] = -1
        a[8,8] = -1
        a[7,8] = -1
        return a

    def matrizForStc(self):
        a = np.zeros((self.columns,self.filas))
        a[2,2] = -1    
        a[2,3] = -1
        a[6,6] = -1 
        a[7,8] = -1
        return a
    def matrizForSunshine(self):
        a = np.zeros((self.columns,self.filas))
        a[2,2] = -1    
        a[2,3] = -1
        a[2,4] = -1
        a[3,2] = -1
        a[3,3] = -1
        a[3,4] = -1
        
        a[6,6] = -1 
        a[7,6] = -1 
        a[8,6] = -1 
        a[9,7] = -1
        a[8,7] = -1
        a[8,8] = -1
        a[7,8] = -1
        return a


    def definirOrigenFin(self,inicio,fin,matriz):
        matriz[inicio[0],inicio[1]] = 2
        matriz[fin[0],fin[1]] = 3
        return matriz
    
    def defineOrigin(self,inicioVector,matriz):
        matriz[inicioVector[0],inicioVector[1]] = 2
        return matriz
    def defineFin(self,finVector,matriz):
        matriz[finVector[0],finVector[1]] = 3
        return matriz