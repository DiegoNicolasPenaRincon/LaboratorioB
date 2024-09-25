import random


def pedirElementos():
    alfabeto = []
    cantidadSimbolos = int(input('Ingrese la cantidad de simbolos que va a tener su alfabeto'))
    while cantidadSimbolos > 0:
        simbolo = input('ingrese el elemento')
        alfabeto.append(simbolo)
        cantidadSimbolos -= 1
    return alfabeto


def igualarArreglo(alfabeto):
    i = 0
    lenguaje = []
    while i < len(alfabeto):
        lenguaje.append(alfabeto[i])
        i += 1
    return lenguaje


def formarLenguajes(alfabeto, lenguajeApoyo):
    lenguajeRetorno = []
    CantidadCombinaciones = random.randint(1, 3)
    while CantidadCombinaciones > 0:
        j = 0
        limiteApoyo = len(lenguajeApoyo)
        while j < len(alfabeto) - 1:
            k = 0
            while k < limiteApoyo:
                lenguajeApoyo.append(alfabeto[j] + lenguajeApoyo[k])
                k += 1
            j += 1
        CantidadCombinaciones -= 1
    CantidadPalabras = 3
    while CantidadPalabras > 0:
        lenguajeRetorno.append(lenguajeApoyo[random.randint(0, len(lenguajeApoyo) - 1)])
        CantidadPalabras -= 1
    return lenguajeRetorno


def unionConjuntos(conjunto1, conjunto2):
    union = set(conjunto1)
    for elemento2 in conjunto2:
        union.add(elemento2)
    return union


def interseccionConjuntos(conjunto1, conjunto2):
    interseccion = set()
    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            if (elemento1 == elemento2):
                interseccion.add(elemento1)
    return interseccion


def generarEstrella(lenguaje, alfabeto):
    cantidadConcatenaciones = int(input('Ingrese la cantidad de cancatenaciones que va a tener su lenguaje'))
    nuevoLenguaje = set()
    while cantidadConcatenaciones > 0:
        for elemento1 in alfabeto:
            for elemento2 in lenguaje:
                nuevoLenguaje.add(elemento1 + elemento2)
        cantidadConcatenaciones -= 1
    return nuevoLenguaje


def verificarPalindrocidad(palabra):
    contador = len(palabra) - 1
    palabraReversa = ''
    while contador > -1:
        palabraReversa += palabra[contador]
        contador -= 1
    if palabraReversa == palabra:
        return True
    return False

def invertirCadena(palabra):
    contador = len(palabra) - 1
    palabraReversa = ''
    while contador > -1:
        palabraReversa += palabra[contador]
        contador -= 1
    return palabraReversa

"""def cambiarSimboloPalabraLenguaje(alfabeto,palabraLenguaje):
    simbolo=input('Ingrese la cantidad de simbolos que va a tener su alfabeto')
    for simboloAlfabeto in alfabeto:
        if simboloAlfabeto==simbolo:
            """



alfabeto = pedirElementos()
print(alfabeto)
lenguajeApoyo = igualarArreglo(alfabeto)
print(lenguajeApoyo)
lenguaje1 = set(formarLenguajes(alfabeto, lenguajeApoyo))
lenguaje2 = set(formarLenguajes(alfabeto, lenguajeApoyo))
lenguaje3 = set(formarLenguajes(alfabeto, lenguajeApoyo))
print(lenguaje1)
print(lenguaje2)
print(lenguaje3)
union1_2=unionConjuntos(lenguaje1,lenguaje2)
print(union1_2)
interseccion1_2=interseccionConjuntos(lenguaje1,lenguaje2)
print(interseccion1_2)
estrella=generarEstrella(lenguaje1,alfabeto)
print(estrella)
esPalindroma = verificarPalindrocidad('ana')
#print(esPalindroma)
cadenaInvertida=invertirCadena('ana')
print(cadenaInvertida)
