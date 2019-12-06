#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Semaforo():
    
    def __init__(self, identificador, tiempo, estado):
        self.identificador = identificador
        self.tiempo = int(tiempo)
        self.estado = estado

    def __str__(self):
        return "Semaforo: %s, Tiempo: %s, Estado: %s"% (self.identificador, self.tiempo, self.estado)

    def getIdentificador(self):
        return self.identificador
    
    def getTiempo(self):
        return self.tiempo
    
    def getEstado(self):
        return self.estado
    
    
    def setIdentificador(self, identificador):
        self.identificador = identificador    

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setEstado(self, estado):
        self.estado = estado