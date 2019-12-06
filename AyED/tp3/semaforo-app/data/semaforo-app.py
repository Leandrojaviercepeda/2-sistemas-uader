#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import imagenes
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

import cola as c
import semaforo as s
from semaforos import Ui_widgSemaforo


class interfazSemaforo(Ui_widgSemaforo, QDialog):

    def __init__(self):
        super(interfazSemaforo, self).__init__()

        Ui_widgSemaforo.__init__(self)
        self.setupUi(self)

        self.iniciado = False
        self.cola = crearColaConSemaforos()

        self.btnCambiar.clicked.connect(self.cambiar)
        self.btnIniciar.clicked.connect(self.iniciar)
        self.btnParar.clicked.connect(self.parar)

    def iniciar(self):
        """Valida la peticion enviada por el boton iniciar e inicia el sistema."""
        if not (self.iniciado):
            self.iniciado = True
            self.iniciarSistema()

    def parar(self):
        """Valida la peticion enviada por el boton parar y para el sistema."""
        if (self.iniciado):
            self.iniciado = False
            self.pararSistema()
        else:

            self.labelMensajes.setText("El istema no ha sido iniciado")

    def cambiar(self):
        """Valida la peticion enviada por el boton cambiar y ejecuta un cambio."""
        if (self.iniciado):
            self.parar()
            self.cambiarDuracion()
        else:
            self.cambiarDuracion()

    def cambiarDuracion(self):
        """Cambia la duracion de un objeto semaforo elejido por identificador."""
        colaAux = c.Cola()
        while not (c.colaVacia(self.cola)):
            semaforo = c.desencolar(self.cola)

            if semaforo.getIdentificador() == self.spinBoxId.value():
                semaforo.setTiempo(int(self.spinBoxDuracion.value()))
                # print(semaforo)

                self.labelMensajes.setText("¡¡Cambios realizados exitosamente!!")

            c.encolar(colaAux, semaforo)

        while not (c.colaVacia(colaAux)):
            c.encolar(self.cola, c.desencolar(colaAux))
        # c.verCola(self.cola)

    def cambiarLabelEstado(self, semaforo, estado):
        """Cambia el label Semaforo segun su estado actual."""
        if semaforo.getIdentificador() == 1:
            self.labelSemaforo1.setStyleSheet(semaforo.getEstado().get(estado))
        elif semaforo.getIdentificador() == 2:
            self.labelSemaforo2.setStyleSheet(semaforo.getEstado().get(estado))
        elif (semaforo.getIdentificador() == 3):
            self.labelSemaforo3.setStyleSheet(semaforo.getEstado().get(estado))
        elif semaforo.getIdentificador() == 4:
            self.labelSemaforo4.setStyleSheet(semaforo.getEstado().get(estado))

    def pararSistema(self):
        """Desencola los semaforos y se cambia a su estado amarillo simulando un sistema pausado."""

        # Crea una cola auxiliar para encolar los semaforos en ella
        colaAux = c.Cola()
        # Desencola cada semaforo y cambia su estado a "Amarillo"
        while not (c.colaVacia(self.cola)):
            semaforo = c.desencolar(self.cola)
            self.cambiarLabelEstado(semaforo, "amarillo")
            # Encolamos en la cola auxiliar
            c.encolar(colaAux, semaforo)
        # Devuelve los semaforos a la cola original
        while not (c.colaVacia(colaAux)):
            c.encolar(self.cola, c.desencolar(colaAux))

        self.labelMensajes.setText("Sistema en pausa")

    def prepararInicio(self):
        """Desencola los semaforos y se cambia a su estado rojo."""
        # Crea una cola auxiliar para encolar los semaforos en ella
        colaAux = c.Cola()
        # Desencola cada semaforo y cambia su estado a "Amarillo"
        while not (c.colaVacia(self.cola)):
            semaforo = c.desencolar(self.cola)
            self.cambiarLabelEstado(semaforo, "rojo")
            # Encolamos en la cola auxiliar
            c.encolar(colaAux, semaforo)
        # Devuelve los semaforos a la cola original
        while not (c.colaVacia(colaAux)):
            c.encolar(self.cola, c.desencolar(colaAux))

    def iniciarSistema(self):
        """Realiza la rutina de desencolar un semaforo para cambiar su estado y luego encolarlo para pasar al siguiente semaforo."""
        # Ejecuta el loop mientras el sistema este iniciado

        while self.iniciado and c.tamanioCola(self.cola) == 4:
            self.prepararInicio()
            # Desencolamos el Semaforo en curso
            semaforo = c.desencolar(self.cola)

            self.labelMensajes.setText("Semáforo " + str(
                semaforo.getIdentificador()) + " en Curso")
            # Cambia el estado del semaforo a "Verde"
            self.cambiarLabelEstado(semaforo, "verde")

            QtTest.QTest.qWait(int(semaforo.getTiempo() * 1000))

            # Cambia el estado del semaforo a "Amarillo"
            self.cambiarLabelEstado(semaforo, "amarillo")

            # Esperamos dos segundo
            QtTest.QTest.qWait(2000)

            # Cambia el estado del semaforo a "Rojo"
            self.cambiarLabelEstado(semaforo, "rojo")

            # Encolamos el Semaforo en curso
            c.encolar(self.cola, semaforo)

        # Al presionar el boton parar el sistema deja de estar iniciado y realiza la rutina de pausarlo
        if not (self.iniciado):
            self.pararSistema()


def crearColaConSemaforos():
    """Crea un objeto cola con 4 objetos semaforos"""

    cola = c.Cola()
    estado = {"rojo": "border-image: url(:/imgSemaforo/SemaforoImages/Rojo.png);",
              "amarillo": "border-image: url(:/imgSemaforo/SemaforoImages/Amarillo - copia.png);",
              "verde": "border-image: url(:/imgSemaforo/SemaforoImages/Verde.png);"}
    for i in range(1, 5):
        semaforo = s.Semaforo(i, 2, estado)
        c.encolar(cola, semaforo)
    return cola


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = interfazSemaforo()
    widget.show()
    sys.exit(app.exec_())
