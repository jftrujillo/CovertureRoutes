import numpy as np


class DFS8:
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
        matriz = []
        n = []
        v = []
        s = []
        columns = 0
        rows = 0

        

        def __init__(self,matriz,colums,rows):
            self.matriz = matriz
            self.columns = colums
            self.rows = rows
            self.n = []
            self.v = []
            self.s = []
        
        
        def getVectorN(self):
            """
            Obtiene el vector N: El vector N son todas las posiciones que puede ocupar el robot.
            Solo se llama una sola vez 
            """


            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.matriz[i,j] != -1):
                        self.n.append([i,j])
        
            
        def isCurrenPositionSeed(self,i,j):
            a =[]
            for element in self.n:
                if(element == [i -1,j]):
                    a.append([i - 1 ,j])
                if(element == [i -1,j - 1]):
                    a.append([i - 1 ,j - 1])
                if(element == [i , j - 1]):
                    a.append([i, j - 1])
                if(element == [i + 1, j - 1]):
                    a.append([i + 1, j - 1])
                if (element == [i + 1 , j]):
                    a.append([i + 1,j])
                if (element == [i + 1 , j + 1]):
                    a.append([i + 1,j + 1])
                if (element == [i, j + 1]):
                    a.append([i,j + 1])            
                if (element == [i - 1, j + 1]):
                    a.append([i - 1,j + 1])            

            for visited in self.v:
                try:
                    a.remove(visited)
                except:
                    pass
            if(len(a)>1):
                return True
            else:
                return  False


        def getVectorA(self,i,j):
            """
            Obtiene el vector A: El vector A se denomina vector Adyacencia, es decir, las posiciones a las cuales
            se puede mover el robot. Aqui se tiene en cuenta el vector de lugares ya visitados.
            @param i: Posicion i donde se desea obtener el vector adyacencia.
            @param j: Posicion j donde se desea obtener el vector adyacencia
            @return a: Vector adyecencia.
            """
            a =[]
            for element in self.n:
                if(element == [i -1,j]):
                    a.append([i - 1 ,j])
                if(element == [i -1,j - 1]):
                    a.append([i - 1 ,j - 1])
                if(element == [i , j - 1]):
                    a.append([i, j - 1])
                if(element == [i + 1, j - 1]):
                    a.append([i + 1, j - 1])
                if (element == [i + 1 , j]):
                    a.append([i + 1,j])
                if (element == [i + 1 , j + 1]):
                    a.append([i + 1,j + 1])
                if (element == [i, j + 1]):
                    a.append([i,j + 1])            
                if (element == [i - 1, j + 1]):
                    a.append([i - 1,j + 1])            
        
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
    
            removeElement = []
            for elementA in a:
                prueba = self.matriz[elementA[0]][elementA[1]]
                if self.matriz[elementA[0]][elementA[1]] < maximunValue:
                    removeElement.append(elementA)
            for element in removeElement:
                a.remove(element)
            try:
                a.remove(self.findStartAndGoal()[1])
            except:
                pass            
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
            self.v.append(visited)
        
        
        def addNewSeed(self, seed):
            """
            Agrega una nueva semilla. Es decir un lugar donde se ha hecho una desicion
            @param seed: La dupla de valores donde la posicion es una semilla
            """
            self.s.append(seed)        
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
            try:
                del self.s[-1]
            except:
                pass
            

        def findStartAndGoal(self):
            a = []
            for i in range(self.rows):
                for j  in range(self.columns):
                    if self.matriz[i,j] == 1:
                        a.insert(0,[i,j])
                    if self.matriz[i,j] == 2:
                        a.insert(1,[i,j])
            return a
        

        def getNextPosition(self,a,currentPosition):
            """
            Esta funcion retorna la siguiente posicion dandole un vector de adyacencia. Esto es para asegurar
            que se cumpla la prioridad anti horaria.
            @param a: Vector adyacencia.
            """
            if len(a) > 1:
                for position in a:
                    if (position[0] == (currentPosition[0] - 1) and position[1] == currentPosition[1]):
                        return position
                for position in a:
                    if (position[0] == (currentPosition[0] - 1) and position[1] == currentPosition[1] - 1):
                        return position
                for position in a:
                    if (position[0] == currentPosition[0] and position[1] == currentPosition[1] - 1):
                        return position
                
                for position in a:
                    if (position[0] == (currentPosition[0] + 1) and position[1] == currentPosition[1] - 1):
                        return position
                for position in a:
                    if (position[0] == currentPosition[0] + 1 and position[1] == currentPosition[1]):
                        return position
                for position in a:
                    if (position[0] == currentPosition[0] + 1 and position[1] == currentPosition[1] + 1):
                        return position
                for position in a:
                    if (position[0] == currentPosition[0] and position[1] == currentPosition[1] + 1):
                        return position
                for position in a:
                    if (position[0] == currentPosition[0] - 1 and position[1] == currentPosition[1] + 1):
                        return position
            else:
                return a[0]
            
        

        def getCoverRouteWitSeed(self):
            currentPosition = self.findStartAndGoal()[0]
            parentVector = []
            covertura =  []
            self.getVectorN()
            while (len(self.v) < (len(self.n) - 1)):
                self.addVisitedPosition(currentPosition)
                parentVector.append(currentPosition)
                if(self.isCurrenPositionSeed(currentPosition[0],currentPosition[1])):
                    #Es una semilla
                    self.addNewSeed(currentPosition)
                    vectorA = self.getVectorA(currentPosition[0],currentPosition[1])
                    nextPosition = self.getNextPosition(vectorA,currentPosition)
                    print(nextPosition)
                    covertura.append(nextPosition)
                    currentPosition = nextPosition                    

                
                else:
                    #no es una semilla
                    if (len(self.getVectorA(currentPosition[0],currentPosition[1])) == 0):
                        try:
                            if not(len(self.v) < (len(self.n) - 1)):
                                break
                            removeElement = []
                            for element in reversed(parentVector):
                                if (not(element == [0,0])):
                                    print(element)
                                    removeElement.append(element)
                                    covertura.append(element)
                                    if element == self.getGetVectorS()[-1]: 
                                        currentPosition = self.getGetVectorS()[-1]
                                        break
                        except:
                            pass
                        self.removeSeedInS()
                        for element in removeElement:
                            parentVector.remove(element)
                    else:
                        vectorA = self.getVectorA(currentPosition[0],currentPosition[1])
                        currentPosition = self.getNextPosition(vectorA,currentPosition)
                        print(currentPosition)
                        covertura.append(currentPosition)
            print(self.findStartAndGoal()[1])
            covertura.append(self.findStartAndGoal()[1])
            print("Ruta encontrada")
            return covertura
