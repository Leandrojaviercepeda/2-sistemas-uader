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
