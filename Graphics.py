import numpy as np
import time as time

class Graphics:
    """
    clase para ver el funcionamiento de los algoritmos de cobertura
    """
    matriz = 0
    def __init__(self,matriz):
        self.matriz = matriz
    

    def printCovertura(self,covertura):
        for element in covertura:
            if (not(self.matriz[element[0]][element[1]] == 2 or self.matriz[element[0]][element[1]] == 3)):
                self.matriz[element[0]][element[1]] = self.matriz[element[0]][element[1]] + 1
                print(self.matriz)
                time.sleep(1)
            else:
                pass
    def printCoverturaWithWavefront(self,covertura):
        for element in covertura:
            if (not(self.matriz[element[0]][element[1]] == 2 or self.matriz[element[0]][element[1]] == 3)):
                self.matriz[element[0]][element[1]] = 1
                print(self.matriz)
                time.sleep(1)
            else:
                pass


