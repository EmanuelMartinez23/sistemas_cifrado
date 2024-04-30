import numpy as np
import cv2
from PIL import Image
import matplotlib.image as imagen
from os import system as bas


# Funcion que va a convertir la imagen en la matriz
def imageToMatrix(ruta):
    # leemos la imagen original todos sus canales
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED) 
    # convertirmos la imagen aformato rgba
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
    # obtenemos el número de filas de la imagen 
    filas = imagen.shape[0]
    # obtenemos el número de columnas de la iamgen
    columnas = imagen.shape[1]
    # Recorremos todos los pixeles de la imagen y crea un vector de color para cada píxel,
    matrixPixelesColores = []
    for i in range(0, filas):
        for j in range(0, columnas):
            # Añadir el vector de color a la lista
            matrixPixelesColores.append(np.array([imagen[i][j][0], imagen[i][j][1], imagen[i][j][2]]))  
    #print(matrixPixelesColores)
    # retornamos esa "matrix", la lista de pixeles que va contener un vector de colores por cada pixel
    return matrixPixelesColores

# Función para convertir una lista de vectores de colores en una imagen
def matrixToImage(matrixPixelesColores, ruta):
    # leemos la imagen original todos sus canales
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    # convertirmos la imagen aformato rgba 
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGRA2RGBA)
    # obtenemos el número de filas de la imagen
    filas = imagen.shape[0]
    # obtenemos el número de columnas de la imagen
    columnas = imagen.shape[1]

    k = 0
    for i in range(0, filas):
        for j in range(0, columnas):
            imagen[i][j][0] = matrixPixelesColores[k][0]
            imagen[i][j][1] = matrixPixelesColores[k][1] 
            imagen[i][j][2] = matrixPixelesColores[k][2]
            k += 1
    # Convertimos la matriz  a una imagen
    return Image.fromarray(imagen, 'RGBA')  


# funcion para calcular la adjunta de una matriz

def calcuAdjunta(matrix):
    # convertirmos la matrix en unidime
    mtrx = matrix.ravel()
    # cofactores de cada elemento
    A = +((mtrx[4] * mtrx[8]) - (mtrx[5] * mtrx[7]))  # Calcular los elementos de la adjunta
    B = -((mtrx[3] * mtrx[8]) - (mtrx[5] * mtrx[6]))
    C = +((mtrx[3] * mtrx[7]) - (mtrx[6] * mtrx[4]))
    D = -((mtrx[1] * mtrx[8]) - (mtrx[2] * mtrx[7]))
    E = +((mtrx[0] * mtrx[8]) - (mtrx[2] * mtrx[6]))
    F = -((mtrx[0] * mtrx[7]) - (mtrx[1] * mtrx[6]))
    G = +((mtrx[1] * mtrx[5]) - (mtrx[2] * mtrx[4]))
    H = -((mtrx[0] * mtrx[5]) - (mtrx[2] * mtrx[3]))
    I = +((mtrx[0] * mtrx[4]) - (mtrx[1] * mtrx[3]))
    # construimos la matriz de cofactores
    cofactor = np.array([[A, B, C], [D, E, F], [G, H, I]])
    # transponemos la matriz de cofactores para obtener la adjunta  
    adjunta = cofactor.T  
    return adjunta

# funcion que calcular la inversa de la matriz clave
def inversaKey():
    # Calculamos el determinante de la clave
    deterKey = int(np.linalg.det(Key)) % 256
    # calculamos  la inversa del determinante  
    det_inv_mod = pow(deterKey, -1, 256)
    # calculamos  la adjunta de la clave  
    adj_key = calcuAdjunta(Key) % 256  
    # calculamos la inversa de la clave
    key_inv = (det_inv_mod * adj_key) % 256  
    # la retornamos
    return key_inv

# funcion que reune todo y cifra una imagen
def encrypt(ruta):
    matrixPixelesColores = imageToMatrix(ruta)  # Convertir la imagen en una lista de vectores de colores
     # Inicializar una lista para almacenar los vectores de color cifrados
    listaColorEncrip = []
    for i in matrixPixelesColores:
        # Cifrar cada vector de color utilizando la clave
        # @ multiplicacion matricial
        listaColorEncrip.append((i @ Key) % 256)  
    # convertimos la lista de vectores de color cifrados en una imagen    
    imagenCifrada = matrixToImage(listaColorEncrip, ruta)  
    imagenCifrada.save("imagen_cifrada.png")

# funcion que reune todo para descifrar una imagen
def decrypt(ruta):
    #Convertirmos la imagen en lista de vectores de colores
    matrixPixelesColores = imageToMatrix(ruta)
    # calculamos la inversa de la matrix clave
    key_inv = inversaKey()  
    listaColorDescifra = []
    for px in matrixPixelesColores:
        # desciframos cada vector de color utilizando la inversa de la clave
        listaColorDescifra.append((px @ key_inv) % 256)  
    imagenDescifrada = matrixToImage(listaColorDescifra, ruta)
    imagenDescifrada.save("imagen_descifrada.png")


Key = np.array([[6, 2, 1], [13, 16, 10], [20, 17, 15]])
encrypt("Img12.bmp")
print("¡Encriptación completada!")
decrypt("imagen_cifrada.png")
print("¡Desencriptación completada!")
