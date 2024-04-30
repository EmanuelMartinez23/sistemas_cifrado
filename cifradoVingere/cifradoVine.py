
# alfabeto extendido 
alfabetoExtendido = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()-_=+[{]}|;:'\",<.>/?`~"

# funcion que toma un mensaje y clave a cifrar
def vigenereCifrar(mensaje, clave):
    # creamos una variable que va a almacenar el mensaje cifrado
    mensajeCifrado = "" 
    # ajustamos la clave con el mensaje , repetimos la clave tantas veces sea para que conincidad con el msj
    claveRepetida = (clave * (len(mensaje) // len(clave))) + clave[:len(mensaje) % len(clave)]

    # Iteramos sobre el mensaje
    for i in range(len(mensaje)):
        # verificamos si el caracter esta en el alfabeto
        if mensaje[i] in alfabetoExtendido:
            # calculamos ese desplazamiento sumando los indices del caracter de nuestro mensaje y la clave
            shift = (alfabetoExtendido.index(mensaje[i]) + alfabetoExtendido.index(claveRepetida[i])) % len(alfabetoExtendido)
            # agregamos el caracter cifrado a la variable que almacena el mensaje cifrado
            mensajeCifrado += alfabetoExtendido[shift]
        else:
            # si es que no esta en el alfabeto lo agregamos como tal al mensaje cifrado
            mensajeCifrado += mensaje[i]
    # retornamos el mensaje cifrado
    return mensajeCifrado

# funcion que toma un mensaje y clave con la que se cifro cifrar
def vigenere_descifrar(mensajeCifrado, clave):
    # variable para almacenar el mensaje descifrado
    mensajeDescifrado = "" 
    
    # ajustamos la clave con  el msj
    claveRepetida = (clave * (len(mensajeCifrado) // len(clave))) + clave[:len(mensajeCifrado) % len(clave)]

    # Iteramos sobre cada caracter del mensaje cifrado.
    for i in range(len(mensajeCifrado)):
        # verificamos que el caracter esta en el alfabeto
        if mensajeCifrado[i] in alfabetoExtendido:
            shift = (alfabetoExtendido.index(mensajeCifrado[i]) - alfabetoExtendido.index(claveRepetida[i])) % len(alfabetoExtendido)
            # agregamos el caracter al mensaje descifrado
            mensajeDescifrado += alfabetoExtendido[shift]
        else:

            #si no solo lo agregamos como tal
            mensajeDescifrado += mensajeCifrado[i]

    return mensajeDescifrado

# funcion que cifra un archivo, recibe el archivo de entrada, el de salida y la clave 
def cifrar_archivo(archivoEntrada, archivo_salida, clave):
    with open(archivoEntrada, 'r') as f:
        contenido = f.read()

    # ciframos
    contenido_cifrado = vigenereCifrar(contenido, clave)

    # escribimos en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(contenido_cifrado)

# funcion que descifra toma dos archivos el de salida y entrada, con la clave de cifrado
def descifrar_archivo(archivoEntrada, archivo_salida, clave):
    with open(archivoEntrada, 'r') as f:
        contenido_cifrado = f.read()

    # Desciframos
    contenido_descifrado = vigenere_descifrar(contenido_cifrado, clave)

    # escribimos en el archivo de salida
    with open(archivo_salida, 'w') as f:
        f.write(contenido_descifrado)

# EJEMPLO:
archivoEntrada = "text.txt" 
archivoCifrado = "archivoCifrado.txt"
archivoDescifrado = "archivoDescifrado.txt"
clave = "ciber"

# Ciframos el archivo de entrada y guardamos el resultado en el archivo cifrado.
cifrar_archivo(archivoEntrada, archivoCifrado, clave)
print("Archivo cifrado correctamente.")

# Desciframos el archivo cifrado y guardamos el resultado en el archivo descifrado.
descifrar_archivo(archivoCifrado, archivoDescifrado, clave)
print("Archivo descifrado correctamente.")


