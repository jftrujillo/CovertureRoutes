import numpy as np


# Siempre damos prioridad en orden de las manecillas del reloj empezando a las 12.
    # En teoria, la primera vez que corra la prueba el contador de vecinos me debe dar
    # un total de 4 por punto, es decir 8.


class WaveFront:
    matrix = 0
    rows = 0
    columns = 0
    counterNeigborgs = 0
    def __init__(self,matrix,rows,columns):
        self.matrix = matrix
        self.rows = rows 
        self.columns = columns 
    
    def isMatrixEmpty(self):
        for matrixRow in self.matrix:
            for matrixBox in matrixRow:
                if matrixBox == 0:
                    return True
        
        return False
    
    def aplyWaveFrontToMatrix(self):
        while (self.isMatrixEmpty()):
            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.boxHasANeighbour(i,j)):
                        self.matrix[i,j] = self.getSmalestNeigbor(i,j) + 1 
                        print(self.matrix)  
        print("La Matrix esta llena")
        return self.matrix
    

    def boxHasANeighbour(self,i,j):
        if(i >= 0 and i <= self.rows + 1 and j>=0 and j<=self.columns - 1   and self.matrix[i,j] != 3 and self.matrix[i,j] != 2  and self.matrix[i,j] != -1):
            try:
                if (self.matrix[i - 1,j] > 1 and self.matrix[i - 1,j] != 2 and self.matrix[i - 1,j] != -1):
                    return True
            except:
                pass
            try:
                if (self.matrix[i,j +1] > 1 and self.matrix[i,j +1] != 2 and self.matrix[i,j +1] != -1):
                    return True
            except:
                pass
            try:
                if (self.matrix[i + 1,j] > 1 and self.matrix[i + 1,j] != 2 and self.matrix[i + 1,j] != -1):
                    return True
            except:
                pass
            try:
                if (self.matrix[i,j - 1] > 1 and self.matrix[i,j - 1] != 2 and self.matrix[i,j - 1] != -1):
                    return True
            except:
                pass
            return False
        else:
            return False
    
    def isValidBox(self,i,j):
        if (i> 0  and i <self.rows and j>0 and j < self.columns):
            return True
        else:
            return False

    
    def getSmalestNeigbor(self,i,j):
        minimunValue = 10000000000
        try:
            if (self.matrix[i - 1,j] < minimunValue and self.matrix[i - 1,j] != 0 and self.matrix[i - 1,j] != 2 and self.matrix[i - 1,j] != -1):
                minimunValue = self.matrix[i - 1,j]
        except:
            pass
        try:
            if (self.matrix[i,j +1] < minimunValue and self.matrix[i,j +1] != 0 and self.matrix[i,j +1] != 2 and self.matrix[i,j +1] != -1):
                minimunValue = self.matrix[i,j +1]
        except:
            pass
        try:
            if (self.matrix[i + 1,j] < minimunValue and self.matrix[i + 1,j] != 0 and self.matrix[i + 1,j] != 2 and self.matrix[i + 1,j] != -1):
                minimunValue = self.matrix[i + 1,j]
        except:
            pass
        try:
            if (self.matrix[i,j - 1] < minimunValue and self.matrix[i,j - 1] != 0 and self.matrix[i,j - 1] != 2 and self.matrix[i,j - 1] != -1):
                minimunValue = self.matrix[i,j - 1]
        except:
            pass
        return minimunValue