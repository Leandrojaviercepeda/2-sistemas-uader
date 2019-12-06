
from criterio import criterio


class Nodo():
    """
    Clase Nodo

    Es un puntero al siguiente elemento de la lista; con este puntero enlazamos con el sucesor,
        de forma que podamos construir la lista.

    Atributos:
        info: guarda la informacion que almacenara el nodo.
        siguiente: es una referencia que apunta al siguiente nodo.
    """

    def __init__(self):
        self.info = None
        self.siguiente = None

    def __str__(self):
        return "%s" % self.info

    def __eq__(self, otro):
        return self.info == otro

    def __ne__(self, otro):
        return self.info != otro

    def __lt__(self, otro):
        return self.info < otro

    def __gt__(self, otro):
        return self.info > otro


class Lista():
    """
    Clase Lista
    
    La lista enlazada es un TDA que nos permite almacenar datos de una forma organizada,
        al igual que los vectores pero, a diferencia de estos, esta estructura es dinámica,
        por lo que no tenemos que saber "a priori" los elementos que puede contener.
    
    En una lista enlazada, cada elemento apunta al siguiente excepto el último que no tiene sucesor
        y el valor del enlace es null. Por ello los elementos son registros que contienen el dato a
        almacenar y un enlace al siguiente elemento. Los elementos de una lista,
        suelen recibir también el nombre de nodos de la lista.
    
    Atributos:
        cabecera: es una referencia que apunta al primer nodo de la Lista de nodos.
        tamanio: nos devuelve el tamaño de la lista en base a la cantidad de nodos que contiene.
    
    Para que esta estructura sea un TDA lista enlazada,
        debe tener unos operadores asociados que permitan la manipulación de los datos que contiene.
        Los operadores básicos de una lista enlazada son:
    
        ·Insertar: inserta un nodo con dato x en la lista, pudiendo realizarse esta inserción
            al principio o final de la lista o bien en orden.
    
        ·Eliminar: elimina un nodo de la lista, puede ser según la posición o por el dato.
    
        ·Buscar: busca un elemento en la lista.

    """

    def __init__(self):
        self.cabecera = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio

    def __str__(self):
        return "%s" % self.toString()

    def buscar(self, buscado, campo=None):
        """
        Dada una lista, realiza una busqueda por campo de un elemento dado.

        @param Dato: objeto de tipo "Dato".
        @param campo: nombre del campo por el cual ordenar.
        @return buscado: dato encontrado
        """
        nodo = self.cabecera
        while ((nodo is not None) and (criterio(nodo, campo) != buscado)):
            nodo = nodo.siguiente

            if (nodo is None):
                return None

        return nodo

    def toString(self):
        """
        Muestra los elementos de una lista.
        """
        if not (self.esVacia()):
            nodo = self.cabecera
            strLista = ""
            while nodo != None:
                strLista += "%s, " % nodo.info
                nodo = nodo.siguiente

            return "(%s)" % strLista[:-2]

    def obtener(self, indice):
        """
        Dado un indice devuelve el dato contenido en esta posicion.
        """
        contador = 0

        if not (self.esVacia()) and type(indice) is int:

            nodo = self.cabecera

            if indice == contador:
                return nodo.info

            while (nodo is not None):

                nodo = nodo.siguiente
                contador += 1

                if contador == indice:
                    return nodo.info

        return None

    def insertar(self, dato, campo=None):
        """
        Inserta un elemento dado ordenado por un campo dado.

        @param dato: elemento a insertar.
        @param campo: nombre del campo por el cual ordenar.
        """
        anterior = None
        actual = None

        self.tamanio += 1
        nodo = Nodo()
        nodo.info = dato

        if (self.cabecera == None) or (criterio(nodo, campo) < criterio(self.cabecera, campo)):
            nodo.siguiente = self.cabecera
            self.cabecera = nodo
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual != None) and (criterio(nodo, campo) > criterio(actual, campo)):
                actual = actual.siguiente
                anterior = anterior.siguiente

            nodo.siguiente = actual
            anterior.siguiente = nodo

    def append(self, dato):
        """
        Inserta un elemento al final de la lista. No se tiene en cuenta el orden ni el tipo.

        @param dato: elemento a insertar
        """
        anterior = None
        actual = None

        self.tamanio += 1
        nodo = Nodo()
        nodo.info = dato

        if (self.cabecera == None):
            nodo.siguiente = self.cabecera
            self.cabecera = nodo
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual != None):
                actual = actual.siguiente
                anterior = anterior.siguiente

            nodo.siguiente = actual
            anterior.siguiente = nodo

    def eliminar(self, dato, campo=None):
        """
        Elimina un elemento dado buscado por campo.

        @param dato: elemento a insertar.
        @param campo: nombre del campo por el cual ordenar.
        """
        actual = None
        anterior = None

        if criterio(self.cabecera, campo) == criterio(dato, campo):
            dato = self.cabecera.info
            self.cabecera = self.cabecera.siguiente
            self.tamanio -= 1
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual != None) and (criterio(actual, campo) != criterio(dato, campo)):
                anterior = anterior.siguiente
                actual = actual.siguiente

            if actual != None:
                dato = actual.info
                anterior.siguiente = actual.siguiente
                self.tamanio -= 1
            else:
                return None

        return dato

    def esVacia(self):
        """
        Devuelve "True" si la lista esta llena, "False" en el caso contrario.
        """
        if self.cabecera != None:
            return False
        return True

    def insertarElementos(self, datos):
        """
        Inserta un conjunto de datos dados en una lista enlazada.

        @param datos: array de datos de cualquier tipo.
        """
        for x in datos:
            self.insertar(x)

    def appendElementos(self, datos):
        """
        Inserta un conjunto de datos dados en una lista enlazada. No se tiene en cuenta el orden.

        @param datos: array de datos de cualquier tipo.
        """
        for x in datos:
            self.append(x)
