#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pila as p

class Nodo():
    def __init__(self):
        self.info = None
        self.sig = None

class Cola:

    def __init__(self):
        self.tamanio = 0
        self.frente = None
        self.final = None

        
def colaLlena(cola):
    return False

def colaVacia(cola):
    return cola.tamanio == 0

def tamanioCola(cola):
    return cola.tamanio

def encolar(cola, x):
    nodo = Nodo()
    nodo.info = x
    nodo.sig = None
    if cola.final == None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1    
    
def desencolar(cola):
    x = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente == None:
        cola.final = None
    cola.tamanio -= 1
    return x

"""
Realizar dos operaciones, una para mostrar el contenido de una cola
    y otra para introducir una serie de elementos en ella.
"""

def llenarCola(cola, lista):
    if not(colaLlena(cola)):
        for i in range(len(lista)):
            encolar(cola, lista[i])

def cargarCola(cola):
    print("Carga de elementos")
    n = "S"
    while not(colaLlena(cola)) and n == "S":
        x = input("Introduzca un elemento: ")
        encolar(cola, x)
        n = input("'S' para continuar: ")
        n.upper()


def mostrarCola(cola):
    colaAux = Cola()
    n = 0
    while not(colaVacia(cola)) and n <= tamanioCola(cola)-1:
        x = desencolar(cola)
        print (x + ", ")
        encolar(colaAux, x)
        encolar(cola, desencolar(colaAux))
        n += 1

def verCola(cola):
    n = tamanioCola(cola)
    for i in range(0, n):
        x = desencolar(cola)
        print(x + ", ")
        encolar(cola, x)


"""
Utilizando las operaciones básicas de colas y pilas,
    escribir un algoritmo que invierta el contenido los elementos de una cola.
"""

def invertirCola(cola):
    pila = p.Pila()

    while not(colaVacia(cola)):
        p.apilar(pila, desencolar(cola))

    while not(p.pilaVacia(pila)):
        encolar(cola, p.desapilar(pila))

"""
Escribir un programa que lea una cadena de caracteres,
    introduciendo cada carácter en una pila a medida que se lee
    y añadiéndolo simultáneamente a una cola.
    cuando se encuentra al final de la cadena,
    utilice las operaciones básicas de pilas
    y colas para determinar si la cadena es un palíndromo.
"""

def esPalindromo(cadena):
    pila = p.Pila()
    cola = Cola()

    for i in range(len(cadena)):
        p.apilar(pila, cadena[i])
        encolar(cola, cadena[i])

    while not(colaVacia(cola) and p.pilaVacia(pila)):
        if desencolar(cola) != p.desapilar(pila):
            return False
    return True

"""
Usando los procedimientos y funciones que implementan
    las operaciones permitidas para pilas y colas;
    escriba los procedimientos que permitan efectuar las siguientes tareas:
    (Cuando escriba los procedimientos tenga en cuenta chequear apropiadamente
     si las estructuras están llenas o vacías cuando corresponda hacerlo).
"""
#a) Mueva todos los elementos desde una pila hacia una cola.
 
pila = p.Pila()
lista = [1,2,3,4,5]
p.llenarPila(pila, lista)

def pilaToCola(pila):
    cola = Cola()
    while not(p.pilaVacia(pila)):
        if not(colaLlena(cola)):
            encolar(cola, p.desapilar(pila))
    return cola        
        
#b) Mueva todos los elementos desde una cola hacia una pila.

def colaToPila(cola):
    pila = p.Pila()
    
    while not(colaVacia(cola)):
        if not(p.pilaLlena(pila)):
            p.apilar(pila, desencolar(cola))
    return pila

#c) Vacíe una pila sobre otra, de tal manera que los elementos
#   agregados a la segunda mantengan el mismo orden relativo que tenían en la primera.


def cambiarDePila(pila):
    
    pilaAux = p.Pila()
    p.invertirPila(pila)
    
    while not(p.pilaVacia(pila)):
        p.apilar(pilaAux, p.desapilar(pila))
    return pilaAux    

#d) Vacíe una pila sobre otra, de tal manera que los elementos
#   agregados a la segunda estén ordenados al revés de lo que estaban en la pila original.

def vaciarPilaSobreOtra(pila):
    pilaAux = p.Pila()
    
    while not(p.pilaVacia(pila)):
        p.apilar(pilaAux, p.desapilar(pila))   
    return pilaAux
        
#e) Comience con una pila vacía y una cola vacía,
#   use la pila para invertir el orden de todos los elementos de la cola.
    
def pilaInvierteCola(cola):
    
    pila = p.Pila()
    #cargarCola(cola)
    
    while not(colaVacia(cola)):
        p.apilar(pila, desencolar(cola))
        
    while not(p.pilaVacia(pila)):
        encolar(cola, p.desapilar(pila))

#f) Comience con una pila vacía y una cola vacía,
#   use la cola para invertir el orden de todos los elementos de la pila.

def colaInviertePila():
    
    pila = p.Pila()
    cola = Cola()
    p.cargarPila(pila)
    
    while not(p.pilaVacia(pila)):
        if not(colaLlena(cola)):
            encolar(cola, p.desapilar(pila))

    while not(colaVacia(cola)):
        if not(p.pilaLlena(pila)):
            p.apilar(pila, desencolar(cola))
    
    return (pila)

"""
Escribir un programa que lea una cadena de caracteres, 
    compuesta de dos partes separadas entre sí por dos puntos ‘:’. 
    Como resultado el programa deberá indicar cual de las siguientes 
    condiciones se cumple en la cadena ingresada:
"""

#m. No se encontraron dos puntos en la línea. 
#n. La parte de la izquierda (antes de los dos puntos), 
#   es más larga que la de la derecha. 
#o. La parte de la derecha (después de los dos puntos), 
#   es más larga que la de la izquierda. 

def dividirEnColas(cadena):
    colaIzquierda = Cola()
    colaDerecha = Cola()
    exisiteDosPuntos = False
    
    for caracter in cadena:
        if (str(caracter) == ":"):
            exisiteDosPuntos = True
        elif exisiteDosPuntos:
            encolar(colaDerecha, caracter)
        else:
            encolar(colaIzquierda, caracter)
    
    return colaIzquierda, colaDerecha, exisiteDosPuntos
    
#p. Las partes derecha e izquierda tienen igual longitud pero son diferentes. 

def igualLongitud(cadena):
    colaIzquierda = Cola()
    colaDerecha = Cola()
    exisiteDosPuntos = None
    colaIzquierda, colaDerecha, exisiteDosPuntos = dividirEnColas(cadena)
    
    salida = None
    
    if (tamanioCola(colaDerecha) == tamanioCola(colaIzquierda)):
        salida = True
    
    if (desencolar(colaIzquierda) != (desencolar(colaDerecha))):
        salida = True
    else:
        salida = False
    
    return salida

        
#q. Las partes derecha e izquierda son exactamente iguales. 
#   Use una cola para mantener la parte izquierda de la línea 
#   mientras analiza la parte derecha.
    
def partesIguales(cadena):
    colaIzquierda = Cola()
    colaDerecha = Cola()
    exisiteDosPuntos = None
    colaIzquierda, colaDerecha, exisiteDosPuntos = dividirEnColas(cadena)
    
    while not(colaVacia(colaIzquierda) and colaVacia(colaDerecha)):
        if (desencolar(colaIzquierda) != desencolar(colaDerecha)):
            return False
    return True    # -*- coding: utf-8 -*-

