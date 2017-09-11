import numpy as np


class STC:
    matriz4x4 = 0 
    matriz1x1 = 0
    vectorS = []
    vectorN = []
    vectorV = []
    nodes = []
    initial1x1 = 0
    initial4x4 = 0
    up = 0
    left = 1
    down = 2
    rigth = 3
    NOVISTIADO = 0
    PARCIALMENTEVISITADO = 1
    TOTALMENTEVISITADO = 2
    currentPosition = 0
    currentNode = 0
    
    def __init__(self,matriz4x4):
        self.matriz4x4 = matriz4x4
        self.matriz1x1 = self.getMatriz1x1(matriz4x4)
    
    def getSTCoverture(self):
        self.getInitialPosition()
        self.currentPosition = self.initial4x4
        self.currentNode = self.initial1x1
        parentNode = None
        self.setVectorN()
        vectorS = []
        covertura = []
        covertura.append(self.currentPosition)

        while (len(self.vectorV) < (len(self.vectorN))):
            positionNode = self.getNewNodeArround(self.currentPosition,self.currentNode,parentNode)
            print(self.matriz4x4)
            while positionNode == None:
                nextPosition = self.searchForNextBorder(self.currentPosition,self.currentNode,parentNode)
                if nextPosition != None:
                    print(nextPosition)
                    print(self.matriz4x4)
                    self.vectorV.append(nextPosition)
                    covertura.append(nextPosition)
                    self.currentPosition = nextPosition
                    self.matriz4x4[self.currentPosition[0],self.currentPosition[1]] = 1
                    positionNode = self.getNewNodeArround(self.currentPosition,self.currentNode,parentNode)
                else:
                    positionNode = self.getNewNodeArroundPartialVisited(self.currentPosition,self.currentNode,vectorS)
                    self.checkStateOfNode(self.currentNode)
                    vectorS.append(self.currentNode)
                    print(self.matriz4x4)
                    if (self.areAllNodesVisited()):
                        print('termino')
                        return covertura

            
            self.currentPosition = positionNode[0]
            self.matriz4x4[self.currentPosition[0],self.currentPosition[1]] = 1
            parentNode = self.currentNode
            self.checkStateOfNode(self.currentNode)
            vectorS.append(self.currentNode)
            self.currentNode = positionNode[1]
            print(self.currentPosition)
            print(self.matriz4x4)
            covertura.append(self.currentPosition)
            self.vectorV.append(self.currentPosition)
        return covertura
                
    

    def areAllNodesVisited(self):
        for row in self.matriz1x1:
            for element in row:
                if element == 0 or element == 1:
                    return False
        return True
    
    def getNewNodeArround(self,currentPosition4x4,currentNode,parentNode):
        posibleNextPosition = []
        posibleNextPosition.append((currentPosition4x4[0] - 1,currentPosition4x4[1]))
        posibleNextPosition.append((currentPosition4x4[0],currentPosition4x4[1] - 1))
        posibleNextPosition.append((currentPosition4x4[0] + 1,currentPosition4x4[1]))
        posibleNextPosition.append((currentPosition4x4[0],currentPosition4x4[1] + 1))
        for position in posibleNextPosition:
            for (node,cells) in self.nodes:
                if(position in cells and node != currentNode and self.matriz1x1[node[0],node[1]] == 0):
                    return [position,node]
        return None
    
    def getNewNodeArroundPartialVisited(self,currentPosition4x4,currentNode,vectorS):
        posibleNextPosition = []
        posibleNextPosition.append((currentPosition4x4[0] - 1,currentPosition4x4[1]))
        posibleNextPosition.append((currentPosition4x4[0],currentPosition4x4[1] - 1))
        posibleNextPosition.append((currentPosition4x4[0] + 1,currentPosition4x4[1]))
        posibleNextPosition.append((currentPosition4x4[0],currentPosition4x4[1] + 1))
        for element in reversed(vectorS):
            for position in posibleNextPosition:
                for (node,cells) in self.nodes:
                    if(position in cells and node != currentNode and self.matriz1x1[node[0],node[1]] == 1 and node == element):
                        return [position,node]
        return None


    def searchForNextBorder(self,currentPosition,currentNode,parentNode):
        posibleFuturePosition = []
        if (parentNode == None):
            #primera interaccino, no existe un padre#
            posibleFuturePosition.append((currentPosition[0],currentPosition[1] - 1))
            posibleFuturePosition.append((currentPosition[0] + 1,currentPosition[1]))
            posibleFuturePosition.append((currentPosition[0],currentPosition[1] + 1))
            posibleFuturePosition.append((currentPosition[0] - 1,currentPosition[1]))
        else:
            row = currentNode[0] - parentNode [0]
            column = currentNode[1] - parentNode [1]
            if(row > 0 and column == 0):
                posibleFuturePosition.append((currentPosition[0] + 1,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] + 1))
                posibleFuturePosition.append((currentPosition[0] - 1,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0],currentPosition[1] - 1))

            elif (row == 0 and column > 0):
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] + 1))
                posibleFuturePosition.append((currentPosition[0] - 1,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] - 1))
                posibleFuturePosition.append((currentPosition[0] + 1,currentPosition[1]))


            elif (row < 0 and column == 0):
                posibleFuturePosition.append((currentPosition[0] - 1,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] - 1))
                posibleFuturePosition.append((currentPosition[0] + 1 ,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] + 1))

            elif (row == 0 and column < 0):
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] - 1))
                posibleFuturePosition.append((currentPosition[0] + 1 ,currentPosition[1]))
                posibleFuturePosition.append((currentPosition[0] ,currentPosition[1] + 1))
                posibleFuturePosition.append((currentPosition[0] - 1,currentPosition[1]))
        for (node,cells) in self.nodes:
            if node == currentNode:
                for element in posibleFuturePosition:
                    if (element in cells and self.matriz4x4[element[0],element[1]] == 0):
                        return element
        return None



    
    def  checkStateOfNode(self,checkedNode):
        counter = 0
        for (node,cells) in self.nodes:
             if (node == checkedNode):
                for cell in cells:
                    if self.matriz4x4[cell[0],cell[1]] == 1 or self.matriz4x4[cell[0],cell[1]] == 2:
                        counter = counter + 1
                if counter == 0:
                    self.matriz1x1[node[0],node[1]] = 0
                elif counter > 0 and counter < 4:
                    self.matriz1x1[node[0],node[1]] = 1
                elif counter == 4:
                    self.matriz1x1[node[0],node[1]] = 2
                break


    
    def nextPosition1x1(self,currentPosition,posibleCells):
        neigborsOfCurrentPosition = []
        neigborsOfCurrentPosition.append((currentPosition[0] - 1,currentPosition[1]))
        neigborsOfCurrentPosition.append((currentPosition[0],currentPosition[1] - 1))
        neigborsOfCurrentPosition.append((currentPosition[0] + 1,currentPosition[1]))
        neigborsOfCurrentPosition.append((currentPosition[0],currentPosition[1] + 1))
        for posibleNeigbor in neigborsOfCurrentPosition:
            if (posibleNeigbor in posibleCells):
                return posibleNeigbor
        return None


    def setVectorN(self):
        for (x,y), element in np.ndenumerate(self.matriz4x4):
            if(element != -1 and element != 2):
                self.vectorN.append((x,y))
                
    def addVisitedPosition(self,position):
        self.matriz1x1[position[0],position[1]] = 4
        for element in self.vectorV:
            if(element == position):
                break
        self.vectorN.append(position)
            

    
    def getMatriz1x1(self,matriz4x4):
        matriz1x1 = 0
        rows = 0
        for element in matriz4x4:
            rows = rows + 1
        colums = len(matriz4x4[0])
        print(str(colums / 2) + " " + str(rows / 2))
        matriz1x1 = np.zeros((rows / 2,colums / 2))
        seedRows = range(0,rows)
        seedColumns = range(0,colums)
        seeds = (list((x,y) for x in seedRows if (x % 2 == 0) for y in seedColumns if (y % 2 == 0)))
        print(matriz1x1)
        print(seeds)
        index = 0
        for (x,y), element in np.ndenumerate(matriz1x1):
            self.nodes.append(((x,y),self.getNode4x4(seeds[index])))
            matriz1x1[x,y] = self.getNode1x1State(seeds[index])
            if (self.getNode1x1State(seeds[index]) == -1):
                for element in self.getNode4x4(seeds[index]):
                    self.matriz4x4[element[0],element[1]] = -1
            index = index + 1
        print(self.nodes)
        print(matriz1x1)
        print(self.matriz4x4)
        return matriz1x1

    
    def getNode4x4(self,position):
        cells = []
        cells.append(position)
        cells.append((position[0],position[1] + 1))
        cells.append((position[0] + 1,position[1] + 1))
        cells.append((position[0] + 1,position[1]))
        return cells

    def getNode1x1State(self,position):
        cells = []
        cells.append(position)
        cells.append((position[0],position[1] + 1))
        cells.append((position[0] + 1,position[1] + 1))
        cells.append((position[0] + 1,position[1]))
        for element in cells:
            if(self.matriz4x4[element[0],element[1]] == -1):
                return -1            
            if(self.matriz4x4[element[0],element[1]] == 2):
                return 2
            
        return 0

    def getInitialPosition(self):    
        for (x,y), element in np.ndenumerate(self.matriz1x1):
            if (element == 2):
                self.initial1x1 = (x,y)
        
        for (x,y), element in np.ndenumerate(self.matriz4x4):
            if (element == 2):
                self.initial4x4 = (x,y)
    
    def getPosiblesNextNodes(self,currentPosition,lastPosition):
        posibleNodes = []
        row = currentPosition[0] - lastPosition[0]
        column = currentPosition[1] - lastPosition[1]
        if(row > 0 and column == 0):
            posibleNodes.append((currentPosition[0],currentPosition[1] - 1))
            posibleNodes.append((currentPosition[0] + 1,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] + 1))
            posibleNodes.append((currentPosition[0] - 1,currentPosition[1]))
            return posibleNodes
        elif (row == 0 and column > 0):
            posibleNodes.append((currentPosition[0] + 1,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] + 1))
            posibleNodes.append((currentPosition[0] - 1,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] - 1))
            return posibleNodes

        elif (row < 0 and column == 0):
            posibleNodes.append((currentPosition[0] ,currentPosition[1] + 1))
            posibleNodes.append((currentPosition[0] - 1,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] - 1))
            posibleNodes.append((currentPosition[0] + 1 ,currentPosition[1]))
            return posibleNodes
        elif (row == 0 and column < 0):
            posibleNodes.append((currentPosition[0] - 1,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] - 1))
            posibleNodes.append((currentPosition[0] + 1 ,currentPosition[1]))
            posibleNodes.append((currentPosition[0] ,currentPosition[1] + 1))
            return posibleNodes
            
        
        


    

    
