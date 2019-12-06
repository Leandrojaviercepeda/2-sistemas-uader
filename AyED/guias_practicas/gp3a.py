from tp3.cola.cola import Cola
import tp3.cola.cola as c

from tp3.cola.cola import Pila
import tp3.cola.cola as p

#-----------------------------------------------------------------------------------

ejercicio = " Ejerccio 1 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Realizar dos operaciones, una para mostrar el contenido de una cola y otra para introducir una serie de elementos en ella.")


lista = [1,9,2,8,3,7,4,6,5,0]
cola = Cola()
#c.cargarCola()
c.llenarCola(cola, lista)
print('\n' + "Cola original: ")
c.mostrarCola(cola)

#-----------------------------------------------------------------------------------

ejercicio = " Ejerccio 2 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Utilizando las operaciones básicas de colas y pilas, escribir un algoritmo que invierta el contenido los elementos de una c.")

lista = [1,9,2,8,3,7,4,6,5,0]
cola = Cola()
c.llenarCola(cola, lista)
print('\n' + "Cola original: ")
c.mostrarCola(cola)

print('\n' + "Cola invertida: ")
c.invertirCola(cola)
c.mostrarCola(cola)

#-----------------------------------------------------------------------------------

ejercicio = " Ejerccio 3 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Escribir un programa que lea una cadena de caracteres, introduciendo cada carácter en una pila a medida que se lee y añadiéndolo simultáneamente a una c. Cuando se encuentra al final de la cadena, utilice las operaciones básicas de pilas y colas para determinar si la cadena es un palíndromo.")

cadena = "Cadena: 'arenera'"
print('\n' + cadena)
print()
print(c.esPalindromo(cadena))

#-----------------------------------------------------------------------------------

ejercicio = " Ejerccio 4 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))
print('\n' + "Usando los procedimientos y funciones que implementan las operaciones permitidas para pilas y colas; escriba los procedimientos que permitan efectuar las siguientes tareas: (Cuando escriba los procedimientos tenga en cuenta chequear apropiadamente si las estructuras están llenas o vacías cuando corresponda hacerlo.")

print("a) Mueva todos los elementos desde una pila hacia una c.")

lista = [1,9,2,8,3,7,4,6,5,0]
pila = Pila()
#cargarPila(pila)
p.llenarPila(pila, lista)
print('\n' + "Pila: ")
p.verPila(pila)

print('\n' + "Cola: ")
c.mostrarCola(c.pilaToCola(pila))

#-----------------------------------------------------------------------------------
print('\n' + '\n' + "b) Mueva todos los elementos desde una cola hacia una p.")

cola = Cola()
lista = [1,9,2,8,3,7,4,6,5,0]
#cargarCola(cola)
c.llenarCola(cola, lista)
print('\n' + "Cola: ")
c.mostrarCola(cola)

print('\n' + "Pila: ")
p.verPila(c.colaToPila(cola))

#-----------------------------------------------------------------------------------
print('\n' + '\n' + "c) Vacíe una pila sobre otra, de tal manera que los elementos agregados a la segunda mantengan el mismo orden relativo que tenían en la primera.")

lista = [1,9,2,8,3,7,4,6,5,0]
pila = Pila()
#cargarPila(pila)
p.llenarPila(pila, lista)
print('\n' + "Pila: ")
p.verPila(pila)

print('\n' + "Pila 2: ")
p.verPila(c.cambiarDePila(pila))

#-----------------------------------------------------------------------------------
print('\n' + '\n' + "d) Vacíe una pila sobre otra, de tal manera que los elementos agregados a la segunda estén ordenados al revés de lo que estaban en la pila original.")

lista = [1,9,2,8,3,7,4,6,5,0]
pila = Pila()
#cargarPila(pila)
p.llenarPila(pila, lista)
print('\n' + "Pila: ")
p.verPila(pila)

print('\n' + "Pila 2: ")
p.verPila(c.vaciarPilaSobreOtra(pila))

#-----------------------------------------------------------------------------------
print('\n' + '\n' + "e) Comience con una pila vacía y una cola vacía, use la pila para invertir el orden de todos los elementos de la c.")

cola = Cola()
lista = [1,9,2,8,3,7,4,6,5,0]
#cargarCola(cola)
c.llenarCola(cola, lista)
print('\n' + "Cola: ")
c.mostrarCola(cola)

c.pilaInvierteCola(cola)
print('\n' + "Cola: ")
c.mostrarCola(cola)

#-----------------------------------------------------------------------------------
print('\n' + '\n' + "f) Comience con una pila vacía y una cola vacía, use la cola para invertir el orden de todos los elementos de la p.")

#p.verPila(c.colaInviertePila())

#-----------------------------------------------------------------------------------

ejercicio = " Ejerccio 5 "
print ('\n' + '\n' + "---------- {} ----------".format(ejercicio))

print('\n' + "Escribir un programa que lea una cadena de caracteres, compuesta de dos partes separadas entre sí por dos puntos ‘:’." + '\n' + "Como resultado el programa deberá indicar cual de las siguientes condiciones se cumple en la cadena ingresada:")


print ('\n' + "m. No se encontraron dos puntos en la línea.")
print ('\n' + "n. La parte de la izquierda (antes de los dos puntos), es más larga que la de la derecha.")
print ('\n' + "o. La parte de la derecha (después de los dos puntos), es más larga que la de la izquierda.")

cadena = "cadena:dividida"
print('\n' + "Cadena: {}" .format(cadena))
colaizquierda = Cola()
coladerecha = Cola()
existedospuntos = None

colaizquierda, coladerecha, existedospuntos = c.dividirEnColas(cadena)

print('\n' + "Parte izquierda: ")
c.mostrarCola(colaizquierda)
print('\n' + '\n' + "Parte derecha: ")
c.mostrarCola(coladerecha)
print('\n' + '\n' + "Existen 'dos puntos': ")
print(existedospuntos)

#-----------------------------------------------------------------------------------

print('\n' + "p. Las partes derecha e izquierda tienen igual longitud pero son diferentes. ")

cadena = "cadena:cadena"
print('\n' + "Cadena: {}" .format(cadena))
print()
print(c.igualLongitud(cadena))

#-----------------------------------------------------------------------------------

print('\n' + "q. Las partes derecha e izquierda son exactamente iguales. Use una cola para mantener la parte izquierda de la línea mientras analiza la parte derecha.")

cadena = "cadena:cadena"
print('\n' + "Cadena: {}" .format(cadena))
print()
print(c.partesIguales(cadena))

