import numpy as np

#Clase para la obtencion de vectores y condiciones necesarias para la implementaciond de 
#el algoritmo de ruta DFS. Los vectores se implementan de la sigujiente manera:
#Vector n(i,j) vector de posibles posiciones (Se ignoran valores con -1)

class DFS:
        matriz = 0
        n = [[0,0]]
        columns = 0
        rows = 0
        

        def __init__(self,matriz,colums,rows):
            self.matriz = matriz
            self.columns = colums
            self.rows = rows
        
        def getVectorN(self):
            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.matriz[i,j] != -1):
                        self.n.insert(-1,[i,j])
            
            print(self.n)
            self.n.remove([0,0])
            print(self.n)
