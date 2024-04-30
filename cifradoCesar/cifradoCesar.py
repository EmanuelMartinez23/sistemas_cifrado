abc = 'abcdefghijklmnopqrstuvwxyz'
def cifrado_cesar(texto,clave):
    # establecemos todas las letras en minusculas
    texto = texto.lower()
    # creamos una variable donde vamos a guardar el cifrado
    texto_cifrado= ''
    # iteramos en el texto ingresado
    for caracter in texto:
        # verificamos si el caracter es del alfabeto
        if caracter.isalpha():
            # obtenemos el indice del caracter en el abc y sumanos el despla(clave)
            #print(abc.find(caracter))
            indice = abc.find(caracter) + clave
            # obtenemos la posición  del caracter que va a ser 
            modulo = int(indice) % len(abc)
            # añadimos al string el caracter difrado
            texto_cifrado = texto_cifrado + str(abc[modulo])
        else:
            # si no esta el caracter en abc que se agregue al texto cifrado igual
            texto_cifrado += caracter
    
    return texto_cifrado

def descifrado_cesar(texto,clave):
    # establecemos todas las letras en minusculas
    texto = texto.lower()
    # creamos una variable donde vamos a guardar el cifrado
    texto_cifrado= ''
    # iteramos en el texto ingresado
    for caracter in texto:
        # verificamos si el caracter es del alfabeto
        if caracter.isalpha():
            # obtenemos el indice del caracter en el abc y sumanos el despla(clave)
            #print(abc.find(caracter))
            indice = abc.find(caracter) - clave
            # obtenemos la posición  del caracter que va a ser 
            modulo = int(indice) % len(abc)
            # añadimos al string el caracter difrado
            texto_cifrado = texto_cifrado + str(abc[modulo])
        else:
            # si no esta el caracter en abc que se agregue al texto cifrado igual
            texto_cifrado += caracter

    return texto_cifrado




entrada = "E#manuel"
clave = 54
texto_cifrado = cifrado_cesar(entrada,clave)
print("Texto cifrado: ", texto_cifrado)
texto_descifrado = descifrado_cesar(texto_cifrado,clave)
print("Texto descifrado: ", texto_descifrado)


