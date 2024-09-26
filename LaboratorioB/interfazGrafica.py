from tkinter import *
import random

from tkinter import messagebox

#Variables importantes

alfabeto=set()
lenguaje1=set()
lenguaje2=set()
lenguaje3=set()
union1_2=set()
union1_3=set()
union2_3=set()
interseccion1_2=set()
interseccion1_3=set()
interseccion2_3=set()
cerraduraEstrella1=set()
cerraduraEstrella2=set()
cerraduraEstrella3=set()
mostrarResultadosOperacion=Label

#Metodos

"""Pide los elementos del alfabeto al usuario"""
def pedirElementos(simbolo,alfabeto):
    simbolo=simbolo.strip()
    if simbolo!='':
        alfabeto.add(simbolo)
    print(alfabeto)

    #print(len(simbolo))
    return alfabeto

"""Crea un arreglo, que rellena con los elementos del conjunto alfabeto, esto se hizo asi para que sea
mucho mas facil obtener los elementos del conjunto"""
def igualarArreglo(alfabeto):
    lenguaje = []
    for elementoAlfabeto in alfabeto:
        lenguaje.append(elementoAlfabeto)
    return lenguaje

"""Forma un lenguaje aleatorio, concatenandose con el mismo. Hay que tener en cuenta que el alfabeto solo se concatena tres veces"""
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

"""Union entre dos lenguajes"""
def unionConjuntos(conjunto1, conjunto2,estado):
    global union1_2
    global union1_3
    global union2_3

    if estado==1:
        union1_2=set(conjunto1)
        for elemento in conjunto2:
            union1_2.add(elemento)
    elif estado==2:
        union1_3=set(conjunto1)
        for elemento in conjunto2:
            union1_3.add(elemento)
    elif estado==3:
        union2_3=set(conjunto1)
        for elemento in conjunto2:
            union2_3.add(elemento)

"""Interseccion de dos lenguajes"""
def interseccionConjuntos(conjunto1, conjunto2,estado):
    interseccion = set()
    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            if (elemento1 == elemento2):
                interseccion.add(elemento1)

    if estado==1:
        global interseccion1_2
        interseccion1_2=set(interseccion)

    elif estado==2:
        global interseccion1_3
        interseccion1_3 = set(interseccion)

    elif estado==3:
        global interseccion2_3
        interseccion2_3 = set(interseccion)

    return interseccion

"""Genera la cerradura estrella de un lenguaje, hasta cierto punto"""
def generarEstrella(lenguajeUtilizar,cantidadConcatenaciones):
    global alfabeto
    nuevoLenguaje = set()
    lenguajeAuxiliar=set()
    estado=0
    if lenguajeUtilizar=='lenguaje 1':
        global lenguaje1
        lenguajeAuxiliar=set(lenguaje1)
        estado=7
    elif lenguajeUtilizar=='lenguaje 2':
        global lenguaje2
        lenguajeAuxiliar = set(lenguaje2)
        estado=8
    else:
        global lenguaje3
        lenguajeAuxiliar=set(lenguaje3)
        estado=9
    while cantidadConcatenaciones > 0:
        for elemento1 in alfabeto:
            for elemento2 in lenguajeAuxiliar:
                nuevoLenguaje.add(elemento1 + elemento2)
        lenguajeAuxiliar.update(nuevoLenguaje)
        cantidadConcatenaciones -= 1
    nuevoLenguaje.update(lenguajeAuxiliar)
    nuevoLenguaje.add('ε')

    if lenguajeUtilizar == 'lenguaje 1':
        global cerraduraEstrella1
        cerraduraEstrella1=set(nuevoLenguaje)
        print(cerraduraEstrella1)
    elif lenguajeUtilizar == 'lenguaje 2':
        global cerraduraEstrella2
        cerraduraEstrella2=set(nuevoLenguaje)
        print(cerraduraEstrella2)
    else:
        global cerraduraEstrella3
        cerraduraEstrella3=set(nuevoLenguaje)
        print(cerraduraEstrella3)

    modificarLabel(estado)

"""Muestra los resultados de la operacion del lenguaje que el usuario escoja"""
def modificarLabel(estado):
    if estado==1:
        mostrarResultadosOperacion.config(text=union1_2,font=('Times', 10),wraplength=800)
    elif estado==2:
        mostrarResultadosOperacion.config(text=union1_3, font=('Times', 10),wraplength=800)
    elif estado==3:
        mostrarResultadosOperacion.config(text=union2_3, font=('Times', 10),wraplength=800)
    elif estado==4:
        mostrarResultadosOperacion.config(text=interseccion1_2, font=('Times', 10),wraplength=800)
    elif estado==5:
        mostrarResultadosOperacion.config(text=interseccion1_3, font=('Times', 10),wraplength=800)
    elif estado==6:
        mostrarResultadosOperacion.config(text=interseccion2_3, font=('Times', 10),wraplength=800)
    elif estado==7:
        mostrarResultadosOperacion.config(text=cerraduraEstrella1, font=('Times', 10),wraplength=800)
    elif estado==8:
        mostrarResultadosOperacion.config(text=cerraduraEstrella2, font=('Times', 10),wraplength=800)
    elif estado==9:
        mostrarResultadosOperacion.config(text=cerraduraEstrella3, font=('Times', 10),wraplength=800)

"""Verificar si una palabra es palindroma"""
def verificarPalindrocidad(palabra):
    palabra=palabra.strip()
    if palabra!='':
        contador = len(palabra) - 1
        palabraReversa = ''
        while contador > -1:
            palabraReversa += palabra[contador]
            contador -= 1
        if palabraReversa == palabra:
             messagebox.showinfo('Informacion','La palabra es palindroma')
        else:
            messagebox.showinfo('Informacion', 'La palabra no es palindroma')
    else:
        messagebox.showerror('Error', 'Ingrese bien la palabra porfavor')

"""Inviertre una palabra"""
def invertirCadena(palabra):
    palabra=palabra.strip()
    if palabra!='':
        contador = len(palabra) - 1
        palabraReversa = ''
        while contador > -1:
            palabraReversa += palabra[contador]
            contador -= 1
        messagebox.showinfo('Palabra invertida', palabraReversa)
    else:
        messagebox.showerror('Error', 'Ingrese bien la palabra porfavor')

"""Inicializa la ventana de gestion de palabras"""
def mostrarInterfazPalabras():
    ventana3=Tk()
    ventana3.geometry("600x400")
    ventana3.title('Gestion de palabras')

    titulopalindromaLabel=Label(ventana3, text="Gestion de palabras", font=('Times', 25),bg='orange')
    ingresarPalindromaLabel=Label(ventana3, text="Ingrese la palabra", font=('Times', 14),bg='orange')
    ingresarPalabraEntry = Entry(ventana3, font=('Times', 14))
    verificarPalindromaButton = Button(ventana3, text='Verificar palindroma', font=('Times', 12), bg='Orange',command= lambda: verificarPalindrocidad(ingresarPalabraEntry.get()))
    invertirPalabraButton=Button(ventana3, text="Invertir cadena", font=('Times', 12), bg='Orange',command= lambda: invertirCadena(ingresarPalabraEntry.get()))

    titulopalindromaLabel.grid(row=0, column=1,pady=30)
    ingresarPalindromaLabel.grid(row=1,column=0,padx=30)
    ingresarPalabraEntry.grid(row=1,column=1,pady=30)
    verificarPalindromaButton.grid(row=2,column=1,pady=30)
    invertirPalabraButton.grid(row=3,column=1)

    ventana3.mainloop()

"""Instancia la interfaz que muestra las operaciones con lenguajes"""
def establecerContinuar(alfabeto):
    alfabetoApoyo=[]
    alfabetoApoyo=igualarArreglo(alfabeto)
    if len(alfabeto)!=0:
        ventana2 = Tk()
        ventana2.geometry("1200x1920")
        ventana2.title('Operaciones con lenguajes')

        global lenguaje1
        global lenguaje2
        global lenguaje3
        lenguaje1=formarLenguajes(alfabetoApoyo,alfabetoApoyo)
        alfabetoApoyo=igualarArreglo(alfabeto)
        lenguaje2=formarLenguajes(alfabetoApoyo,alfabetoApoyo)
        alfabetoApoyo = igualarArreglo(alfabeto)
        lenguaje3=formarLenguajes(alfabetoApoyo,alfabetoApoyo)

        global mostrarResultadosOperacion
        mostrarResultadosOperacion = Label(ventana2)
        lenguaje1Label = Label(ventana2, text="Lenguaje 1", font=('Times', 14), bg='orange')
        lenguaje2Label = Label(ventana2, text="Lenguaje 2", font=('Times', 14), bg='orange')
        lenguaje3Label = Label(ventana2, text="Lenguaje 3", font=('Times', 14), bg='orange')
        unionButton1_2 = Button(ventana2, text="Union lenguaje 1 y 2", font=('Times', 14), bg='orange',command=lambda: [unionConjuntos(lenguaje1,lenguaje2,1),modificarLabel(1)])
        unionButton1_3 = Button(ventana2, text="Union lenguaje 1 y 3", font=('Times', 14), bg='orange',command=lambda: [unionConjuntos(lenguaje1,lenguaje3,2),modificarLabel(2)])
        unionButton2_3 = Button(ventana2, text="Union lenguaje 2 y 3", font=('Times', 14), bg='orange',command=lambda: [unionConjuntos(lenguaje2,lenguaje3,3),modificarLabel(3)])
        interseccionButton1_2=Button(ventana2,text="Interseccion lenguaje 1 y 2", font=('Times', 14), bg='orange',command=lambda: [interseccionConjuntos(lenguaje1,lenguaje2,1),modificarLabel(4)])
        interseccionButton1_3=Button(ventana2,text="Interseccion lenguaje 1 y 3",font=('Times', 14), bg='orange',command=lambda: [interseccionConjuntos(lenguaje1,lenguaje2,2),modificarLabel(5)])
        intersecccionButton2_3=Button(ventana2,text="Interseccion lenguaje 2 y 3",font=('Times', 14), bg='orange',command=lambda: [interseccionConjuntos(lenguaje1,lenguaje2,3),modificarLabel(6)])

        lenguaje1MostrarLabel = Label(ventana2, width=30, height=15, padx=20,pady=20,text=lenguaje1)
        lenguaje2MostrarLabel = Label(ventana2, width=30, height=15, padx=20,pady=20,text=lenguaje2)
        lenguaje3MostrarLabel = Label(ventana2, width=30, height=15, padx=20,pady=20,text=lenguaje3)

        cantidadConcatenacionesSpBox=Spinbox(ventana2,from_=0,to=3,state="readonly")
        cantidadConcatenacionesLabel=Label(ventana2, text="Cantidad de concatenaciones de su cerradura estrella", font=('Times', 14), bg='orange')
        lenguajeCerraduraSpnBox=Spinbox(ventana2,state="readonly",values=['lenguaje 1','lenguaje 2','lenguaje 3'])
        generarCerraduraEstrellaButton=Button(ventana2,text="Generar cerradura estrella", font=('Times', 14), bg='orange',command=lambda: generarEstrella(lenguajeCerraduraSpnBox.get(),int(cantidadConcatenacionesSpBox.get())) )
        resultadosLabel=Label(ventana2, text="Resultados operacion", font=('Times', 14),bg='orange')

        lenguaje1MostrarLabel.grid(row=2, column=0, padx=30)
        lenguaje2MostrarLabel.grid(row=2, column=2, padx=30)
        lenguaje3MostrarLabel.grid(row=2, column=4, padx=30)
        lenguaje1Label.grid(row=0, column=0, pady=30)
        lenguaje2Label.grid(row=0, column=2, pady=30)
        lenguaje3Label.grid(row=0, column=4, pady=30)
        unionButton1_2.grid(row=3, column=0,pady=30)
        unionButton1_3.grid(row=3, column=2,pady=30)
        unionButton2_3.grid(row=3, column=4,pady=30)
        interseccionButton1_2.grid(row=4,column=0,pady=30)
        interseccionButton1_3.grid(row=4,column=2)
        intersecccionButton2_3.grid(row=4,column=4)
        cantidadConcatenacionesLabel.grid(row=5,column=0)
        cantidadConcatenacionesSpBox.grid(row=5,column=2)
        lenguajeCerraduraSpnBox.grid(row=5,column=3)
        generarCerraduraEstrellaButton.grid(row=6,column=2,pady=30)
        resultadosLabel.grid(row=7,column=0,pady=30)
        mostrarResultadosOperacion.grid(row=8,column=0)



        print(lenguaje1)
        print(lenguaje2)
        print(lenguaje3)

        ventana2.mainloop()
    else:
        messagebox.showerror('Error', 'No puede continuar con el alfabeto vacio')


"""Ventana principal"""

ventana=Tk()
ventana.geometry("500x400")

ventana.title('Pagina principal')

tituloLabel=Label(ventana,text="Bienvenidos",font=('Times', 25),bg='orange')

ingresarCantidadLabel=Label(ventana,text="Ingrese un simbolo del alfabeto",font=('Times', 14),bg='orange')

ingresarCantidadEntry=Entry(ventana,font=('Times',14))

ingresarCantidadButton=Button(ventana,text='Ingresar simbolo',font=('Times',12),bg='Orange',command=lambda: pedirElementos(ingresarCantidadEntry.get(),alfabeto))

continuarButton=Button(ventana,text='Formar lenguajes',font=('Times',12),bg='Orange',command=lambda: establecerContinuar(alfabeto))

interfazPalabrasButton=Button(ventana,text='Gestion de palindromas',font=('Times',12),bg='Orange',command=lambda: mostrarInterfazPalabras())

tituloLabel.grid(row=0,column=1,pady=30)
ingresarCantidadLabel.grid(row=2,column=1,pady=30)
ingresarCantidadEntry.grid(row=3,column=1)
ingresarCantidadButton.grid(row=4,column=1,pady=20)
continuarButton.grid(row=5,column=1,pady=20)
interfazPalabrasButton.grid(row=6,column=0)

ventana.mainloop()


