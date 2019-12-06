

class NodoArchivo():
    """
    Clase Nodo
    
    Es un puntero al indice elemento de la lista; con este puntero enlazamos con el sucesor,
        de forma que podamos construir la lista.
    
    Atributos:
        info: guarda la informacion que almacenara el nodo.
        indice: es una referencia que apunta al indice nodo.
    """

    def __init__(self, info, indice):
        self.info = info
        self.indice = indice

    def __str__(self):
        return "%s" % self.info

    def __eq__(self, cosa):
        return self.info == cosa

    def __ne__(self, cosa):
        return self.info != cosa

    def __lt__(self, cosa):
        return self.info < cosa

    def __gt__(self, cosa):
        return self.info > cosa
