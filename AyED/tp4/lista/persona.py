class Persona(object):

    def __init__(self, nombre, edad, estadoCivil=None, direccion=None):
        self.nombre = nombre
        self.edad = int(edad)
        self.estadoCivil = estadoCivil
        self.direccion = direccion

    def __str__(self):
        salida = "Nombre: {}, Edad: {}, Estado civil: {}, Direccion: {}".format(self.nombre, self.edad,
                                                                                self.estadoCivil, self.direccion)
        return salida

    def __eq__(self, otro):     
        return id(self) == id(otro)
    
    def __ne__(self, otro):
        return id(self) != id(otro)
    
    def __lt__(self, otro):
        if otro:   
            return id(self) < id(otro)
        return False
            
    def __gt__(self, otro):
        if otro:
            return id(self) > id(otro)
        return False

