from tp2.pila.pila import Pila
import tp2.pila.pila as p


ejercicio = " Ejercicio 1 "
print ('\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Realizar un subprograma que obtenga el número de copias de un determinado elemento en una pila dada.")

lista = [9,3,8,2,7,3,6,4,2,5]
pila = Pila()

#p.cargarPila(pila)

p.llenarPila(pila, lista)


print('\n' + "Pila: ")
p.verPila(pila)

buscado = 3

print('\n' + '\n' + "Elemento a encontrar: {}".format(buscado))
print('\n' + "Numero de veces que aparece el elemento '{}': {}".format(buscado, p.numeroDeCopiasElemento(pila, buscado)))

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 2 "
print ('\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Utilizando las operaciones sobre pilas, desarrollar un subprograma que permita eliminar de una pila de enteros todos los números impares.")

lista = [9,1,8,2,7,3,6,4,5,2]
pila = Pila()

#p.cargarPila(pila)

p.llenarPila(pila, lista)

print('\n' + "Pila original: ")
p.verPila(pila)

p.eliminarImpares(pila)

print ('\n' + '\n' + "Pila de numeros Pares: ")
p.verPila(pila)

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 3 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Haciendo uso de las operaciones sobre pilas, realizar un programa que permita cambiar todas las apariciones de un determinado elemento de la pila por otro dado.")

lista = [0,1,8,2,0,5,6,4,5,0]
pila = Pila()

#p.cargarPila(pila)

p.llenarPila(pila, lista)
print('\n' + "Pila original: ")
p.verPila(pila)

buscado = 0

print('\n' + '\n' + "Elemento a reemplazar: {}".format(buscado))

reemplazo = 3
print('\n' +  "Reemplazo: {}".format(reemplazo))

p.cambiarX(pila, buscado, reemplazo)

print('\n' + "Pila resultante: ")

p.verPila(pila)

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 4 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Diseñar un algoritmo sencillo para invertir el contenido de una pila cualquiera.")

lista = [0,1,8,2,0,5,6,4,5,0]
pila = Pila()
p.llenarPila(pila, lista)

#p.cargarPila(pila)

print('\n' + "Pila original: ")
p.verPila(pila)

p.invertirPila(pila)

print('\n' + '\n' + "Pila invertida: ")
p.verPila(pila)

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 5 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Obtener un algoritmo que determine si una cadena de caracteres es o no un palíndromo. ")

cadena = "anulalaluna"
print('\n' + "Cadena: {}".format(cadena))
pila = Pila()
p.llenarPila(pila, cadena)

print('\n' + "¿Es palindromo?: {}".format(p.esPalindromo(cadena)))

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 6 "
print ('\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Escribir un algoritmo para determinar si una hilera de caracteres de entrada es de la forma xCy, donde x es el inverso de y. Ej. mamaCamam.")

cadena = "anulaCaluna"
print('\n' + "Cadena: {}".format(cadena))
pila = Pila()
p.llenarPila(pila, cadena)

print('\n' + "¿Es de la forma xCy?: {}".format(p.xCy(cadena)))

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 7 "
print ('\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Leer una palabra y visualizarla en orden inverso.")

cadena = "visualizar al revés"
print('\n' + "Cadena: {}".format(cadena))
pila = Pila()
p.llenarPila(pila, cadena)

print('\n' + "Cadena en orden inverso: {}".format(p.invertirPalabra(cadena)))

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 8 "
print ('\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Escribir un segmento de programa que elimine el elemento justo debajo de la cima de la p.")

lista = [9,3,8,2,7,3,6,4,2,5]

pila = Pila()
p.llenarPila(pila, lista)

#p.cargarPila(pila)

print('\n' + "Pila original: ")
p.verPila(pila)

p.eliminarDebajoCima(pila)

print('\n' + '\n' + "Pila resultante: ")
p.verPila(pila)

#---------------------------------------------------------------------------

ejercicio = " Ejercicio 9 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Escribir una función que obtenga el íesimo elemento a partir de la cima de una pila, sin borrarlo.")

lista = [9,3,8,2,7,3,6,4,2,5]
pila = Pila()

#p.cargarPila(pila)

p.llenarPila(pila, lista)

elemento = 2
print('\n' + "Elemento a obtener: {}".format(elemento))

print('\n' + "Pila original: ")
p.verPila(pila)

print('\n' + '\n' + "Elemento: {}".format(p.obtenerIesimoElemento(pila, elemento)))


print('\n' + "Pila: ")
p.verPila(pila)