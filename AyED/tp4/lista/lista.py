
class Nodo(object):

    def __init__(self, info=None, modoComparacion=None):
        self.modoComparacion = modoComparacion
        self.info = info
        self.siguiente = None

    def __str__(self):
        return "Info: %s, siguiente: %s" %(self.info, self.siguiente)

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
        if self.modoComparacion == "nombre":
            return self.info.nombre
        
        elif self.modoComparacion == "edad":
            return self.info.edad
        
        elif self.modoComparacion == "estadoCivil":
            return self.info.estadoCivil
        
        elif self.modoComparacion == "direccion":
            return self.info.direccion
              
        return self.info


class Lista(object):
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

    def buscar(self, buscado):
        """
        Dada una lista, realiza una busqueda por campo de un elemento dado.

        @param Dato: objeto de tipo "Dato".
        @param campo: nombre del campo por el cual ordenar.
        """
        nodo = self.cabecera
        while ((nodo != None) and (nodo.info != buscado)):
            nodo = nodo.siguiente
            if (nodo == None):
                return None
        return nodo.info

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

    def insertar(self, dato, campo=None):
        """
        Inserta un elemento dado ordenado por un campo dado.

        @param dato: elemento a insertar.
        @param campo: nombre del campo por el cual ordenar.
        """
        self.tamanio += 1
        nodo = Nodo(dato, campo)

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

    def append(self, dato):
        """
        Inserta un elemento al final de la lista. No se tiene en cuenta el orden ni el tipo.

        @param dato: elemento a insertar
        """
        self.tamanio += 1
        nodo = Nodo(dato)

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

    def eliminar(self, dato):
        """
        Elimina un elemento. Si la lista fue ordenada por un campo clave, puede especificar este unico dato para eliminar un elemento.

        @param dato: elemento a insertar.
        """

        if self.cabecera == dato:
            dato = self.cabecera.info
            self.cabecera = self.cabecera.siguiente
            self.tamanio -= 1
        else:
            anterior = self.cabecera
            actual = self.cabecera.siguiente

            while (actual != None) and (actual != dato):
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

