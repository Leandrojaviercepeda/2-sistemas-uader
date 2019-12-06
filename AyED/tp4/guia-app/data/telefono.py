

class Telefono(object):
    """
    Clase Telefono
    
    Atributos:
        caracteristica: Caracteristica local del telefono.
        numero: Numero de telefono.
    """

    def __init__(self, caracteristica=None, numero=None):
        super(Telefono, self).__init__()
        self.caracteristica = str(caracteristica)
        self.numero = str(numero)

    def __str__(self):
        return "%s" % self.caracteristica + "%s" % self.numero

    def comparar(self, telefono):
        return self.caracteristica + self.numero == self.caracteristica + self.numero

    def __eq__(self, otro):
        return self.caracteristica + self.numero == otro

    def __ne__(self, otro):
        return self.caracteristica + self.numero != otro

    def __lt__(self, otro):
        return self.caracteristica + self.numero < otro

    def __gt__(self, otro):
        return self.caracteristica + self.numero > otro
