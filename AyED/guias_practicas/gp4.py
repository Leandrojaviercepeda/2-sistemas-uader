
from tp4.lista.lista import Lista
from tp4.lista.lista import Nodo
from tp4.lista.persona import Persona


ejercicio = " Ejerccio 2 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Dada una lista enlazada, cuyos nodos tienen la estructura (información, siguiente), diseñar un procedimiento que cuente el Nº de nodos de la lista. ")

#------------------------------------Ejercicio 2---------------------------------------

def cantidadNodos(lista):
    """
    Devuelve la cantidad de nodos de una lista enlazada.
    @param Lista()
    """
    return len(lista)

#---------------------------------------------------------------------------

lista2 = Lista()
datos2 = ["a", "b", "c", "d", "e", "f", "g", "h"]

lista2.insertarElementos(datos2)

print('\n' + "Lista: ")
print(lista2)

print('\n' + '\n' + "Cantidad de Nodos: {}".format(cantidadNodos(lista2)))

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 3"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escribir un programa tal que dada una lista de caracteres, borre de ella las vocales. ")

#------------------------------------Ejercicio 3---------------------------------------

def borrarVocales(lista):
    """
    Dada una lista de caracteres, borra de ella las vocales.
    @param Lista()
    """
    vocales = "aeiou"
    for vocal in vocales:
        lista.eliminar(vocal)

#---------------------------------------------------------------------------

lista3 = Lista()
datos3 = ["a", "b", "e", "d", "i", "f", "o", "h", "u"]

lista3.insertarElementos(datos3)

print('\n' + "Lista: ")
print(lista3)

borrarVocales(lista3)

print('\n' + '\n' + "Lista sin Vocales: ")
print(lista3)

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 4"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Dada una lista de enteros generar dos listas uno con Nºs impares y otra con los pares. ")

#------------------------------------Ejercicio 4---------------------------------------

def generarListasParesEImpares(lista):
    """
    Dada una lista de enteros, genera dos listas una con Nros impares y otra con Nros pares.
    @param Lista()
    """
    listaPares = Lista()
    listaImpares = Lista()

    for entero in lista:
        if entero % 2 == 0:
            listaPares.insertar(entero)
        else:
            listaImpares.insertar(entero)

    return listaPares, listaImpares

#---------------------------------------------------------------------------

datos4 = [1,2,3,4,5,6,7,8,9,10]

print('\n' + "Lista de enteros: ")
print(datos4)

listaPar = Lista()
listaImpar = Lista()

listaPar, listaImpar = generarListasParesEImpares(datos4)
print('\n' + "Lista Par: ")
print(listaPar)

print('\n' + '\n' + "Lista Impar: ")
print(listaImpar)


#---------------------------------------------------------------------------

ejercicio = " Ejerccio 5"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escribir un procedimiento que modifique el campo información de un nodo j-esimo de una lista enlazada.")

#------------------------------------Ejercicio 5---------------------------------------

def modificarInfoNodo(lista, nuevoDato, numeroNodo):
    """
    Modifica el campo información de un nodo j-esimo de una lista enlazada.
    @param Lista()
    """
    nodo = lista.cabecera
    contadorNodo = 1
    while ((nodo != None) and (contadorNodo != numeroNodo)):
        nodo = nodo.siguiente
        contadorNodo += 1

    if (nodo != None):
        nodo.info = nuevoDato
    else:
        return print("Nodo inexistente")

#---------------------------------------------------------------------------

lista5 = Lista()
datos5 = [1,2,3,4,5,6,7,8,9,10]

lista5.insertarElementos(datos5)

print('\n' + "Lista: ")
print(lista5)

#Modificamos el nodo 5 de la lista:
modificarInfoNodo(lista5, "A", 4)

print('\n' + '\n' + "Lista con nodo modificado: ")
print(lista5)

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 6"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Construir un procedimiento que realice una inserción inmediatamente antes del nodo i-esimo de una lista. (Buscar por campo). ")

#------------------------------------Ejercicio 6---------------------------------------

def insertarAntesDelIesimoNodo(lista, dato):
    """
    Realiza una inserción inmediatamente antes del nodo i-esimo de una lista.

    @param lista: lista enlazada tipo "Lista".
    @param dato: elemento a insertar.
    """

    lista.tamanio += 1
    nodo = Nodo()
    nodo.info = dato
    if cantidadNodos(lista) <= 2:
        nodo.siguiente = lista.cabecera
        lista.cabecera = nodo
    else:
        iesimo = None
        anterior = lista.cabecera
        actual = lista.cabecera.siguiente
        while (actual != None):
            iesimo = anterior
            anterior = anterior.siguiente
            actual = actual.siguiente
        iesimo.siguiente = nodo
        nodo.siguiente = anterior
        anterior.siguiente = actual


#---------------------------------------------------------------------------

lista6 = Lista()
datos6 = [1,2,3,4,5,6,7,8,9,10]

lista6.insertarElementos(datos6)

print('\n' + "Lista: ")
print(lista6)

dato = "Z"
print('\n' + '\n' +"Dato a insertar como anterior al iesimo elemento: \"{}\"".format(dato))

insertarAntesDelIesimoNodo(lista6, dato)

print('\n' + "Lista resultante: ")
print(lista6)

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 7"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Realizar un procedimiento que muestre los elementos de una lista de enteros y su suma.")

#------------------------------------Ejercicio 7---------------------------------------

def sumaLista(lista):
    """
    Muestra los elementos de una lista de enteros y su suma.

    @param lista: lista enlazada tipo "Lista".
    """
    nodo = lista.cabecera
    enteros = ""
    suma = 0
    while (nodo != None):
        enteros += str(nodo.info) + ", "
        suma += int(nodo.info)
        nodo = nodo.siguiente
    return(enteros[:-2], suma)

#---------------------------------------------------------------------------

lista7 = Lista()
datos7 = [1,2,3,4,5,6,7,8,9,10]

lista7.insertarElementos(datos7)

print('\n' + "Lista: ")
print(lista7)
enteros, suma = sumaLista(lista7)

print('\n' + "Enteros: {}. Suma: {}".format(enteros, suma))

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 8"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Construir una lista de registros con los siguientes campos (Nombre, edad, edo_civil, dirección), eliminar el nodo que contiene los datos de Roberto González.")

#------------------------------------Ejercicio 8---------------------------------------

lista8 = Lista()

for i in range (3):
    registro = Persona("Lean", "25", "Soltero", "Gualeguaychu")
    lista8.insertar(registro, 'nombre')

registro = Persona("Roberto Gonzalez", "27", "Casado", "Concepcion del Uruguay")
lista8.insertar(registro, 'nombre')

print('\n' + "Lista con Roberto Gonzalez: ")
print(lista8)
print ('\n' + '\n' + "--------------------")

registro = Persona("Roberto Gonzalez", "27", "Casado", "Concepcion del Uruguay")
lista8.eliminar(registro, 'nombre')


print('\n' + "Lista sin Roberto Gonzalez: ")
print(lista8)

#---------------------------------------------------------------------------

ejercicio = " Ejerccio 9"
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escriba un algoritmo que realice c/u de las sig. operaciones: a- Concatenar dos listas. b- Liberar todos los nodos de una lista. c- Formar una lista que contiene la intersección de los elementos de dos listas.")

#------------------------------------Ejercicio 9---------------------------------------

def conectarDosListas(lista1, lista2):
    """
    Realiza c/u de las sig. operaciones:
        a- Concatenar dos listas.
        b- Liberar todos los nodos de una lista.
        c- Formar una lista que contiene la intersección de los elementos de dos listas.

    @param lista1: lista enlazada tipo "Lista".
    @param lista2: lista enlazada tipo "Lista".
    """

    listaConcatenada = Lista()
    listaIntersectada = Lista()
    nodo = lista1.cabecera
    while nodo != None:
        listaConcatenada.insertar(nodo.info)
        nodo = nodo.siguiente

    nodo = lista2.cabecera
    while nodo != None:
       listaConcatenada.insertar(nodo.info)
       nodo = nodo.siguiente

    nodoL1 = lista1.cabecera
    nodoL2 = lista2.cabecera
    while nodoL1 != None and nodoL2 != None:
        listaIntersectada.append(nodoL1.info)
        listaIntersectada.append(lista2.eliminar(nodoL2.info))
        nodoL1 = nodoL1.siguiente
        nodoL2 = nodoL2.siguiente
    return (listaConcatenada, listaIntersectada)


#---------------------------------------------------------------------------

datos1 = ["1","2","3","4","5","6","7","8","9"]
datos2 = ["a","b","c","d","e","f","g","h","i"]
lista1 = Lista()
lista2 = Lista()

lista1.insertarElementos(datos1)
lista2.insertarElementos(datos2)

print('\n' + "Lista1: ")
print(lista1)
print('\n' + '\n' + "Lista2: ")
print(lista2)
listaConcatenada, listaIntersectada = conectarDosListas(lista1, lista2)

print('\n' + '\n' + "lista Concatenada: ")
print(listaConcatenada)

print('\n' + '\n' + "lista Intersectada: ")
print(listaIntersectada)

print('\n' + '\n' + "Lista intacta \"lista1\": ")
print(lista1)

print('\n' + '\n' + "Lista liberada \"lista2\": ")
print(lista2)
