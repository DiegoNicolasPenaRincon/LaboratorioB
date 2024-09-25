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