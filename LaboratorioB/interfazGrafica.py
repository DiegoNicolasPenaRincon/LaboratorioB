from tkinter import *
import random

"""Variables importantes"""

alfabeto=set()
lenguaje1=set()
lenguaje2=set()
lenguaje3=set()

"""Validaciones"""



"""Metodos"""

def pedirElementos(simbolo,alfabeto):
    simbolo=simbolo.strip()
    if simbolo!='':
        alfabeto.add(simbolo)
    print(alfabeto)

    #print(len(simbolo))
    return alfabeto

def igualarArreglo(alfabeto):
    i = 0
    lenguaje = []
    for elementoAlfabeto in alfabeto:
        lenguaje.append(elementoAlfabeto)
    return lenguaje

def establecerContinuar(alfabeto):
    alfabetoApoyo=[]
    alfabetoApoyo=igualarArreglo(alfabeto)
    if len(alfabeto)!=0:
        global lenguaje1
        global lenguaje2
        global lenguaje3
        lenguaje1=formarLenguajes(alfabetoApoyo,alfabetoApoyo)
        alfabetoApoyo=igualarArreglo(alfabeto)
        lenguaje2=formarLenguajes(alfabetoApoyo,alfabetoApoyo)
        alfabetoApoyo = igualarArreglo(alfabeto)
        lenguaje3=formarLenguajes(alfabetoApoyo,alfabetoApoyo)

        print(lenguaje1)
        print(lenguaje2)
        print(lenguaje3)

def formarLenguajes(alfabeto, lenguajeApoyo):
    lenguajeRetorno = set()
    alfabeto=igualarArreglo(alfabeto)
    CantidadCombinaciones = random.randint(1, 3)
    while CantidadCombinaciones > 0:
        j = 0
        limiteApoyo = len(lenguajeApoyo)
        while j < len(alfabeto):
            k = 0
            while k < limiteApoyo:
                lenguajeApoyo.append(alfabeto[j] + lenguajeApoyo[k])
                k += 1
            j += 1
        CantidadCombinaciones -= 1
    CantidadPalabras = 3
    while CantidadPalabras > 0:
        lenguajeRetorno.add(lenguajeApoyo[random.randint(0, len(lenguajeApoyo) - 1)])
        CantidadPalabras -= 1
    return lenguajeRetorno


"""Interfaz grafica"""
ventana=Tk()
ventana.geometry("1080x1920")

tituloLabel=Label(ventana,text="Bienvenidos",font=('Times', 25),bg='orange')

ingresarCantidadLabel=Label(ventana,text="Ingrese un simbolo del alfabeto",font=('Times', 14),bg='orange')

ingresarCantidadEntry=Entry(ventana,font=('Times',14))

ingresarCantidadButton=Button(ventana,text='Ingresar simbolo',font=('Times',12),bg='Orange',command=lambda: pedirElementos(ingresarCantidadEntry.get(),alfabeto))

continuarButton=Button(ventana,text='Formar lenguajes',font=('Times',12),bg='Orange',command=lambda: establecerContinuar(alfabeto))

unionButton=Button(ventana,text='Interseccion',font=('Times',12),bg='Orange')



tituloLabel.grid(row=0,column=2,pady=30)
ingresarCantidadLabel.grid(row=2,column=0,padx=20,pady=30)
ingresarCantidadEntry.grid(row=2,column=1)
ingresarCantidadButton.grid(row=3,column=1)
continuarButton.grid(row=3,column=3)
unionButton.grid(row=4,column=1)

ventana.mainloop()


