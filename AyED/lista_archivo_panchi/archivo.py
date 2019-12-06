# -*- coding: utf-8 -*-
import shelve


class Archivo:
 
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.inicializar()
        
         
    def inicializar(self):
        archivo = self.abrir()
        archivo.close()
    
    
    def abrir(self):
        return shelve.open(self.nombreArchivo)
  
    
    """agrega un registro en la posicion indicada"""
    def agregar(self, pos, dato):
        
        with self.abrir() as archivo:
            archivo[str(pos)] = dato
            
    """agrega un registro a lo ultimo del archivo"""
    def append(self, dato):
        
        with self.abrir() as archivo:
        
            tamañoArchivo = str(len(archivo))
            archivo[tamañoArchivo] = dato


    """Devuelve el registro que está en la posicion indicada, si el archivo no tiene la posición, devuelve None."""
    def leer(self, pos):
        with self.abrir() as archivo:
        
            try:
                return archivo[str(pos)]
            except KeyError:
                return None

    
    """Modifica el registro en la posicion indicada, insertando el dato indicado. Si el archivo no tiene la posición indicada devuelve None."""
    def modificar(self, pos, dato):
        with self.abrir() as archivo:
        
            try:
                archivo[str(pos)] = dato
                return True
            except:
                return False

    
    def vacio(self):
        with self.abrir() as archivo:
        
            if len(archivo) == 0:
                return True
            else:
                return False
    
    
    """Busca el dato indicado (buscado) en el archivo y devuelve la posición en la que se encuentra. Si no lo encuentra devuelve None."""
    def indice(self, buscado, offsetIndice = 0):        
        
        indice = 0 + offsetIndice
        elemento = self.leer(indice)
        
        while(elemento):

            if (elemento.igual(buscado)):
                return indice
            
            indice += 1
            elemento = self.leer(indice)

                
        return None
            
    
    def __str__(self):
        
        strArchivo = "" 
        indice = 0
        elemento = self.leer(indice)
        
        while(elemento):
            
            strArchivo += "{0}, ".format(elemento) 
            indice += 1
            elemento = self.leer(indice)
                
        return strArchivo
    
    
    def __len__(self):
        with self.abrir() as archivo:
            return len(archivo)
        
    


