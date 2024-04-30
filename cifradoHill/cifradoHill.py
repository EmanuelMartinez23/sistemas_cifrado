import numpy as np

# Diccionario para mapear caracteres a números y viceversa
NUMBER_MAP = {
    " ": 0, "!": 1, '"': 2, "#": 3, "$": 4, "%": 5, "&": 6, "'": 7, "(": 8, ")": 9,
    "*": 10, "+": 11, ",": 12, "-": 13, ".": 14, "/": 15, "0": 16, "1": 17, "2": 18, "3": 19,
    "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, ":": 26, ";": 27, "<": 28, "=": 29,
    ">": 30, "?": 31, "@": 32, "A": 33, "B": 34, "C": 35, "D": 36, "E": 37, "F": 38, "G": 39, "H": 40,
    "I": 41, "J": 42, "K": 43, "L": 44, "M": 45, "N": 46, "O": 47, "P": 48, "Q": 49, "R": 50, "S": 51,
    "T": 52, "U": 53, "V": 54, "W": 55, "X": 56, "Y": 57, "Z": 58, "[": 59, "\\": 60, "]": 61, "^": 62,
    "_": 63, "`": 64, "a": 65, "b": 66, "c": 67, "d": 68, "e": 69, "f": 70, "g": 71, "h": 72, "i": 73,
    "j": 74, "k": 75, "l": 76, "m": 77, "n": 78, "o": 79, "p": 80, "q": 81, "r": 82, "s": 83, "t": 84,
    "u": 85, "v": 86, "w": 87, "x": 88, "y": 89, "z": 90, "{": 91, "|": 92, "}": 93, "~": 94, "\n": 95
}

# Diccionario inverso para mapear números a caracteres
REVERSE_MAP = {v: k for k, v in NUMBER_MAP.items()}

# Función para calcular el máximo común divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Funcion que calcula la matrix inversa
def matrixModInv(matrix, modulo):
    # Calculamos el determinante y vamos a redondear para que sea entero
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = next((i for i in range(1, modulo) if (det * i) % modulo == 1), None)

    if det_inv is None:
        raise ValueError("La Matrix  no es invertible.")

    # Calculate la matrix inversa
    matrixModInv = np.round(det_inv * np.linalg.inv(matrix) * det) % modulo

    #print(matrixModInv.astype(int))
    # regresamos la matriz inversa
    return matrixModInv.astype(int)

# Funcion para convertir el texto en la matriz
def textToMatrix(text, n):
    matrix = [NUMBER_MAP[char] for char in text]
    # cantidad de letras de relleno
    relleno = n - (len(matrix) % n)
    if relleno != n:
        # 95 es el total de caracteres de nuestro dicc
        matrix += [95] * relleno 
    #print(np.array(matrix).reshape(-1, n))
    #retornamos la matriz bidi
    return np.array(matrix).reshape(-1, n)

# funcion que convierte una matriz en texto
def matrixToText(matrix):
    # convertirmos la matrix bidi a unidime para que este en una sola lista
    return "".join(REVERSE_MAP[num] for num in matrix.flatten() if num in REVERSE_MAP)

# funcion para encriptar texto
def encrypt(textoPlano, key):
    # conseguimos la longuit de la clave
    n = len(key)
    # conseguimos la matriz de numeros del texto dado
    matrix = textToMatrix(textoPlano, n)
    # conseguimos la matriz de la clave
    keyMatrix = np.array(key)
    # aqui hacemos con dot la multiplicacion de las dos matrices 
    matrixEncripta = np.dot(matrix, keyMatrix) % 95
    # de acuerdo a nuestra matrix de la multi la pasamos a texto 
    return matrixToText(matrixEncripta)

# funcion para descencripta
def decrypt(textoCifrado, key):
    # loguitud de la clave 
    n = len(key)
    # pasamos el texto cifrado a una matrix 
    matrix = textToMatrix(textoCifrado, n)
    # hacemos la matrix de la clave 
    keyMatrix = np.array(key)
    # hacemos la matrix invertida de la keyMatrix
    keyMatrix_inv = matrixModInv(keyMatrix, 95)
    # conseguimos la matriz descencriptada multiplicando matrices
    matrixDescencrip = np.dot(matrix, keyMatrix_inv) % 95
    # retornamos el texto de la matriz
    return matrixToText(matrixDescencrip)

# funcion que lee el texto de un archivo
def leerTextoDeArchivo(rutaArchivo):
    with open(rutaArchivo, 'r') as file:
        return file.read()

# funcion para escribri en un archivo
def escribirTextoEnArchivo(rutaArchivo, text):
    with open(rutaArchivo, 'w') as file:
        file.write(text.strip())

# funcion donde hacemos todo el proceso de encriptar llamando a los demas metodos
def encriptarArchivo(input_rutaArchivo, output_rutaArchivo, key):
    # obtenemos el texto
    textoPlano = leerTextoDeArchivo(input_rutaArchivo)
    # obtenemo  el texto cifrado
    textoCifrado = encrypt(textoPlano, key)
    # escribimos en el archivo de salida
    escribirTextoEnArchivo(output_rutaArchivo, textoCifrado)

def desencriptarArchivo(input_rutaArchivo, output_rutaArchivo, key):
    textoCifrado = leerTextoDeArchivo(input_rutaArchivo)
    textoDescifrado = decrypt(textoCifrado, key)
    # escribimos el texto descifrado en el archivo 
    escribirTextoEnArchivo(output_rutaArchivo, textoDescifrado)

# Archivos de entrada 
input_rutaArchivo = 'text.txt'
rutaDeArchivoEncriptado = 'texto_encriptado.txt'
rutaDeArchivoDesencriptado = 'texto_desencriptado.txt'

# OUTPUT 
key = [[6, 2, 1], [13, 16, 10], [20, 17, 15]]

# cifrar y descifrar archivos
encriptarArchivo(input_rutaArchivo, rutaDeArchivoEncriptado, key)
desencriptarArchivo(rutaDeArchivoEncriptado, rutaDeArchivoDesencriptado, key)

print("Cifrado completo !!! \nTexto cifrado guardado en la ruta:", rutaDeArchivoEncriptado)
print("Descifrado completado !!!\nTexo cifrado guardado en la ruta:", rutaDeArchivoDesencriptado)
