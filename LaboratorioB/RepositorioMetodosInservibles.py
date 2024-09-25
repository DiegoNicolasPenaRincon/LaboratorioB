"""Validaciones"""

def cantidadAceptada(char):
    if char in '12345678910':
        return True
    return False

"""Metodos"""

def pedirElementos(character):
    alfabeto = []
    if cantidadAceptada(character)==False:
        print('No')
    else:
        cantidadSimbolos = int(character)
        while cantidadSimbolos > 0:
            simbolo = input('ingrese el elemento')
            alfabeto.append(simbolo)
            cantidadSimbolos -= 1
    return alfabeto

def generarEstrella(lenguajeUtilizar, alfabeto,cantidadConcatenaciones):
    nuevoLenguaje = set()
    lenguajeAuxiliar=set()
    if lenguajeUtilizar=='lenguaje 1':
        global lenguaje1
        lenguajeAuxiliar=set(lenguaje1)
    elif lenguajeUtilizar=='lenguaje 1':
        global lenguaje2
        lenguajeAuxiliar = set(lenguaje2)
    else:
        global lenguaje3
        lenguajeAuxiliar=set(lenguaje3)
    while cantidadConcatenaciones > 0:
        for elemento1 in alfabeto:
            for elemento2 in lenguajeAuxiliar:
                nuevoLenguaje.add(elemento1 + elemento2)
        cantidadConcatenaciones -= 1
    return nuevoLenguaje