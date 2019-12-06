# -*- coding: utf-8 -*-
from archivo import Archivo
from nodo import Nodo

"""
soporta:
    •inserción/eliminación de elementos repetidos
    •re-utilización de huecos    
    •cualquier tipo de dato (pero no soporta la inserción de diferentes tipos de datos)    

    IMPORTANTE: El tipo de datos que va a contener la lista queda determinado por el primer elemento que se inserta a la misma, 
    pero si todos los datos que contiene son borrados se puede cambiar el tipo de dato que almacena esta ingresando un tipo de dato
    diferente al que contenía en primera instancia.
    
    Ejemplo:
        lista = ListaArchivo("lista")
        lista.insertar("dato de tipo string") <--- ahora solo se pueden ingresar strings
        lista.insertar(1.7) <--------------------- error
        lista.eliminar("dato de tipo string") <--- eliminamos el unico elemento de la lista, ahora podemos cambiar el tipo que almacena
        lista.insertar(1.7) <--------------------- ahora solo se puaeden ingresar floats
"""  

class ListaArchivo:
    
    vacio = "---"
    msjErrorTipo = "ERROR: El tipo del elemento que intentas insertar ({0}) no coincide con el tipo de datos que contiene la lista ({1})."
    
    def __init__(self, nombre):

        self.archivo = Archivo(nombre)
        if self.archivo.vacio():
            self.archivo.append(None)
            
        self.primero = self.archivo.leer(0)
        self.tamaño = self.getTamaño()
    
    
    def vacia(self):
        
        listaVacia = (self.tamaño == 0)
        
        if listaVacia:
            return True
        else:
            return False     
        
        
    """actualiza el primero (tanto en el archivo como en la variable que maneja la lista)"""
    def cambiarPrimero(self, nuevoPrimero):
        self.primero = nuevoPrimero
        self.archivo.modificar(0, nuevoPrimero)
        
    
    def getIndiceEspacioVacio(self):
        
        for i in range(len(self.archivo)):
            
            esUnEspacioVacio = (self.archivo.leer(i) == ListaArchivo.vacio)
            
            if esUnEspacioVacio:
                return i
        
        
        return len(self.archivo)
    
    
    def getTamaño(self):
        
        cantidadElementos = 0
        
        for i in range(1, len(self.archivo)):
            elemento = self.archivo.leer(i)
            
            if (elemento != ListaArchivo.vacio):
                cantidadElementos += 1
        
        
        return cantidadElementos
        
    
    def getPrimerElemento(self):
        return self.archivo.leer(self.primero)
    
    
    def insertar(self, dato):
        
        nuevoElemento = Nodo(dato)
        
        indicePrimero = self.primero
        indiceNuevoElemento = self.getIndiceEspacioVacio()
        
        try:
            nuevoMenorAlPrimero = (nuevoElemento < self.getPrimerElemento())
        except TypeError:
            
            tipoDatoElemento = nuevoElemento.getTipo()
            tipoDatoLista = self.getPrimerElemento().getTipo()
            
            print(ListaArchivo.msjErrorTipo.format(tipoDatoElemento, tipoDatoLista))
            return
        
        if self.vacia() or nuevoMenorAlPrimero:
              
            nuevoElemento.cambiarSiguiente(indicePrimero)
            self.cambiarPrimero(indiceNuevoElemento)
            
        else:
            
            anterior = self.getPrimerElemento()
            actual = self.archivo.leer(anterior.siguiente)
            
            hayaSiguiente = (actual != None)
            actualSeaMenor = (actual < nuevoElemento)
            
            while hayaSiguiente and actualSeaMenor:
                
                actual = self.archivo.leer(actual.siguiente)
                anterior = self.archivo.leer(anterior.siguiente)
                
                hayaSiguiente = (actual != None)
                actualSeaMenor = (actual < nuevoElemento)
            
            indiceAnterior = self.archivo.indice(anterior, 1)
            
            anterior.cambiarSiguiente(indiceNuevoElemento)
            nuevoElemento.cambiarSiguiente(self.archivo.indice(actual, 1))
            
            self.archivo.modificar(indiceAnterior, anterior)
                 
            
        self.archivo.agregar(indiceNuevoElemento, nuevoElemento)
        self.tamaño += 1 
    
    
    def eliminar(self, dato): 
        
        info = None
        
        if self.vacia():
            return info
        
        indicePrimerElemento = self.primero
        primerElemento = self.getPrimerElemento()
        
        esElPrimero = (dato == primerElemento)
        
        if esElPrimero:
            
            info = primerElemento.info

            siguienteAlPrimero = primerElemento.siguiente
            self.cambiarPrimero(siguienteAlPrimero)
            
            primerElemento.cambiarInfo(ListaArchivo.vacio)
            self.archivo.modificar(indicePrimerElemento, primerElemento)
            
            self.tamaño -= 1
            
        else:
            anterior = primerElemento         
            actual = self.archivo.leer(anterior.siguiente)

            hayaSiguiente = (actual != None)
            noEncontrado = (actual != dato)
            
            while hayaSiguiente and noEncontrado:
                
                actual = self.archivo.leer(actual.siguiente)
                anterior = self.archivo.leer(anterior.siguiente)
                
                hayaSiguiente = (actual != None)
                noEncontrado = (actual != dato)
                   
            loEncontró = (actual == dato)
            
            if loEncontró:
                info = actual.info
                
                indiceActual = self.archivo.indice(actual, 1)
                indiceAnterior = self.archivo.indice(anterior, 1)
                
                anterior.cambiarSiguiente(actual.siguiente)
                self.archivo.modificar(indiceAnterior, anterior)
                
                actual.cambiarInfo(ListaArchivo.vacio)
                self.archivo.modificar(indiceActual, actual)
                
                self.tamaño -= 1
                
        return info
    
    
    def insertarElementos(self, lista):
        for i in lista:
            self.insertar(i)
    
    
    def __str__(self):
        strLista = ""
        actual = self.getPrimerElemento()      
        hayaSiguiente = (actual != None)
        
        while hayaSiguiente:
            
            strLista += "{0}, ".format(actual)
            actual = self.archivo.leer(actual.siguiente)
            
            hayaSiguiente = (actual != None)
        
        return strLista
    
    def __len__(self):
        return self.tamaño




lista = ListaArchivo("lean")
#datos = ["f", "a", "c", "b", "h", "i"]
#lista.insertarElementos(datos)
print(lista)