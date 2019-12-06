# -*- coding: utf-8 -*-
from tp6.arbol_avl.arbolAvl import ArbolAVL
import random

#lista = random.sample(range(0,100), 10)


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 1 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escribir un algoritmo que inserte en un árbol binario de búsqueda vacío los siguientes nodos: 3,1,4,6,9,2,7,5.")


# --------------------------------------------- ej1 ---------------------------------------------


def ejercicio1(arbol):  # Ejercicio 1
    """
    Inserta en un árbol binario de búsqueda vacío los siguientes nodos: 3,1,4,6,9,2,7,5.
    @param: ArbolAVL()
    """
    if type(arbol) == ArbolAVL:

        nodos = [3, 1, 4, 6, 9, 2, 7, 5]
        for nodo in nodos:
            arbol.insertar(nodo)

    return "Error de tipo de dato"


# -----------------------------------------------------------------------------------------------------

arbol = ArbolAVL()

ejercicio1(arbol)

print("\nArbol: ")

arbol.printArbol()


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 2 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Realizar dos algoritmos, el primero que devuelva el hijo derecho de un nodo\
      y el segundo, el izquierdo." + '\n')

# --------------------------------------------- ej2 a ---------------------------------------------


def obtenerHijoDerecho(arbol, valor):  # Ejercicio 2a
    """
    Devuelve el hijo derecho de un nodo.
    @param ArbolAVL()
    @param Valor
    """
    existeNodo = arbol.encontrar(valor)

    if existeNodo:
        hijoDerecho = existeNodo.hijo_derecho

    return hijoDerecho


# --------------------------------------------- ej2 b -------------------------------------------------


def obtenerHijoIzquierdo(arbol, valor):  # Ejercicio 2b
    """
    Devuelve el hijo izquierdo de un nodo.
    @param ArbolAVL()
    @param Valor
    """
    existeNodo = arbol.encontrar(valor)

    if existeNodo:
        hijoIzquierdo = existeNodo.hijo_izquierdo

    return hijoIzquierdo


# -----------------------------------------------------------------------------------------------------

arbol2 = ArbolAVL()
elementos2 = ["c", "d", "e", "s", "g", "b", "a"]
arbol2.insertarElementos(elementos2)

print("\nArbol: \n")
arbol2.printArbol()

nodoDerecho = obtenerHijoDerecho(arbol2, "g")
print("\nHijo derecho: ", nodoDerecho)

nodoIzquierdo = obtenerHijoIzquierdo(arbol2, "d")
print("\nHijo izquierdo: ", nodoIzquierdo)


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 4 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Construir dos algoritmos para calcular el máximo y mínimo elemento de un árbol binario de búsqueda." + '\n')


# --------------------------------------------- ej4 a -------------------------------------------------


def elementoMaximo(arbol):  # Ejercicio 4a
    """
    Devuelve el elemento maximo de un arbol.
    @param ArbolAVL()
    """
    nodo_actual = arbol.raiz
    elementoMaximo = nodo_actual.clave

    while nodo_actual:

        if elementoMaximo < nodo_actual.clave:
            elementoMaximo = nodo_actual.clave

        nodo_actual = nodo_actual.hijo_derecho

    return elementoMaximo


# --------------------------------------------- ej4 b -------------------------------------------------


def elementoMinimo(arbol):  # Ejercicio 4a
    """
    Devuelve el elemento minimo de un arbol.
    @param ArbolAVL()
    """
    nodo_actual = arbol.raiz
    elementoMinimo = nodo_actual.clave

    while nodo_actual:

        if elementoMinimo > nodo_actual.clave:
            elementoMinimo = nodo_actual.clave

        nodo_actual = nodo_actual.hijo_izquierdo

    return elementoMinimo


# -----------------------------------------------------------------------------------------------------

arbol4 = ArbolAVL()
elementos4 = random.sample(range(0, 100), 10)

arbol4.insertarElementos(elementos4)
print("\nArbol: \n")
arbol4.printArbol()

print("\nElemento maximo: ", elementoMaximo(arbol4))
print("\nElemento minimo: ", elementoMinimo(arbol4))


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 5 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print(
    '\n' + "Construir los algoritmos pre-orden, post-orden e in-orden para recorrer el siguiente árbol binario: ['A', 'B', 'F', 'G', 'C', 'D', 'E']" + '\n')


# --------------------------------------------- ej5 a -------------------------------------------------


def preOrden(arbol):
    """
    Imprime el arbol en preOrden: raiz - izquierda - derecha
    @param ArbolAVL()
    """

    def _preOrden(nodo):

        stringArbol = ""
        if nodo:
            stringArbol += " {},".format(str(nodo))
            stringArbol += _preOrden(nodo.hijo_izquierdo)
            stringArbol += _preOrden(nodo.hijo_derecho)

        return stringArbol

    stringPreOrden = "( %s )" % (_preOrden(arbol.raiz)[1:-1])
    return stringPreOrden

# --------------------------------------------- ej5 b -------------------------------------------------


def postOrden(arbol):
    """
    Imprime el arbol en postOrden: izquierda - derecha - raiz
    @param ArbolAVL()
    """
    def _postOrden(nodo):

        stringArbol = ""
        if nodo:
            stringArbol += _postOrden(nodo.hijo_izquierdo)
            stringArbol += _postOrden(nodo.hijo_derecho)
            stringArbol += " {},".format(str(nodo))

        return stringArbol

    stringPostOrden = "( %s )" % (_postOrden(arbol.raiz)[1:-1])
    return stringPostOrden

# --------------------------------------------- ej5 c -------------------------------------------------


def inOrden(arbol):
    """
    Imprime el arbol en inOrden: izquierda - raiz - derecha
    @param ArbolAVL()
    """
    def _inOrden(nodo):

        stringArbol = ""
        if nodo:
            stringArbol += _inOrden(nodo.hijo_izquierdo)
            stringArbol += " {},".format(str(nodo))
            stringArbol += _inOrden(nodo.hijo_derecho)

        return stringArbol

    stringInOrden = "( %s )" % (_inOrden(arbol.raiz)[1:-1])
    return stringInOrden


# -----------------------------------------------------------------------------------------------------

elementos5 = ["A", "B", "F", "G", "C", "D", "E"]
arbol5 = ArbolAVL()
arbol5.insertarElementos(elementos5)

print("\nArbol: ")
arbol5.printArbol()

print("\nPreOrden: ", preOrden(arbol5))

print("\nPostOrden: ", postOrden(arbol5))

print("\nInOrden: ", inOrden(arbol5))


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 6 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Recorrer en los tres modos el siguiente árbol: ['*', '+', 'A', 'C', 'B']" + '\n')


# -----------------------------------------------------------------------------------------------------


elementos6 = ["*", "+", "A", "C", "B"]
arbol6 = ArbolAVL()
arbol6.insertarElementos(elementos6)

print("\nArbol: ")
arbol6.printArbol()

print("\nPreOrden: ", preOrden(arbol6))

print("\nPostOrden: ", postOrden(arbol6))

print("\nInOrden: ", inOrden(arbol6))


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 7 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escribir procedimientos tal que dado un árbol binario, calcule: a- el número de nodos del árbol. b- el número de hojas del árbol. c- la altura del árbol." + '\n')


# --------------------------------------------- ej7 a -------------------------------------------------


def cantidadNodos(arbol):
    """
    Devuelve la cantidad de nodos del Arbol
    @param ArbolAVL()
    """
    def _cantidadNodos(nodo, pila):
        if nodo:
            pila.append(1)
            _cantidadNodos(nodo.hijo_izquierdo, pila)
            _cantidadNodos(nodo.hijo_derecho, pila)

    nodo_actual = arbol.raiz
    numeroNodos = []
    _cantidadNodos(nodo_actual, numeroNodos)
    return len(numeroNodos)


# --------------------------------------------- ej7 b -------------------------------------------------


def cantidadHojas(arbol):
    """
    Devuelve la cantidad de nodos hoja del Arbol
    @param ArbolAVL()
    """
    def _cantidadNodos(nodo, pila):
        if nodo:

            if nodo.esHoja():
                pila.append(1)

            _cantidadNodos(nodo.hijo_izquierdo, pila)
            _cantidadNodos(nodo.hijo_derecho, pila)

    nodo_actual = arbol.raiz
    numeroNodos = []
    _cantidadNodos(nodo_actual, numeroNodos)
    return len(numeroNodos)


# --------------------------------------------- ej7 c -------------------------------------------------


def altura(arbol):
    """
    Devuelve la altura del Arbol
    @param ArbolAVL()
    """
    return arbol.altura()


# -----------------------------------------------------------------------------------------------------


arbol7 = ArbolAVL()
elementos7 = random.sample(range(0, 100), 10)

arbol7.insertarElementos(elementos7)
print("\nArbol: \n")
arbol7.printArbol()

print("\nNumero de nodos: ", cantidadNodos(arbol7))

print(arbol7)
print("\nNumero de nodos hoja: ", cantidadHojas(arbol7))

print("\nAltura del arbol: ", altura(arbol7))


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 8 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Se dispone de un árbol binario de elementos tipo integer. Escribir funciones que calculen: a- la suma de sus elementos. b- la suma de sus elementos que son múltiplos de 3." + '\n')


# --------------------------------------------- ej8 a -------------------------------------------------


def calcularSuma(arbol):
    """
    Calcula la suma de los elementos del Arbol
    @param ArbolAVL()
    """
    def _calcularSuma(nodo):
        suma = 0
        if nodo and type(nodo.clave) is int:
            suma += _calcularSuma(nodo.hijo_izquierdo)
            suma += nodo.clave
            suma += _calcularSuma(nodo.hijo_derecho)

        return suma
    return _calcularSuma(arbol.raiz)


# --------------------------------------------- ej8 b -------------------------------------------------


def calcularSumaMultiplosDe3(arbol):
    """
    Calcula la suma de los elementos del Arbol
    @param ArbolAVL()
    """

    def esMultiplo(valor, multiple):
        """
        Calcular si el numero es multiplo
        """
        resto = valor % multiple
        if resto == 0:
            return True
        return False

    def sumar(stack):
        resultado = 0
        for numero in stack:
            resultado += numero
        return resultado

    def _calcularSuma(nodo, stack):

        if nodo and type(nodo.clave) is int:

            if esMultiplo(nodo.clave, 3):
                stack.append(nodo.clave)

            _calcularSuma(nodo.hijo_izquierdo, stack)
            _calcularSuma(nodo.hijo_derecho, stack)

        return stack

    pila = []
    sumaMultiplosDe3 = sumar(_calcularSuma(arbol.raiz, pila))
    
    return sumaMultiplosDe3


# -----------------------------------------------------------------------------------------------------


arbol8 = ArbolAVL()
elementos8 = [3, 6, 20, 9, 5, 23, 25]

arbol8.insertarElementos(elementos8)
print("\nArbol: \n")
arbol8.printArbol()

print("\nSuma: ", calcularSuma(arbol8))

print("\nSuma multiplos de '3': ", calcularSumaMultiplosDe3(arbol8))


# -----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 9 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Construir un algoritmo tal que elimine un nodo c de un árbol binario. Considerar los tres casos. (nodo c no se encuentra, nodo c tiene 0 o un subárbol, nodo de clave c tiene dos subárboles)." + '\n')


# --------------------------------------------- ej9 a -------------------------------------------------


def eliminar(arbol, clave):
    """
    Elimina un nodo de un Arbol teniendo en cuenta los siguientes casos:
        a- El nodo no esta en el arbol.
        b- El nodo tiene 0 o un hijo.
        c- El nodo tiene ambos hijos.
    @param: ArbolAVL()
    @param: Clave en el arbol.
    """
    arbol.borrar_clave(clave)


# -----------------------------------------------------------------------------------------------------

arbol9 = ArbolAVL()
elementos9 = [10, 9, 8, 5, 4, 3, 13, 15, 14]

arbol9.insertarElementos(elementos9)
print("\nArbol: \n")
arbol9.printArbol()
print(arbol9)

print("\n")

print("------------------------------------------------------------------------------------")
print("\nIntentando eliminar una clave que no se encuentra en el Arbol: \n")
clave = 1
print("\nClave a eliminar: {}".format(clave))
eliminar(arbol9, 1)
print("\n")
arbol9.printArbol()
print(arbol9)


print("------------------------------------------------------------------------------------")
print("\nEliminando nodo con 0 Hijos del Arbol: \n")
clave = 8
print("\nClave a eliminar: {}".format(clave))
eliminar(arbol9, clave)
print("\n")
arbol9.printArbol()
print(arbol9)

print("------------------------------------------------------------------------------------")
print("\nEliminando nodo con 1 Hijos del Arbol: \n")
clave = 9
print("\nClave a eliminar: {}".format(clave))
eliminar(arbol9, clave)
print("\n")
arbol9.printArbol()
print(arbol9)

print("------------------------------------------------------------------------------------")
print("\nEliminando nodo con 2 Hijos del Arbol: \n")
clave = 13
print("\nClave a eliminar: {}".format(clave))
eliminar(arbol9, clave)
print("\n")
arbol9.printArbol()
print(arbol9)

print("------------------------------------------------------------------------------------")
print("\nEliminando nodo raiz del Arbol: \n")
clave = 5
print("\nClave a eliminar: {}".format(clave))
eliminar(arbol9, clave)
print("\n")
arbol9.printArbol()
print(arbol9)


#-----------------------------------------------------------------------------------------------------


ejercicio = " Ejerccio 11 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Realizar una función tal que dado un nivel de un árbol binario, devuelva el número de nodos de ese nivel." + '\n')


#--------------------------------------------- ej11 a -------------------------------------------------





#-----------------------------------------------------------------------------------------------------

arbol11 = ArbolAVL()
elementos11 = [10, 9, 8, 5, 4, 3, 13, 15, 14]

arbol11.insertarElementos(elementos11)
print("\nArbol: \n")
arbol11.printArbol()
print(arbol11)



#-----------------------------------------------------------------------------------------------------
