
maximo = 10

class Cola:

    def __init__(self):
        self.tamanio = 0
        self.frente = 0
        self.final = -1
        self.estructura = []
        for i in range(0, maximo):
            self.estructura.append(None)


def colaLlena(cola):
    """ Efecto: devuelve "true" si la cola está llena, "false" si no está llena.

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    return (cola.tamanio == maximo)


def colaVacia(cola):
    """ Efecto: devuelve "true" si la cola está vacia, "false" si no está vacia.

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    return(cola.tamanio == 0)


def tamanioCola(cola):
    """ Efecto: devuelve la cantidad de elementos de la "Cola".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    return cola.tamanio

def encolar(cola, x):
    """ Efecto: inserta un elemento al final de la "Cola".

        Parámetros:
        cola -- tipo "Cola()"
        x -- elemento a ser encolado.

        Excepciones:
    """
    if cola.final == maximo -1:
        cola.final = 0
    else:
        cola.final += 1
    cola.estructura[cola.final] = x
    cola.tamanio += 1

def desencolar(cola):
    """ Efecto: elimina el elemento situado al frente de la "Cola".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    x = cola.estructura[cola.frente]
    if cola.frente == maximo -1:
        cola.frente = 0
    else:
        cola.frente += 1
    cola.tamanio -= 1
    return x


def llenarCola(cola, lista):
    """ Efecto: introduce una serie de elementos en la "Cola".

        Parámetros:
        cola -- tipo "Cola()"
        lista -- array de datos de cualquier tipo.

        Excepciones:
    """
    if not(colaLlena(cola)):
        for i in range(len(lista)):
            encolar(cola, lista[i])

def cargarCola(cola):
    """ Efecto: le permite al usuario introducir una serie de elementos en la "Cola".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    print("Carga de elementos")
    n = "S"
    while not(colaLlena(cola)) and n == "S":
        x = input("Introduzca un elemento: ")
        encolar(cola, x)
        n = input("'S' para continuar: ")
        n.upper()


def mostrarCola(cola):
    """ Efecto: muestra el contenido de una "Cola".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    colaAux = Cola()
    n = 0
    while not(colaVacia(cola)) and n <= tamanioCola(cola)-1:
        x = desencolar(cola)
        print(x, end=", ")
        encolar(colaAux, x)
        encolar(cola, desencolar(colaAux))
        n += 1


def invertirCola(cola):
    """ Efecto: invierte el contenido de una "Cola".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    pila = Pila()

    while not(pilaLlena(pila)):
        apilar(pila, desencolar(cola))

    while not(colaLlena(cola)):
        encolar(cola, desapilar(pila))


def esPalindromo(cadena):
    """ Efecto: determina si la cadena es un palíndromo.

        Parámetros:
        cadena -- cadena de datos

        Excepciones:
    """
    pila = Pila()
    cola = Cola()

    for i in range(len(cadena)):
        apilar(pila, cadena[i])
        encolar(cola, cadena[i])

    while not(colaVacia(cola) and pilaVacia(pila)):
        if desencolar(cola) != desapilar(pila):
            return False
    return True


def pilaToCola(pila):
    """ Efecto: Mueva todos los elementos desde una "Pila" hacia una "Cola".

        Parámetros:
        pila -- tipo "TPila()"

        Excepciones:
    """
    cola = Cola()
    while not(pilaVacia(pila)):
        if not(colaLlena(cola)):
            encolar(cola, desapilar(pila))
    return cola


def colaToPila(cola):
    """ Efecto: Mueva todos los elementos desde una "Cola" hacia una "Pila".

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    pila = Pila()

    while not(colaVacia(cola)):
        if not(pilaLlena(pila)):
            apilar(pila, desencolar(cola))
    return pila


def cambiarDePila(pila):
    """ Efecto: Vacía una pila sobre otra, de tal manera que los elementos agregados a la segunda mantienen el mismo orden relativo que tenían en la primera.

        Parámetros:
        pila -- tipo "TPila()"

        Excepciones:
    """
    pilaAux = Pila()
    invertirPila(pila)

    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))
    return pilaAux


def vaciarPilaSobreOtra(pila):
    """ Efecto: Vacía una pila sobre otra, de tal manera que los elementos agregados a la segunda estan ordenados al revés de lo que estaban en la pila original.

        Parámetros:
        pila -- tipo "TPila()"

        Excepciones:
    """
    pilaAux = Pila()

    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))
    return pilaAux


def pilaInvierteCola(cola):
    """ Efecto: usa una pila para invertir el orden de todos los elementos de la cola.

        Parámetros:
        cola -- tipo "Cola()"

        Excepciones:
    """
    pila = Pila()
    #cargarCola(cola)

    while not(colaVacia(cola)):
        apilar(pila, desencolar(cola))

    while not(pilaVacia(pila)):
        encolar(cola, desapilar(pila))


def colaInviertePila(pila):
    """ Efecto: use una cola para invertir el orden de todos los elementos de la 

        Parámetros:
        pila -- tipo "TPila()"

        Excepciones:
    """
    cola = Cola()
    #cargarPila(pila)

    while not(pilaVacia(pila)):
        if not(colaLlena(cola)):
            encolar(cola, desapilar(pila))

    while not(colaVacia(cola)):
        if not(pilaLlena(pila)):
            apilar(pila, desencolar(cola))

    return (pila)


def dividirEnColas(cadena):
    """ Efecto: lee una cadena de caracteres, compuesta de dos partes separadas entre sí por dos puntos ‘:’.
        Como resultado el programa deberá indicar cual de las siguientes condiciones se cumple en la cadena ingresada:
        
        No se encontraron dos puntos en la línea. 
        La parte de la izquierda (antes de los dos puntos), es más larga que la de la derecha. 
        La parte de la derecha (después de los dos puntos), es más larga que la de la izquierda.
        
        Parámetros:
        cadena -- cadena de datos
        
        Excepciones:
    """
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
    

def igualLongitud(cadena):
    """ Efecto: lee una cadena de caracteres, compuesta de dos partes separadas entre sí por dos puntos ‘:’.
        Como resultado el programa deberá indicar cual de las siguientes condiciones se cumple en la cadena ingresada:
        
        Las partes derecha e izquierda tienen igual longitud pero son diferentes. 
        
        Parámetros:
        cadena -- cadena de datos
        
        Excepciones:
    """
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

    
def partesIguales(cadena):
    """ Efecto: lee una cadena de caracteres, compuesta de dos partes separadas entre sí por dos puntos ‘:’.
        Como resultado el programa deberá indicar cual de las siguientes condiciones se cumple en la cadena ingresada:
        
        Las partes derecha e izquierda son exactamente iguales. 
        
        Parámetros:
        cadena -- cadena de datos
        
        Excepciones:
    """
    colaIzquierda = Cola()
    colaDerecha = Cola()
    exisiteDosPuntos = None
    colaIzquierda, colaDerecha, exisiteDosPuntos = dividirEnColas(cadena)
    
    while not(colaVacia(colaIzquierda) and colaVacia(colaDerecha)):
        if desencolar(colaIzquierda) != desencolar(colaDerecha):
            return False
    return True


maximo = 20


class Pila:

    def __init__(self):
        self.tope = 0
        self.estructura = []
        for i in range(0, maximo):
            self.estructura.append(None)


# (Devuelve true si la pila está llena, false si no está llena)
def pilaLlena(pila):
    return (maximo == pila.tope)


# (Apila un elemento en el ultimo lugar de la pila)
def apilar(pila, x):
    pila.estructura[pila.tope] = x
    pila.tope += 1


# (Desapila el ultimo elemento de la pila)
def desapilar(pila):
    pila.tope -= 1
    x = pila.estructura[pila.tope]
    return x


# (determina si una pila es no vacía)
def pilaVacia(pila):
    return (pila.tope == 0)


# (devuelve el ultimo elemento insertado en la pila)
def cimaPila(pila):
    return pila.estructura[pila.tope - 1]


def cargarPila(pila):
    print("Carga de elementos")
    n = "S"
    while not (pilaLlena(pila)) and n == "S":
        x = input("Introduzca un elemento: ")
        apilar(pila, x)
        n = input("'S' para continuar: ").upper()


# (muestra el contenido de la pila)
def verPila(pila):
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        x = desapilar(pilaAux)
        print(x, end=", ")
        apilar(pila, x)


# (Dada una lista de elementos los introduce una pila)
def llenarPila(pila, lista):
    for i in range(len(lista)):
        if not (pilaLlena(pila)):
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

    while not (pilaVacia(pila)):
        x = desapilar(pila)
        if (x == buscado):
            repeticiones += 1
        apilar(pilaAux, x)

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return repeticiones


"""
2. Utilizando las operaciones sobre pilas,
desarrollar un subprograma que permita eliminar
de una pila de enteros todos los números impares.
"""


def eliminarImpares(pila):
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pilaAux, x)

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


"""
3. Haciendo uso de las operaciones sobre pilas,
realizar un programa que permita cambiar todas
las apariciones de un determinado x de
la pila por otro dado.
"""


def cambiarX(pila, buscado, x):
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        if (cimaPila(pila) == buscado):
            desapilar(pila)
            apilar(pilaAux, x)
        else:
            apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


"""
4. Diseñar un algoritmo sencillo para invertir
el contenido de una pila cualquiera.
"""


def invertirPila(pila):
    pilaAux = Pila()
    pilaAux2 = Pila()
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not (pilaVacia(pilaAux2)):
        apilar(pila, desapilar(pilaAux2))


"""
5. Obtener un algoritmo que determine si
una cadena de caracteres es o no un palíndromo.
"""


def esPalindromo(palabra):
    pila = Pila()
    pilaAux = Pila()
    pilaAux2 = Pila()

    for i in range(len(palabra)):
        if not (pilaLlena(pila)):
            apilar(pila, palabra[i])

    for i in range(len(palabra)):
        if not (pilaLlena(pilaAux)):
            apilar(pilaAux, palabra[i])

    while not (pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not (pilaVacia(pila) and pilaVacia(pilaAux2)):
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

    while not (pilaVacia(pila) and pilaVacia(pilaAux)):
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

    while not (pilaVacia(pila)):
        palabrainversa += desapilar(pila)

    return palabrainversa


"""
8. Escribir un segmento de programa que elimine
el elemento justo debajo de la cima de la pila.
"""


def eliminarDebajoCima(pila):
    pilaAux = Pila()

    if not (pilaLlena(pilaAux)):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


"""
9. Escribir una función que obtenga el íesimo
elemento a partir de la cima de una pila, sin borrarlo.
"""


def obtenerIesimoElemento(pila, numero):
    x = None
    if not (pilaVacia(pila)):
        for i in range(0, numero):
            x = desapilar(pila)

    return x


#-----------------------------------------------------------------------------------------------------------------------


maximo = 30


class Pila:

    def __init__(self):
        self.tope = 0
        self.estructura = []
        for i in range(0, maximo):
            self.estructura.append(None)


def pilaLlena(pila):
    """ Devuelve true si la pila está llena, false si no está llena.

    Args:
        pila -- tipo "Pila()"
    """
    return (maximo == pila.tope)


def apilar(pila, x):
    """Apila un elemento en el ultimo lugar de la pila.

        Args:
            pila -- tipo "Pila()"
    """
    pila.estructura[pila.tope] = x
    pila.tope += 1


def desapilar(pila):
    """ Desapila el ultimo elemento de la pila.

        Args:
            pila -- tipo "Pila()"
    """
    pila.tope -= 1
    x = pila.estructura[pila.tope]
    return x


def pilaVacia(pila):
    """ Determina si una pila es no vacía.

        Args:
            pila -- tipo "Pila()"
    """
    return (pila.tope == 0)


def cimaPila(pila):
    """ Devuelve el ultimo elemento insertado en la pila.

        Args:
            pila -- tipo "Pila()"
    """
    return pila.estructura[pila.tope - 1]


def cargarPila(pila):
    """ Permite al usuario cargar elementos mientras lo desee.

        Args:
            pila -- tipo "Pila()"
    """
    print("Carga de elementos")
    n = "S"
    while not (pilaLlena(pila)) and n == "S":
        x = input("Introduzca un elemento: ")
        apilar(pila, x)
        n = input("'S' para continuar: ")
        n.upper()


def verPila(pila):
    """ Muestra el contenido de la pila.

        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        x = desapilar(pilaAux)
        print(x, end=", ")
        apilar(pila, x)


def llenarPila(pila, lista):
    """ Dado un array de datos los introduce una pila.

        Args:
            pila -- tipo "Pila()"
            lista -- array["cualquier tipo"]
    """
    for i in range(len(lista)):
        if not (pilaLlena(pila)):
            apilar(pila, lista[i])


def tamanioPila(pila):
    """ Devuelve el tamaño de la Pila.

        Args:
            pila -- tipo "Pila()"
    """
    return pila.tope


def numeroDeCopiasElemento(pila, buscado):
    """ Devuelve el número de copias de un determinado elemento en una pila dada.

        Args:
            pila -- tipo "Pila()"
            buscado -- "dato que desee encontrar"
    """
    repeticiones = 0
    pilaAux = Pila()

    while not (pilaVacia(pila)):
        x = desapilar(pila)
        if (x == buscado):
            repeticiones += 1
        apilar(pilaAux, x)

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return repeticiones


def eliminarImpares(pila):
    """ Permite eliminar de una pila de enteros todos los números impares.

        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pilaAux, x)

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def cambiarX(pila, buscado, x):
    """ Permite cambiar todas las apariciones de un determinado elemento de la pila por otro dado.

        Args:
            pila -- tipo "Pila()"
            buscado -- "Elemento reemplazable"
            x -- "Elemento de reemplazo"
    """
    pilaAux = Pila()
    while not (pilaVacia(pila)):
        if (cimaPila(pila) == buscado):
            desapilar(pila)
            apilar(pilaAux, x)
        else:
            apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def invertirPila(pila):
    """ Invertie el contenido de una pila cualquiera.

        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    pilaAux2 = Pila()
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not (pilaVacia(pilaAux2)):
        apilar(pila, desapilar(pilaAux2))


def esPalindromo(palabra):
    """ determina si una cadena de caracteres es o no un palíndromo.

        Args:
            palabra -- cadena de "str"
    """
    pila = Pila()
    pilaAux = Pila()
    pilaAux2 = Pila()

    for i in range(0, len(palabra)):
        if not (pilaLlena(pila)):
            apilar(pila, palabra[i])

    for i in range(len(palabra)):
        if not (pilaLlena(pilaAux)):
            apilar(pilaAux, palabra[i])

    while not (pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not (pilaVacia(pila) and pilaVacia(pilaAux2)):
        if desapilar(pila) != desapilar(pilaAux2):
            return False
    return True


def xCy(palabra):
    """ determina si una hilera de caracteres de entrada es de la forma xCy, donde x es el inverso de y. Ej. mamaCamam.

        Args:
            palabra -- cadena de "str"
    """
    pilaAux = Pila()
    pila = Pila()
    llenarPila(pila, palabra)

    while (cimaPila(pila) != "C"):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)

    while not (pilaVacia(pila) and pilaVacia(pilaAux)):
        if (desapilar(pila) != desapilar(pilaAux)):
            return False
    return True


def invertirPalabra(palabra):
    """ Lee una palabra y para visualizarla en orden inverso.

        Args:
        palabra -- cadena de "str"


    """
    palabrainversa = ""
    pila = Pila()
    llenarPila(pila, palabra)

    while not (pilaVacia(pila)):
        palabrainversa += desapilar(pila)

    return palabrainversa


def eliminarDebajoCima(pila):
    """ Elimina el elemento justo debajo de la cima de la pila.

        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()

    if not (pilaLlena(pilaAux)):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)
    while not (pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def obtenerIesimoElemento(pila, numero):
    """ Obtiene el íesimo elemento a partir de la cima de una pila, sin borrarlo.

        Args:
            pila -- tipo "Pila()"
            numero -- Elemento seleccionado
    """
    pilaAux = Pila()

    x = None
    if not (pilaVacia(pila)):
        for i in range(0, numero):
            x = desapilar(pila)
            apilar(pilaAux, x)

    while not (pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return x
