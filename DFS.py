import numpy as np


class DFS:
        """
        #Clase para la obtencion de vectores y condiciones necesarias para la implementaciond de 
        #el algoritmo de ruta DFS. Los vectores se implementan de la sigujiente manera:
        #Vector n(i,j) vector de posibles posiciones (Se ignoran valores con -1)
        #VectorA a(i,j) vector de adyancencia, posibles vecinos que se pueden ocupar, los visitados no cuadran
        #VectorV v(i,j) vector de posiciones visitadas. Cuando posiciones visitadas =  vector n se recorrio toda la matriz
        #VectorP p(i,j) vector padre. Vector que guarda las ultimas pociciones visitadas, se usa apra recorrer a la 
        #inversar la matriz en caso de querer buscar una semilla
        #Vector semilla s(i,j) cuando |a(i,j)|>1 quiere decir que es un punto de desicion, es decir una rama de el arbol de expansion
        #VectorR ruta(i,j) guarda toda la ruta. Este es el resultado es decir la ruta.
        Se recorre en contra de las manecillas del reloj.
        """
        matriz = 0
        n = [[0,0]]
        v = [[0,0]]
        s = [[0,0]]
        columns = 0
        rows = 0

        

        def __init__(self,matriz,colums,rows):
            self.matriz = matriz
            self.columns = colums
            self.rows = rows
        
        
        def getVectorN(self):
            """
            Obtiene el vector N: El vector N son todas las posiciones que puede ocupar el robot.
            Solo se llama una sola vez 
            """


            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.matriz[i,j] != -1):
                        self.n.insert(-1,[i,j])
            self.n.remove([0,0])
            
        
        def getVectorA(self,i,j,n):
            """
            Obtiene el vector A: El vector A se denomina vector Adyacencia, es decir, las posiciones a las cuales
            se puede mover el robot. Aqui se tiene en cuenta el vector de lugares ya visitados.
            @param i: Posicion i donde se desea obtener el vector adyacencia.
            @param j: Posicion j donde se desea obtener el vector adyacencia
            @return a: Vector adyecencia.
            """
            a =[[0,0]]
            for element in n:
                if(element == [i,j - 1]):
                    a.insert(-1,[i ,j - 1])
                if(element == [i - 1, j]):
                    a.insert(-1,[i -1, j])
                if (element == [i , j + 1]):
                    a.insert(-1,[i,j + 1])
                if (element == [i +1, j]):
                    a.insert(-1,[i +1 ,j])            
            a.remove([0,0])
            for visited in self.v:
                try:
                    a.remove(visited)
                except:
                    pass
            maximunValue = 0
            countOfSeed = 0
            for element in a:
                if self.matriz[element[0]][element[1]] > maximunValue:
                    maximunValue = self.matriz[element[0]][element[1]]
                    countOfSeed = 1
                elif self.matriz[element[0]][element[1]] == maximunValue:
                    countOfSeed = countOfSeed + 1
            
            removeElement = [[0,0]]
            for elementA in a:
                if self.matriz[elementA[0]][elementA[1]] < maximunValue:
                    removeElement.insert(-1,elementA)
            removeElement.remove([0,0])
            for element in removeElement:
                a.remove(element)                    
            return a

        
        def addVisitedPosition(self,visited):
            """
            Agrega una nueva posicion al vector de posiciones visitadas. Esto es para evaluar si una posicion ya esta
            visitada antes de llegar. La idea es agregar una posicion visitade en el lugar que se llega para mantener
            el vector de vistas actualizado a cada momento.
            @param visited: Posicion visitada para agregar al vector de lugares visitadas. 
            """
            for element in self.v:
                if (element == visited):
                    return
            self.v.insert(-1,visited)
        
        
        def addNewSeed(self, seed):
            """
            Agrega una nueva semilla. Es decir un lugar donde se ha hecho una desicion
            @param seed: La dupla de valores donde la posicion es una semilla
            """
            self.s.insert(-1,seed)        
        def getGetVectorS(self):
            """
            Retorna el vectot de semillas
            """
            return self.s
        
        def removeSeedInS(self):
            """
            Eliminar la ultima semilla en el vector. Esto se hace a medidac que vamos hacia atras en caso de no tener mas 
            posiciones que vistar.
            """
            del self.s[-1]
        

        

        def findStartAndGoal(self):
            a = [[0,0]]
            for i in range(self.rows):
                for j  in range(self.columns):
                    if self.matriz[i,j] == 2:
                        a.insert(0,[i,j])
                    if self.matriz[i,j] == 3:
                        a.insert(1,[i,j])
            a.remove([0,0])
            return a
        

        def getNextPosition(self,a):
            """
            Esta funcion retorna la siguiente posicion dandole un vector de adyacencia. Esto es para asegurar
            que se cumpla la prioridad anti horaria.
            @param a: Vector adyacencia.
            """
            if len(a) > 1:
                nextPosition = [10000000,10000000]
                for position in a:
                    if position[1] < nextPosition[1]:
                        nextPosition = position
                    elif position[1] == nextPosition[1]:
                        if (position[0] < nextPosition[0]):
                            nextPosition = position
                return nextPosition
            else:
                return a[0]
            
        
        def getCoverRoute(self):
            currentPosition = self.findStartAndGoal()[0]
            self.getVectorN()
            for x in range(15):
                if(len(self.getVectorA(currentPosition[0],currentPosition[1],self.n)) > 1):
                    #Es una semilla
                    self.addNewSeed(currentPosition)
                else:
                    #no es una semilla
                    pass
                vectorA = self.getVectorA(currentPosition[0],currentPosition[1],self.n)
                nextPosition = self.getNextPosition(vectorA)
                self.addVisitedPosition(currentPosition)
                print(nextPosition)
                currentPosition = nextPosition
            
            

 