import numpy as np

class WaveFront:
    matrix = 0
    def __init__(self,matrix):
        self.matrix = matrix
    
    def isMatrixEmpty(self):
        for matrixRow in self.matrix:
            for matrixBox in matrixRow:
                if matrixBox == 0:
                    return True
        
        return False
    
    def aplyWaveFrontToMatrix(self):
        while (self.isMatrixEmpty):
            for matrixRow in self.matrix:
                for matrixBox in matrixRow:
                    print(matrixBox)
   
        print("La Matrix esta llena")




    