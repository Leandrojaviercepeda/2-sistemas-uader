"""Realizar un programa que permita generar una lista randomicamente de aproximadamente 2000.
Mostrar la lista.
Llamar a QS para ordenar la lista.
Mostrar lista ordenada.
Busqueda binaria recursiva."""

import funciones as fn
import random

nombreArchivo = "ListaRandomica"

tamañoArchivo = 50
lista = random.sample(range(100,200), tamañoArchivo)

def listarArchivo(A):  
    for i in range(0, len(A)):
        num = fn.leerArchivo(A, i)
        print(num, end = ", ")
            
def generarArchivo(A):
    for i in range(tamañoArchivo):
        fn.agregarDato(A,lista[i])
    

archivo = fn.abrirArchivo(nombreArchivo)

fn.borrarArchivo(archivo)


generarArchivo(archivo)

print ("\n", "Lista randomica desordenada de numeros: ")
listarArchivo(archivo)

fn.qsArchivo(archivo,0,len(archivo)-1)
print ("\n", "Lista randomica ordenada de numeros: ")
listarArchivo(archivo)

print("\n", "Buscado:",fn.bbArchivo(archivo,0,len(archivo)-1,150))

fn.cerrarArchivo(archivo)
