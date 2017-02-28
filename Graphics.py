import numpy as np
import time as time

class Graphics:
    """
    clase para ver el funcionamiento de los algoritmos de cobertura
    """
    matriz = 0
    down = 1
    left = 2 
    up = 3
    rigth = 4
    static = 5

    def __init__(self,matriz):
        self.matriz = matriz
        down = 1
        left = 2 
        up = 3
        rigth = 4
        
    

    def printCovertura(self,covertura):
        """
        imprime un demo de como se desplaza el dron en una matriz vacia, sumando + 1 en cada nueva celda
        visitada
        @param covertura: arreglo con la covertura a evaluar.
        """
        for element in covertura:
            if (not(self.matriz[element[0]][element[1]] == 2 or self.matriz[element[0]][element[1]] == 3)):
                self.matriz[element[0]][element[1]] = self.matriz[element[0]][element[1]] + 1
                print(self.matriz)
                time.sleep(0.3)
            else:
                pass
    
    def printCoverturaWithWavefront(self,covertura):
        """
        imprime un demo de como se desplaza el dron en una matriz con distribucion wavefront, colocando  1 en cada nueva celda
        visitada. No muestra re visistas
        @param covertura: arreglo con la covertura a evaluar.
        """
        for element in covertura:
            if (not(self.matriz[element[0]][element[1]] == 2 or self.matriz[element[0]][element[1]] == 3)):
                self.matriz[element[0]][element[1]] = 1
                print(self.matriz)
                time.sleep(0.2)
            else:
                pass
    
    def counter(self):
        """
        Contador de visitas y re visitas. imprime visitas y re visitas
        """
        visit = 0
        reVisit = 0
        for row in self.matriz:
            for column in row:
                if column == 1:
                    visit = visit + 1
                elif column > 1:
                    reVisit = reVisit + (column - 1)

        print("Visitas = " + str(visit))
        print("Re Visitas = " + str(reVisit))
    
    def numberOfTwist(self,covertura):
        """
        imprime la cantidad de giros de 90 grados y de 180 grados.
        @param covertura: arreglo con la covertura a evaluar.
        """
        twist90 = 0
        twist180 = 0
        orientation =  0
        lastOrientation = 0
        for i, element in enumerate(covertura):
            try:
                orientation = self.orientationOfWay(element,covertura[i + 1])
                if (not(orientation == self.static)):
                    if (lastOrientation == orientation):
                        pass
                    else:
                        x = abs(lastOrientation - orientation)
                        if x == 2:
                            #Giro de 180 grados
                            twist180 = twist180 + 1
                        elif x == 1 or x == 3:
                            twist90 = twist90 + 1
                        lastOrientation = orientation
                else:
                    pass
            except:
                pass

        print("Giros de 90 grados: " + str(twist90))
        print("giros de 180 grados: " + str(twist180))

    def orientationOfWay(self,currentPosition,futurePosition):
        row = futurePosition[0] - currentPosition[0]        
        column = futurePosition[1] - currentPosition[1]
        if (row == 0 and column > 0):
            return self.rigth
        if (row == 0 and column < 0):
            return self.left
        if (row > 0 and column == 0):
            return self.down
        if (row < 0 and column == 0):
            return self.up
        if (row == 0 and column == 0):
            return self.static
            





