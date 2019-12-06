
class Nodo():
    
    def __init__(self):
        self.info = None
        self.sig = None


class Pila():
    
    def __init__(self):
        self.tamanio = 0
        self.tope = None


def apilar(pila, x):
    """ Efecto: Apila un elemento en el ultimo lugar de la pila.
        
        Args:
            pila -- tipo "Pila()"
    """
    nodo = Nodo()
    nodo.info = x
    nodo.sig = pila.tope
    pila.tope = nodo
    pila.tamanio += 1


def desapilar(pila):
    """ Efecto: Desapila el ultimo elemento de la pila.
        
        Args:
            pila -- tipo "Pila()"
            pila -- tipo "Pila()"
    """
    x = pila.tope.info
    pila.tope = pila.tope.sig
    pila.tamanio -= 1
    return x


def pilaVacia(pila):
    """ Efecto: Determina si una pila es no vacía.
        
        Args:
            pila -- tipo "Pila()"
    """
    return (pila.tope == None)


def pilaLlena(pila):
    """ Efecto: Devuelve False por defecto.
        
        Args:
            pila -- tipo "Pila()"
    """
    return False


def cimaPila(pila):
    """ Efecto: Devuelve el ultimo elemento insertado en la pila.
        
        Args:
            pila -- tipo "Pila()"
    """
    return pila.tope.info


def cargarPila(pila):
    """ Efecto: Permite al usuario cargar elementos mientras lo desee.
        
        Args:
            pila -- tipo "Pila()"
    """
    print("Carga de elementos")
    n = "S"
    while not(pilaLlena(pila)) and n == "S":
        x = input("Introduzca un elemento: ")
        apilar(pila, x)
        n = input("'S' para continuar: ")
        n.upper()


def verPila(pila):
    """ Efecto: Muestra el contenido de la pila.
        
        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        x = desapilar(pilaAux)
        print (x , end = ", ")
        apilar(pila, x)


def llenarPila(pila, lista):
    """ Efecto: Dado un array de datos los introduce una pila.
    
        Args:
            pila -- tipo "Pila()"
            lista -- array["cualquier tipo"]
    """
    for i in range(len(lista)):
        if not(pilaLlena(pila)):
            apilar(pila, lista[i])    


def tamanioPila(pila):
    """ Efecto: Devuelve el tamaño de la Pila.
    
        Args:
            pila -- tipo "Pila()
    """
    return pila.tope


def numeroDeCopiasElemento(pila, buscado):
    """ Efecto: Devuelve el número de copias de un determinado elemento en una pila dada.
        
        Args:
            pila -- tipo "Pila()"
            buscado -- "dato que desee encontrar"
    """
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


def eliminarImpares(pila):
    """ Efecto: Permite eliminar de una pila de enteros todos los números impares.
        
        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    while not(pilaVacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pilaAux, x)

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def cambiarX(pila, buscado, x):
    """ Efecto: Permite cambiar todas las apariciones de un determinado elemento de la pila por otro dado.
        
        Args:
            pila -- tipo "Pila()"
            buscado -- "Elemento reemplazable"
            x -- "Elemento de reemplazo"
    """
    pilaAux = Pila()
    while not(pilaVacia(pila)):
        if (cimaPila(pila) == buscado):
            desapilar(pila)
            apilar(pilaAux, x)
        else:
            apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def invertirPila(pila):
    """ Efecto: Invertie el contenido de una pila cualquiera.
        
        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()
    pilaAux2 = Pila()
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pilaAux2, desapilar(pilaAux))

    while not(pilaVacia(pilaAux2)):
        apilar(pila, desapilar(pilaAux2))


def esPalindromo(palabra):
    """ Efecto: determina si una cadena de caracteres es o no un palíndromo.
        
        Args:
            palabra -- cadena de "str"
    """
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


def xCy(palabra):
    """ Efecto: determina si una hilera de caracteres de entrada es de la forma xCy, donde x es el inverso de y. Ej. mamaCamam.
        
        Args:
            palabra -- cadena de "str"
    """
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


def invertirPalabra(palabra):
    """ Efecto: Lee una palabra y para visualizarla en orden inverso.
        
        Args:
            palabra -- cadena de "str"
    """
    palabrainversa = ""
    pila = Pila()
    llenarPila(pila, palabra)

    while not(pilaVacia(pila)):
        palabrainversa += desapilar(pila)

    return palabrainversa


def eliminarDebajoCima(pila):
    """ Efecto: elimina el elemento justo debajo de la cima de la pila.
        
        Args:
            pila -- tipo "Pila()"
    """
    pilaAux = Pila()

    if not(pilaLlena(pilaAux)):
        apilar(pilaAux, desapilar(pila))

    desapilar(pila)
    while not(pilaVacia(pila)):
        apilar(pilaAux, desapilar(pila))

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))


def obtenerIesimoElemento(pila, numero):
    """ Efecto: obtiene el íesimo elemento a partir de la cima de una pila, sin borrarlo.
        
        Args:
            pila -- tipo "Pila()"
            numero -- Elemento seleccionado
    """
    pilaAux = Pila()
    x = None
    if not(pilaVacia(pila)):
        for i in range(0, numero):
            x = desapilar(pila)
            apilar(pilaAux, x)

    while not(pilaVacia(pilaAux)):
        apilar(pila, desapilar(pilaAux))

    return x
