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
        self.rows = rows - 1 
        self.columns = columns - 1
    
    def isMatrixEmpty(self):
        for matrixRow in self.matrix:
            for matrixBox in matrixRow:
                if matrixBox == 0:
                    return True
        
        return False
    
    def aplyWaveFrontToMatrix(self):
        #while (self.isMatrixEmpty):
            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.boxHasANeighbour(i,j)):
                        self.counterNeigborgs = self.counterNeigborgs + 1
                print(self.counterNeigborgs)   
        #print("La Matrix esta llena")
    

    def boxHasANeighbour(self,i,j):
        if(i > 0 and i < self.rows and j>0 and j<self.columns):
            if (self.matrix[i - 1,j] > 1):
                return True
            if (self.matrix[i,j +1] > 1):
                return True
            if (self.matrix[i + 1,j] > 1):
                return True
            if (self.matrix[i,j - 1] > 1):
                return True
            return False
        else:
            return False
    
    def isValidBox(self,i,j):
        if (i> 0  and i <self.rows and j>0 and j < self.columns):
            return True
        else:
            return False

    
    def getSmalestNeigbor(self,i,j):
        minimunValue = 10000000
        if (self.matrix[i - 1,j] < minimunValue):
            minimunValue = self.matrix[i - 1,j]
        if (self.matrix[i,j +1] < minimunValue):
            minimunValue = self.matrix[i,j +1]
        if (self.matrix[i + 1,j] < minimunValue):
            return True
        if (self.matrix[i,j - 1] < minimunValue):
            minimunValue = self.matrix[i,j - 1]
        return minimunValue
        





    