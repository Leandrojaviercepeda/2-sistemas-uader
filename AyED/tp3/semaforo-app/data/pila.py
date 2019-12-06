#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nodo():
    
    def __init__(self):
        self.info = None
        self.sig = None
        
class Pila():
    
    def __init__(self):
        self.tamanio = 0
        self.tope = None
        
def apilar(pila, x):
    nodo = Nodo()
    nodo.info = x
    nodo.sig = pila.tope
    pila.tope = nodo
    pila.tamanio += 1
    
def desapilar(pila):
    
    x = pila.tope.info
    pila.tope = pila.tope.sig
    pila.tamanio -= 1
    return x

#(determina si una pila es no vacía)
def pilaVacia(pila):
    return (pila.tope == None)

#(Devuelve true si la pila está llena, false si no está llena)
def pilaLlena(pila):
    return False

#(devuelve el ultimo elemento insertado en la pila)
def cimaPila(pila):
    return pila.tope.info


def cargarPila(pila):
    print("Carga de elementos")
    n = "S"
    while not(pilaLlena(pila)) and n == "S":
        x = input("Introduzca un elemento: ")
        apilar(pila, x)
        n = input("'S' para continuar: ")
        n.upper()

#(muestra el contenido de la pila)
def verPila(pila):
    pilaAux = Pila()
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        x = desapilar(pilaAux)
        print (x + ", ")
        apilar(pila, x)

#(Dada una lista de elementos los introduce una pila)
def llenarPila(pila, lista):
        for i in range(len(lista)):
            if not(pilaLlena(pila)):
                apilar(pila, lista[i])


def tamanioPila(pila):
    return pila.tope


"""
1. Realizar un subprograma que obtenga el número de copias
    de un determinado elemento en una pila dada.
"""

def numeroDeCopiasElemento(pila, buscado):
    repeticiones = 0
    pilaAux = Pila()

    while not(pilaVacia(pila)):
        x = desapilar(pila)
        if (x == buscado):
            repeticiones +=1
        apilar(pilaAux, x)

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return repeticiones

"""
2. Utilizando las operaciones sobre pilas,
    desarrollar un subprograma que permita eliminar
    de una pila de enteros todos los números impares.
"""

def eliminarImpares(pila):
    pilaAux = Pila()
    while not(pilaVacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pilaAux, x)

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

"""
3. Haciendo uso de las operaciones sobre pilas,
    realizar un programa que permita cambiar todas
    las apariciones de un determinado x de
    la pila por otro dado.
"""

def cambiarX(pila, buscado, x):

    pilaAux = Pila()
    while not(pilaVacia(pila)):
        if (cimaPila(pila) == buscado):
            desapilar(pila)
            apilar(pilaAux, x)
        else:
            apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

"""
4. Diseñar un algoritmo sencillo para invertir
    el contenido de una pila cualquiera.
"""

def invertirPila(pila):

    pilaAux = Pila()
    pilaAux2 = Pila()
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not(pilaVacia(pilaAux2)):
        apilar(pila, desapilar(pilaAux2))

"""
5. Obtener un algoritmo que determine si
    una cadena de caracteres es o no un palíndromo.
"""

def esPalindromo(palabra):

    pila = Pila()
    pilaAux = Pila()
    pilaAux2 = Pila()

    for i in range(0,len(palabra)):
        if not(pilaLlena(pila)):
            apilar(pila, palabra[i])

    for i in range(len(palabra)):
        if not(pilaLlena(pilaAux)):
            apilar(pilaAux, palabra[i])

    while not(pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not(pilaVacia(pila) and pilaVacia(pilaAux2)):
        if desapilar(pila) != desapilar(pilaAux2):
            return False
    return True

"""
6. Escribir un algoritmo para determinar si una hilera
    de caracteres de entrada es de la forma xCy,
    donde x es el inverso de y. Ej. mamaCamam.
"""

def xCy(palabra):

    pilaAux = Pila()
    pila = Pila()
    llenarPila(pila, palabra)

    while (cimaPila(pila) != "C"):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)

    while not(pilaVacia(pila) and pilaVacia(pilaAux)):
        if (desapilar(pila) != desapilar(pilaAux)):
            return False
    return True

"""
7. Leer una palabra y visualizarla en orden inverso.
"""

def invertirPalabra(palabra):

    palabrainversa = ""
    pila = Pila()
    llenarPila(pila, palabra)

    while not(pilaVacia(pila)):
        palabrainversa += desapilar(pila)

    return palabrainversa

"""
8. Escribir un segmento de programa que elimine
    el elemento justo debajo de la cima de la pila.
"""

def eliminarDebajoCima(pila):
    pilaAux = Pila()

    if not(pilaLlena(pilaAux)):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

"""
9. Escribir una función que obtenga el íesimo
    elemento a partir de la cima de una pila, sin borrarlo.
"""

def obtenerIesimoElemento(pila, numero):
    pilaAux = Pila()

    x = None
    if not(pilaVacia(pila)):
        for i in range(0, numero):
            x = desapilar(pila)
            apilar(pilaAux, x)

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return x
