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
        return a
    def definirOrigenFin(self,inicio,fin,matriz):
        inicioVector = inicio.split(",")
        finVector = fin.split(",")
        matriz[int(inicio[0]),int(inicio[2])] = 2
        matriz[int(fin[0]),int(fin[2])] = 3
        return matriz