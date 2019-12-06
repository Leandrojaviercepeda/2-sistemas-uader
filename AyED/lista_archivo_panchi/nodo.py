# -*- coding: utf-8 -*-

class Nodo:
    def __init__(self, info):
        self.info = info
        self.siguiente = None
    
    
    def cambiarSiguiente(self, nuevoSiguiente):
        self.siguiente = nuevoSiguiente   
    
    
    def cambiarInfo(self, nuevaInfo):
        self.info = nuevaInfo

    
    def getTipo(self):
        return type(self.info).__name__                 
        
        
    """compara tanto la info como el siguiente"""
    def igual(self, otro):
        if otro:
            return (self.info == otro) and (self.siguiente == otro.siguiente)
        else:
            return False 
    
    
    """compara solo la info"""
    def __eq__(self, otro):       
        if otro:
            return self.info == otro
        else:
            return False  
    
    
    def __ne__(self, otro):
        if otro:
            return self.info != otro
        else:
            return True
        
    
    def __lt__(self, otro):
        if otro:
            return self.info < otro
        else:
            return False
        
        
    def __gt__(self, otro):
        if otro:
            return self.info > otro
        else:
            return True
    
    
    def __str__(self):
        return str(self.info)  