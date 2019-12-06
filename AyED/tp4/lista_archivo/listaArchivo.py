
from archivo import Archivo

class Nodo():

    def __init__(self):
        self.modoComparacion = None
        self.info = None
        self.siguiente = None
    
    def setCriterio(self, modoComparacion):
        self.modoComparacion = modoComparacion
    
    def getInfo(self):
        return self.info
    
    def setInfo(self, dato):
        self.info = dato
        
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
        
    def getSiguiente(self):
        return self.siguiente

    def getTipo(self):
        return type(self.info).__name__
    
    def comparar(self, otro):
        if otro:
            return (self.criterio() == otro.criterio()) and (self.siguiente == otro.siguiente)
        else:
            return False

    def __str__(self):
        return '{}'.format(self.info)

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
        if self.modoComparacion == "origen":
            return self.info.obtenerOrigen()
        
        elif self.modoComparacion == "destino":
            return self.info.obtenerDestino()
        
        elif self.modoComparacion == "distancia":
            return self.info.obtenerDistancia()
        
        elif self.modoComparacion == "medio":
            return self.info.obtenerMedio()

        return self.info


class ListaArchivo():

    msjErrorTipo = "ERROR: El tipo del elemento que intentas insertar ({0}) no coincide con el tipo de datos que contiene la lista ({1})."

    def __init__(self, nombre):
        self.archivo = Archivo(nombre)


        if self.archivo.vacio():
            self.archivo.append(None)

        self.primero = self.archivo.leer(0)
        self.huecos = self.inicializarHuecos()
        self.tamaño = self.getTamaño()
        self.iterador = None

    def vacia(self):
        return True if (self.tamaño == 0) else False

    def getPrimero(self):
        return self.archivo.leer(self.primero)

    def setPrimero(self, nuevoPrimero):
        self.primero = nuevoPrimero
        self.archivo.modificar(0, nuevoPrimero)

    def setHueco(self, hueco):
        self.huecos.append(hueco)

    def getPosicion(self):
        hayHuecos = (len(self.huecos) != 0)

        if hayHuecos:
            return self.huecos.pop(0)
        else:
            return len(self.archivo)

    def getTamaño(self):
        return ((len(self.archivo)- 1)- len(self.huecos))

    def inicializarHuecos(self):
        huecos = []
        for i in range(1, len(self.archivo)):
            if self.archivo.leer(i) == None:
                huecos.append(i)
        return huecos

    def __str__(self):

        strLista = ""
        actual = self.getPrimero()
        hayaSiguiente = (actual != None)

        while hayaSiguiente:

            strLista += '{}, '.format(actual)
            actual = self.archivo.leer(actual.siguiente)

            hayaSiguiente = (actual != None)

        return '[{}]'.format(strLista[:-2])

    def __len__(self):
        return ((len(self.archivo)- 1)- len(self.huecos))

    def insertar(self, dato, campo=None):

        nodo = Nodo()
        nodo.setCriterio(campo)
        nodo.setInfo(dato)
        pos = self.getPosicion()

        try:
            nuevoMenorAlPrimero = nodo < self.getPrimero()
        except TypeError:

            tipoDatoElemento = nodo.getTipo()
            tipoDatoLista = self.getPrimero().getTipo()

            print(ListaArchivo.msjErrorTipo.format(tipoDatoElemento, tipoDatoLista))
            return

        if self.vacia() or nuevoMenorAlPrimero:

            nodo.setSiguiente(self.primero)
            self.setPrimero(pos)

        else:

            anterior = self.getPrimero()
            actual = self.archivo.leer(anterior.getSiguiente())

            hayaSiguiente = (actual != None)
            actualSeaMenor = actual < nodo

            while hayaSiguiente and actualSeaMenor:

                actual = self.archivo.leer(actual.getSiguiente())
                anterior = self.archivo.leer(anterior.getSiguiente())


                hayaSiguiente = (actual != None)
                actualSeaMenor = actual < nodo

            indiceAnterior = self.archivo.getIndice(anterior, 1)

            nodo.setSiguiente(anterior.getSiguiente())
            anterior.setSiguiente(pos)

            self.archivo.modificar(indiceAnterior, anterior)

        self.archivo.insertar(pos, nodo)
        self.tamaño = self.tamaño+1

    def eliminar(self, dato):

        if not(self.vacia()):

            primerElemento = self.getPrimero()
            esElPrimero = (dato == primerElemento)

            if esElPrimero:

                info = primerElemento.getInfo()

                siguienteAlPrimero = primerElemento.getSiguiente()

                self.archivo.borrarRegistro(self.primero)
                self.setPrimero(siguienteAlPrimero)

                self.tamaño = self.tamaño-1

            else:

                anterior = primerElemento
                actual = self.archivo.leer(anterior.getSiguiente())

                hayaSiguiente = (actual != None)
                nuevoSeaDistinto = actual != dato

                while hayaSiguiente and nuevoSeaDistinto:
                    anterior = self.archivo.leer(anterior.getSiguiente())
                    actual = self.archivo.leer(actual.getSiguiente())

                    hayaSiguiente = (actual != None)
                    nuevoSeaDistinto = dato != actual

                loEncontro = (actual == dato)

                if loEncontro:

                    info = actual.getInfo()

                    indiceActual = self.archivo.getIndice(actual, 1)
                    indiceAnterior = self.archivo.getIndice(anterior, 1)


                    anterior.setSiguiente(actual.getSiguiente())
                    self.archivo.modificar(indiceAnterior, anterior)

                    self.archivo.modificar(indiceActual, None)
                    self.tamaño = self.tamaño-1

            return info
        else:
            return None

    def insertarDatos(self, datos):
        for dato in datos:
            self.insertar(dato)

    def buscar(self, dato, campo=None):
        """
        Devuelve un dato si este esta contenido en la "ListaArchivo". La busqueda se puede realizar especificando un campo.
        
        @param dato: dato a buscar.
        @param campo: campo por el cual buscar.
        @return resultado: "dato" si este esta contenido. "None" si no esta contenido.
        """
        anterior = self.getPrimero()
        actual = self.archivo.leer(anterior.getSiguiente())

        if anterior == dato:
            return anterior

        else:
            hayaSiguiente = (actual is not None)
            nuevoSeaDistinto = actual != dato

            while hayaSiguiente and nuevoSeaDistinto:
                anterior = self.archivo.leer(anterior.getSiguiente())
                actual = self.archivo.leer(actual.getSiguiente())

                hayaSiguiente = (actual is not None)
                nuevoSeaDistinto = dato != actual

            loEncontro = actual == dato

            if loEncontro:
                return actual

        return None

    def __contains__(self, item):
        return self.buscar(item) is not None

    def __iter__(self):
        self.iterador = self.getPrimero()
        return self

    def __next__(self):
        if self.iterador is not None:
            nodo = self.iterador
            self.iterador = self.archivo.leer(nodo.getSiguiente())
            return nodo
        else:
            raise StopIteration

