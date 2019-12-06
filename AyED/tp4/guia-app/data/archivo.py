
import shelve


class Archivo():

    def __init__(self, nombre):
        """
        Efecto: crea un archivo.
        Parámetros:
            nombre: "archivo.extension"
        """
        self.nombre = nombre
        self.inicializar()

    def inicializar(self):
        archivo = self.abrir()
        archivo.close()

    def abrir(self):
        return shelve.open(self.nombre)

    def insertar(self, pos, dato):
        """Agrega un registro en la posicion indicada"""
        with self.abrir() as archivo:
            try:
                archivo[str(pos)] = dato
                return True
            except KeyError:
                return False

    def append(self, dato):
        """Agrega un registro al final del archivo"""
        with self.abrir() as archivo:
            pos = str(len(archivo))
            archivo[pos] = dato

    def borrarRegistro(self, pos):

        with self.abrir() as archivo:
            try:
                archivo[str(pos)] = None
                return True
            except KeyError:
                return False

    def limpiar(self):

        with self.abrir() as archivo:
            try:
                archivo.clear()
            except:
                return False

    def modificar(self, pos, dato):
        """Modifica el registro en la posicion indicada, insertando el dato indicado. Si el archivo no tiene la posición indicada devuelve None."""
        with self.abrir() as archivo:
            try:
                archivo[str(pos)] = dato
                return True
            except KeyError:
                return False

    def leer(self, pos):
        """Devuelve el registro que está en la posicion indicada, si el archivo no tiene la posición, devuelve None."""
        with self.abrir() as archivo:
            try:
                return archivo[str(pos)]
            except KeyError:
                return None

    def vacio(self):

        with self.abrir() as archivo:
            if len(archivo) != 0:
                return False
            return True

    def getIndice(self, buscado, offsetIndice=0):
        """Busca el dato indicado (buscado) en el archivo y devuelve la posición en la que se encuentra. Si no lo encuentra devuelve None."""
        indice = 0 + offsetIndice
        elemento = self.leer(indice)

        while elemento:

            if (elemento.comparar(buscado)):
                return indice
            indice += 1
            elemento = self.leer(indice)

        return None

    def __len__(self):
        with self.abrir() as archivo:
            return len(archivo)

    def __str__(self):

        strArchivo = ""
        indice = 0
        elemento = self.leer(indice)

        while (elemento):
            strArchivo += "\nIndice: %s, dato: %s" % (indice, elemento)
            indice += 1
            elemento = self.leer(indice)

        return strArchivo
