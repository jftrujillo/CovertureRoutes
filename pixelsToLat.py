from osgeo import gdal
import csv
ds = gdal.Open('comple_modificado.tif')

# unravel GDAL affine transform parameters
c, a, b, f, d, e = ds.GetGeoTransform()
puntos = []

def pixel2coord(col, row):
    """Returns global coordinates to pixel center using base-0 raster index"""
    xp = a * col + b * row + a * 0.5 + b * 0.5 + c
    yp = d * col + e * row + d * 0.5 + e * 0.5 + f
    return(xp, yp)



if __name__ == "__main__":
    #primero que sale -76 es longitud, el otro latitud    
    with open('coverturaDFS.txt','rb') as file:
        spamreader = csv.reader(file, delimiter = ',', quotechar = "|")
        for row in spamreader:
            puntos.append(pixel2coord(int(row[1]),int(row[0])))
    
    with open('puntosDfs.txt','wb') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(puntos)
    
    puntosDfs8 = []
    with open('coverturaDfs8.txt',"rb") as file:
        spamreader = csv.reader(file, delimiter = ',', quotechar = "|")
        for row in spamreader:
            puntosDfs8.append(pixel2coord(int(row[1]),int(row[0])))
    with open('puntosDfs8.txt','wb') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(puntosDfs8)
    
    puntosEspiral = []
    with open('coverturaEspiral.txt',"rb") as file:
        spamreader = csv.reader(file, delimiter = ',', quotechar = "|")
        for row in spamreader:
            puntosEspiral.append(pixel2coord(int(row[1]),int(row[0])))
    
    with open('puntosEspiral.txt','wb') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(puntosEspiral)

    puntosStc = []

    with open('coverturaSTC.txt',"rb") as file:
        spamreader = csv.reader(file, delimiter = ',', quotechar = "|")
        for row in spamreader:
            puntosStc.append(pixel2coord(int(row[1]),int(row[0])))
    
    with open('puntosSTC.txt','wb') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(puntosStc)


    puntosSunshine = []

    with open('coverturaSunshine.txt',"rb") as file:
        spamreader = csv.reader(file, delimiter = ',', quotechar = "|")
        for row in spamreader:
            puntosSunshine.append(pixel2coord(int(row[1]),int(row[0])))


    with open('puntosSunshine.txt','wb') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(puntosSunshine)
    

    


    