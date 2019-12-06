
from telefono import Telefono


class Contacto(object):
    """
    Clase Contacto
    
    Atributos:
        nombre: Nombre de la persona.
        apellido: Apellido de la persona.
        telefono: telefono de la persona (objeto de tipo Telefono)
    """

    def __init__(self, nombre, apellido, telefono=Telefono(), direccion=None, localidad=None):
        """
        :type nombre: str
        :type apellido: str
        :type telefono: object
        :type direccion: str
        :type localidad: str
        """
        super(Contacto, self).__init__()
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.telefono = telefono
        self.direccion = str(direccion)
        self.localidad = str(localidad)
        self.activo = True

    def __str__(self):
        return "Contacto: %s %s %s %s %s." % (self.nombre, self.apellido, self.telefono, self.direccion, self.localidad)

    def __eq__(self, otro):
        return self.telefono == otro

    def __ne__(self, otro):
        return self.telefono != otro

    def __lt__(self, otro):
        return self.telefono < otro

    def __gt__(self, otro):
        return self.telefono > otro
