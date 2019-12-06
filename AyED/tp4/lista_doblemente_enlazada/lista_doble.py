# -*- coding: utf-8 -*-


class Nodo(object):
    """
    Clase Nodo
    
    Es un puntero al siguiente elemento de la lista; con este puntero enlazamos con el sucesor,
        de forma que podamos construir la lista.
    
    Atributos:
        info: guarda la informacion que almacenara el nodo.
        siguiente: es una referencia que apunta al siguiente nodo.
        anterior: es una referencia que apunta al anterior nodo.
    """
    def __init__(self, info=None, campo=None):
        self.modoComparacion = campo
        self.info = info
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return "%s" %(self.info)

    def __eq__(self, otro):     
        return self.criterio() == otro
    
    def __ne__(self, otro):
        return self.criterio() != otro
    
    def __lt__(self, otro):
        if otro:   
            return self.criterio() < otro
        return False
            
    def __gt__(self, otro):
        if otro:
            return self.criterio() > otro
        return False

    def criterio(self):
        """
        Dado un modoComparacion por el cual ordenar, devuelve un campo del dato contenido en el dato de la info.
        """
        #if self.modoComparacion == "primeraOpcion":
        #    return self.info.campo

        return self.info


class ListaDoble():
    """
    Clase ListaDoble
    
    Es una estructura de datos que consiste en un conjunto de nodos enlazados secuencialmente.
        Cada nodo contiene dos campos, llamados enlaces, que son referencias al nodo siguiente
        y al anterior en la secuencia de nodos. El enlace al nodo anterior del primer nodo
        y el enlace al nodo siguiente del último nodo, apuntan a un tipo de nodo que marca el final de la lista,
        normalmente un nodo centinela o puntero null,para facilitar el recorrido de la lista.
        Si existe un único nodo centinela, entonces la lista es circular a través del nodo centinela.
        
    El doble enlace de los nodos permite recorrer la lista en cualquier dirección.
        Mientras que agregar o eliminar un nodo en una lista doblemente enlazada requiere
        cambiar más enlaces que en estas mismas operaciones en una lista enlazada simple,
        las operaciones son más simples porque no hay necesidad de mantener guardado el nodo anterior
        durante el recorrido, ni necesidad de recorrer la lista para hallar el nodo anterior,
        la referencia al nodo que se quiere eliminar o insertar es lo único necesario.
    
    Atributos:
        cabecera: es una referencia que apunta al primer nodo de la Lista de nodos.
        final: es una referencia que apunta al ultimo nodo de la Lista de nodos.
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
        self.final = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio

    def __str__(self):
        return "%s" %self.toString()
    
    def actualizarPunteros(self):

        if not self.esVacia():
            
            self.cabecera.anterior = None            
            anterior = self.cabecera
            actual = self.cabecera.siguiente
            
            while actual is not None:
                actual.anterior = anterior
                actual = actual.siguiente
                anterior = anterior.siguiente
            
            self.final = anterior
    
    def buscar(self, buscado, campo=None):
        """
        Dada una lista, realiza una busqueda por campo de un elemento dado.

        @param Dato: objeto de tipo "Dato".
        @param campo: nombre del campo por el cual ordenar.
        """
        nodo = self.cabecera
        while nodo is not None and nodo.info != buscado:
            nodo = nodo.siguiente
            if (nodo is None):
                return None
        return buscado

    def insertar(self, dato, campo=None):
        """
        Inserta un elemento dado ordenado por un campo dado.

        @param dato: elemento a insertar.
        @param campo: nombre del campo por el cual ordenar.
        """
        anterior = None
        actual = None

        self.tamanio += 1
        nodo = Nodo(dato, campo)
        
        if not(self.esVacia()):
            self.cabecera.anterior = nodo

        if (self.cabecera is None) or (nodo < self.cabecera):
                nodo.siguiente = self.cabecera
                self.cabecera = nodo
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual is not None) and (nodo > actual):
                actual = actual.siguiente
                anterior = anterior.siguiente

            nodo.siguiente = actual
            anterior.siguiente = nodo
        
        self.actualizarPunteros()

    def append(self, dato):
        """
        Inserta un elemento al final de la lista. No se tiene en cuenta el orden ni el tipo.

        @param dato: elemento a insertar
        """
        anterior = None
        actual = None

        self.tamanio += 1
        nodo = Nodo(dato)

        if (self.cabecera == None):
                nodo.siguiente = self.cabecera
                self.cabecera = nodo
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual is not None):
                actual = actual.siguiente
                anterior = anterior.siguiente

            nodo.siguiente = actual
            anterior.siguiente = nodo
     
        self.actualizarPunteros()

    def eliminar(self, dato):
        """
        Elimina un elemento. Si la lista fue ordenada por un campo clave, puede especificar este unico dato para eliminar un elemento.
        @param dato: elemento a insertar.
        @param campo: nombre del campo por el cual ordenar.
        """
        actual = None
        anterior = None

        if self.cabecera == dato:
            dato = self.cabecera.info
            self.cabecera = self.cabecera.siguiente
            self.tamanio -= 1
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while actual is not None and actual != dato:
                anterior = anterior.siguiente
                actual = actual.siguiente

            if actual is not None:
                dato = actual.info
                anterior.siguiente = actual.siguiente
                self.tamanio -= 1
            else:
                return None

        self.actualizarPunteros()

        return dato 
    
    def esVacia(self):
        """
        Devuelve "True" si la lista esta llena, "False" en el caso contrario.
        """
        if self.cabecera is not None:
            return False
        return True

    def insertarElementos(self, datos, campo=None):
        """
        Inserta un conjunto de datos dados en una lista enlazada.

        @param datos: array de datos de cualquier tipo.
        """
        for x in datos:
            self.insertar(x, campo)

    def appendElementos(self, datos):
        """
        Inserta un conjunto de datos dados en una lista enlazada. No se tiene en cuenta el orden.

        @param datos: array de datos de cualquier tipo.
        """
        for x in datos:
            self.append(x)

    def toString(self):
        """
        Muestra los elementos de una lista.
        """
        if not(self.esVacia()):
            
            nodo = self.cabecera
            strLista = ""
            
            while nodo is not None:
                strLista += "%s, "% nodo.info
                nodo = nodo.siguiente
                
            return "(%s)"%strLista[:-2]

    def toStringInversa(self):
        """
        Muestra los elementos de una self en forma invertida.
        """
        if not(self.esVacia()):
            
            nodo = self.final
            strLista = ""
            
            while nodo is not None:
                strLista += "{}, ".format(nodo.info)
                nodo = nodo.anterior

            return "(%s)" % strLista[:-2]

datos = ["c","b","a","d","g","x","o","s","h"]
lista = ListaDoble()
lista.insertarElementos(datos)
print(lista)
print()
print(lista.toStringInversa())