# -*- coding: utf-8 -*-

from tp4.lista_doblemente_enlazada.lista_doble import ListaDoble

ejercicio = " Ejerccio "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Genere un algoritmo que permita visualizar una lista en forma inversa con operaciones basicas de Lista.")

datos = [2,1,3,4,5,6,7,8,9]
lista = ListaDoble()
lista.insertarElementos(datos)

print('\n' + "Lista original: ")
print(lista)
print()

print('\n' + "Lista inversa: ")
print(lista.toStringInversa())