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
        for element in a:
            element[0] = -1
        for element in a:
            element[-1] = -1
        a[0] = -1
        a[-1] = -1
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


    def definirOrigenFin(self,inicio,fin,matriz):
        inicioVector = inicio.split(",")
        finVector = fin.split(",")
        matriz[int(inicioVector[0]),int(inicioVector[1])] = 2
        matriz[int(finVector[0]),int(finVector[1])] = 3
        return matriz
    
    def defineOrigin(self,inicio,matriz):
        inicioVector = inicio.split(",")
        matriz[int(inicioVector[0]),int(inicioVector[1])] = 2
        return matriz