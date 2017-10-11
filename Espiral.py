import numpy as np
import copy
from matricesVacias import matricesVacias
from Graphics import Graphics

class Espiral:

    def __init__(self): 
        pass
    
    def getCoverturePath(self,a,pi_x,pi_y):
        
        A = np.matrix([[0,-1],
                        [1,0]])
        B = np.matrix([[0,1],
                        [-1,0]])
        hm,gm = a.shape

        visitado = 1
        obstaculo = -1
        nothing = 0
        
        visitados = []
        pactual = np.matrix([[pi_x],[pi_y]])
        a[pi_x][pi_y] = visitado
        visitados.append((pactual[0,0],pactual[1,0]))

        panterior = np.matrix([])
        print("aqui")
        while any (nothing in arr for arr in a):
            if len(panterior) == 1:
                if gm - 1 > pi_y:
                    psiguiente = np.matrix([[pi_x],[pi_y +1]])
                else:
                    psiguiente = np.matrix([[pi_x],[pi_y-1]])
            else:
                r = pactual - panterior
                ##print(r)
                ##print(b)
                psiguiente = pactual + (A*r)
                ##print(psiguiente)
                x = int(psiguiente[0,0])
                y = int (psiguiente[1,0])
                if (x<0 or y<0 or x>hm-1 or y>gm-1 or a[x][y]==obstaculo or  a[x][y]==visitado):
                    psiguiente = pactual + (r)
                    ##print(psiguiente)
                    x = int(psiguiente[0,0])
                    y = int (psiguiente[1,0])
                    if (x<0 or y<0 or x>hm-1 or y>gm-1 or a[x][y]==obstaculo or  a[x][y]==visitado):
                        psiguiente = pactual + (B*r)
                        x = int(psiguiente[0,0])
                        y = int (psiguiente[1,0])
                        if (x<0 or y<0 or x>hm-1 or y>gm-1 or a[x][y]==obstaculo or  a[x][y]==visitado):
                            #psiguiente = panterior
                            ##obtener el index de la posicion anterior en el vector de visitados
                            ##obtener el indice de esta posicon donde se cierra y hacer la siguinte coordenada a la corrdenada anterior en el vector de visitados.
                            f = int(pactual[0,0])
                            g = int (pactual[1,0])
                            i = visitados.index((f,g))
                            xc,yc = visitados[i-1]
                            psiguiente = np.matrix([[xc],[yc]])
                            print(visitados)                       
            print(psiguiente)
            panterior = pactual
            pactual = psiguiente
            visitados.append((pactual[0,0],pactual[1,0]))
            xa = int(pactual[0,0])
            ya = int (pactual[1,0])
            a[xa][ya] = visitado
        print(visitados)
        return visitados



        
        

        
        
