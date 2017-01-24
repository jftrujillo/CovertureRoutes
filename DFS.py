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
            return self.n
        
        def getVectorA(self,i,j,n):
            a =[[0,0]]
            for element in n:
                if(element == [i + 1,j]):
                    a.insert(-1,[i + 1,j])
                if(element == [i, j + 1]):
                    a.insert(-1,[i, j + 1])
                if (element == [i - 1,j]):
                    a.insert(-1,[i - 1,j])
                if (element == [i, j - 1]):
                    a.insert(-1,[i, j - 1])
            a.remove([0,0])
            print(a)
        

        def findStartAndGoal(self):
            a = [[0,0]]
            for i in range(self.rows):
                for j  in range(self.columns):
                    if self.matriz[i,j] == 2:
                        a.insert(0,[i,j])
                    if self.matriz[i,j] == 3:
                        a.insert(1,[i,j])
            a.remove([0,0])
            print(a)
                        