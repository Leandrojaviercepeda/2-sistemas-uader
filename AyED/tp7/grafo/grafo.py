import sys


class Vertice(object):
    """
    Vertice utiliza un diccionario para realizar un seguimiento
    de los vértices a los que está conectado, y la Ponderacion() de cada arista.
    """

    def __init__(self, clave, info):
        super(Vertice, self).__init__()
        self.__id = clave
        self.__info = info
        self.__predecesor = None
        self.__conectadoA = {}
        self.__dist = sys.maxsize

    def __cmp__(self, otroVertice):
        return self.cmp(self.__dist, otroVertice.__dist)

    def __lt__(self, otroVertice):
        prioridad = self.__dist
        otraPrioridad = otroVertice.__dist
        return prioridad < otraPrioridad

    def obtenerId(self):
        return self.__id

    def obtenerInfo(self):
        return self.__info

    def asignarDistancia(self, distancia):
        self.__dist = distancia

    def obtenerDistancia(self):
        return self.__dist

    def asignarPredecesor(self, predecesor):
        self.__predecesor = predecesor

    def obtenerPredecesor(self):
        return self.__predecesor

    def agregarVecino(self, vecino, ponderacion=0):
        """
        Agrega una conexión desde este vértice a otro.
        :param vecino: Vertice().
        :param ponderacion: costo para ir de un vértice a
               otro. Representado por un diccionario.
        """
        assert type(vecino) is Vertice, "OopS! '{}' no es de tipo '{}'".format(vecino, Vertice)
        self.__conectadoA[vecino] = ponderacion

    def quitarVecino(self, vecino):
        assert vecino in self.__conectadoA, "Oops! '{}' no esta conectado a '{}'".format(self.__id, vecino)
        del self.__conectadoA[vecino]
        return "{} quitado!".format(vecino.__id)

    def __str__(self):
        return str(self.__id) + ' conectadoA: ' + str([x.__id for x in self.__conectadoA])

    def obtenerConexiones(self):
        """
        Devuelve todos los vértices de la lista de adyacencia,
        :return: vertices a los que se conecta.
        """
        return self.__conectadoA.keys()

    def obtenerPonderacion(self, vecino):
        """
        Devuelve la ponderación de la arista de este vértice
        al vértice pasado como parámetro.
        :param vecino: vertice al que se conecta.
        :return: costo de ir de un vertice a otro
        """
        assert vecino in self.__conectadoA, "Oops! '{}' no esta conectado a '{}'".format(self.__id, vecino)
        return self.__conectadoA[vecino]


class Grafo(object):
    """
    Grafo contiene un diccionario que asigna nombres de vértices a objetos vértice.
    También proporciona métodos para agregar vértices a un grafo y conectar un vértice a otro.
    """

    def __init__(self):

        self.__listaVertices = {}
        self.__numVertices = 0

    def agregarVertice(self, clave, info):
        self.__numVertices = self.__numVertices + 1
        nuevoVertice = Vertice(clave, info)
        self.__listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def quitarVertice(self, clave):
        assert clave in self.__listaVertices, "Oops! '{}' no esta en '{}'".format(clave, self)
        del self.__listaVertices[clave]
        self.__numVertices = self.__numVertices - 1

    def __str__(self):
        strG = ""
        for v in self.__listaVertices.values():
            strG += "%s,\n " % (v.__str__())
        return "({})".format(strG[:-3])

    def obtenerVertice(self, n):
        """
        Devuelve un vertice dada una clave, None si esta no existe.
        :param n: clave
        :return: Vertice()
        """
        if n in self.__listaVertices:
            return self.__listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.__listaVertices

    def agregarArista(self, de, a, costo=0):
        """
        Crea una conexion (arista) de un vertice a otro.
        :param de: clave
        :param a: clave
        :param costo: costo para ir de un vértice a otro.
        """
        if de not in self.__listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.__listaVertices:
            nv = self.agregarVertice(a)
        self.__listaVertices[de].agregarVecino(self.__listaVertices[a], costo)

    def quitarArista(self, de, a):
        """
        Elimina una conexion (arista) de un vertice a otro.
        :param de: clave
        :param a: clave
        :return: str
        """
        assert de in self.__listaVertices, "Oops! '{}' no esta en '{}'".format(de, self)
        assert a in self.__listaVertices, "Oops! '{}' no esta en '{}'".format(a, self)
        self.__listaVertices[de].quitarVecino(self.__listaVertices[a])
        return "Arista de '{}' a '{}' quitada!".format(self.__listaVertices[de].obtenerId(),
                                                       self.__listaVertices[a].obtenerId())

    def obtenerVertices(self):
        return self.__listaVertices.keys()

    def __iter__(self):
        return iter(self.__listaVertices.values())
