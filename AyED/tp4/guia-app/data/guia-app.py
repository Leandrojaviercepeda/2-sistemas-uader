
import sys

from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidgetItem

from archivo import Archivo
from nodo_archivo import NodoArchivo

from lista import Lista
from criterio import criterio
import hashing as hashing
import validaciones as validaciones

from telefono import Telefono
from contacto import Contacto
from ui_widget_principal import Ui_widget_principal

from confirmacion import Confirmacion



class GuiaApp(Ui_widget_principal, QWidget):
    ARCHIVO = "contactos"

    MSJ_CAMPOS_INCOMPLETOS = "¡Error, todos los campos deben estar completos!"
    MSJ_CARACTERISTICA_INVALIDA = "¡Error, ingrese una caracteristica valida!"
    MSJ_CARACTERES_INVALIDOS = "¡Error, no se permiten los siguientes caracteres '/`#'%><!.[]*$;:?^{}+-\!' !"
    MSJ_CONSULTA_BORRAR = "¿Esta seguro de borrar?"
    MSJ_CONSULTA_EDITAR = "¿Esta seguro de editar?"
    MSJ_CONTACTO_EXISTENTE = "No es posible realizar la operacion, ¡el contacto ya esta en el sistema!"
    MSJ_DIVERGENCIA = "¡No se encontraron coincidencias!"
    MSJ_OPERACION_CANCELADA = "¡Operacion cancelada!"
    MSJ_OPERACION_EXITOSA = "¡Operacion realizada con exito!"
    MSJ_REACTIVACION = "¿El contacto esta desactivado, desea reactivarlo?"
    MSJ_REACTIVACION_EXITOSA = "¡Contacto reactivado con exito!"
    MSJ_PRESIONAR_EDITAR = "¡Complete los campos que desea editar, luego presione nuevamente el boton editar!"
    MSJ_SELECCION_NECESARIA = "¡Primero debe seleccionar un contacto!"
    MSJ_TELEFONO_INVALIDO = "¡Error, los formatos de telefonos validos son: ****-******, ***-*******, **-********!"

    """
    """

    def __init__(self):
        super(GuiaApp, self).__init__()

        Ui_widget_principal.__init__(self)
        self.setupUi(self)

        self.botones = [self.layout_operaciones.itemAt(i).widget() for i in range(self.layout_operaciones.count()) if
                        type(self.layout_operaciones.itemAt(i).widget()) is type(
                            self.layout_operaciones.itemAt(0).widget())]
        self.inputs = [self.layout_campos.itemAt(i).widget() for i in range(self.layout_campos.count()) if
                       type(self.layout_campos.itemAt(i).widget()) is type(self.layout_campos.itemAt(0).widget())]
        self.placeholders_inputs = [dato.placeholderText() for dato in self.inputs]

        self.archivo_contactos = Archivo(GuiaApp.ARCHIVO)  # archivo de contactos
        self.lista_contactos_inactivos = Lista()  # lista con todos los contactos inactivos
        self.lista_contactos = Lista()  # lista con todos los contactos
        self.zonas = hashing.inicializarZonas()  # lista de zonas

        self.inicializarZonasYContactos()

        self.boton_agregar.clicked.connect(self.agregar)
        self.boton_listar.clicked.connect(self.listar)
        self.boton_buscar.clicked.connect(self.buscar)
        self.boton_borrar.clicked.connect(self.borrar)
        self.boton_editar.clicked.connect(self.editar)

    def agregar(self):
        """
        #Agrega un contacto en el archivo si este no esta contenido.
        #Agrega un contacto a la lista de zonas segun corresponda.
        #Agrega un contacto a la lista de todos los contactos.
        """
        todosLosCamposEstanCompletos = self.verificarCamposCompletos()
        hayCaracteresInvalidos = self.verificarCaracteresInvalidos()

        if todosLosCamposEstanCompletos and not (hayCaracteresInvalidos):

            laCaracteristicaEsValida = validaciones.caracteristica(self.input_caracteristica.text())

            elTelefonoEsValido = validaciones.telefono(self.input_caracteristica.text(), self.input_telefono.text())

            if laCaracteristicaEsValida and elTelefonoEsValido:

                datos = self.getInputsText()
                contacto = Contacto(datos[0], datos[1], Telefono(datos[3], datos[4]), datos[2], datos[5])

                noEstaEnLista = hashing.hashing(self.zonas, contacto.telefono.caracteristica).buscar(contacto) is None

                hayUnInactivo = self.lista_contactos_inactivos.buscar(contacto) is not None

                if hayUnInactivo and noEstaEnLista:

                    estaInactivo = self.lista_contactos_inactivos.buscar(contacto).info.info.activo == False

                    if estaInactivo and self.confirmacion(GuiaApp.MSJ_REACTIVACION):
                        nodoArchivo = self.lista_contactos_inactivos.buscar(contacto).info
                        nodoArchivo.info.activo = True
                        posicion = nodoArchivo.indice

                        self.archivo_contactos.modificar(posicion, nodoArchivo)

                        self.respuesta(GuiaApp.MSJ_REACTIVACION_EXITOSA)
                        self.inicializarZonasYContactos()
                        self.cargarTabla(self.lista_contactos)  # refrescamos la tabla


                elif noEstaEnLista:

                    nodo = NodoArchivo(contacto, len(self.archivo_contactos))
                    self.archivo_contactos.append(nodo)  # guarda el nodo en el archivo

                    self.respuesta(GuiaApp.MSJ_OPERACION_EXITOSA)
                    self.inicializarZonasYContactos()
                    self.cargarTabla(self.lista_contactos)  # refrescamos la tabla

                else:
                    self.avisar(GuiaApp.MSJ_CONTACTO_EXISTENTE)

            else:
                if not (laCaracteristicaEsValida):
                    self.avisar(GuiaApp.MSJ_CARACTERISTICA_INVALIDA)

                elif not (elTelefonoEsValido):
                    self.avisar(GuiaApp.MSJ_TELEFONO_INVALIDO)

        elif not todosLosCamposEstanCompletos:
            self.avisar(GuiaApp.MSJ_CAMPOS_INCOMPLETOS)
        elif hayCaracteresInvalidos:
            self.avisar(GuiaApp.MSJ_CARACTERES_INVALIDOS)

    def borrar(self):
        """
        #Hace una baja logica de un contacto.
        """
        datosContacto = self.obtenerFilaTabla()
        noSeleccionoUnaFila = len(datosContacto) == 0

        if (noSeleccionoUnaFila):
            self.avisar(GuiaApp.MSJ_SELECCION_NECESARIA)
            self.limpiarInputs()
            self.soloLecturaInputs(True)
            self.borrar()
        else:
            self.setInputsText(datosContacto)

            if self.confirmacion(GuiaApp.MSJ_CONSULTA_BORRAR):

                contacto = Contacto(datosContacto[0], datosContacto[1], Telefono(datosContacto[4], datosContacto[5]),
                                    datosContacto[2], datosContacto[3])
                nodoArchivo = hashing.hashing(self.zonas, datosContacto[4]).buscar(
                    contacto).info  # obtenemos el nodoArchivo
                posicion = nodoArchivo.indice  # obtenemos el indice del nodoArchivo
                nodoArchivo.info.activo = False  # hacemos la baja logica

                self.archivo_contactos.modificar(posicion, nodoArchivo)  # guardamos el nodoArchivo dado de baja

                self.respuesta(GuiaApp.MSJ_OPERACION_EXITOSA)
                self.soloLecturaInputs(False)
                self.inicializarZonasYContactos()
                self.cargarTabla(self.lista_contactos)  # refrescamos la tabla
            else:
                self.respuesta(GuiaApp.MSJ_OPERACION_CANCELADA)

    def editar(self):
        """
        #Edita de un contacto.
        """

        datosContacto = self.obtenerFilaTabla()

        noSeleccionoUnaFila = len(datosContacto) == 0

        if (noSeleccionoUnaFila):
            self.avisar(GuiaApp.MSJ_SELECCION_NECESARIA)
            self.limpiarInputs()
            self.editar()
        else:

            self.setPlaceholders(datosContacto)  # completamos los campos con los elementos de la tabla
            self.boton_editar.setCheckable(True)

            def esperar_edicion(self):
                self.avisar(GuiaApp.MSJ_PRESIONAR_EDITAR)

            if self.boton_editar.isChecked():

                contactoEditado = self.obtenerContactoEditado()

                self.boton_editar.setCheckable(False)

                laCaracteristicaEsValida = validaciones.caracteristica(contactoEditado.telefono.caracteristica)
                elTelefonoEsValido = validaciones.telefono(contactoEditado.telefono.caracteristica,
                                                           contactoEditado.telefono.numero)
                hayCaracteresInvalidos = self.verificarCaracteresInvalidos()

                if laCaracteristicaEsValida and elTelefonoEsValido and not (hayCaracteresInvalidos):

                    contacto = Contacto(datosContacto[0], datosContacto[1],
                                        Telefono(datosContacto[4], datosContacto[5]), datosContacto[2],
                                        datosContacto[3])

                    hayUnInactivo = self.lista_contactos_inactivos.buscar(contactoEditado) is not None
                    esElMismoContacto = contacto == contactoEditado

                    estaEnLista = hashing.hashing(self.zonas, contactoEditado.telefono.caracteristica).buscar(
                        contactoEditado)

                    if hayUnInactivo and not (estaEnLista):

                        estaInactivo = self.lista_contactos_inactivos.buscar(contactoEditado).info.info.activo == False

                        if estaInactivo and self.confirmacion(GuiaApp.MSJ_REACTIVACION):
                            nodoArchivo = self.lista_contactos_inactivos.buscar(contactoEditado).info
                            nodoArchivo.info = contactoEditado
                            nodoArchivo.info.activo = True
                            posicion = nodoArchivo.indice

                            self.archivo_contactos.modificar(posicion, nodoArchivo)  # guardamos el nodoArchivo nuevo

                            self.respuesta(GuiaApp.MSJ_REACTIVACION_EXITOSA)
                            self.restaurarPlaceholders()
                            self.inicializarZonasYContactos()  # refrescamos las listas
                            self.cargarTabla(hashing.hashing(self.zonas,
                                                             contactoEditado.telefono.caracteristica))  # refrescamos la tabla

                    elif esElMismoContacto and self.confirmacion(GuiaApp.MSJ_CONSULTA_EDITAR) or not (
                            esElMismoContacto) and not (estaEnLista) and self.confirmacion(GuiaApp.MSJ_CONSULTA_EDITAR):

                        nodoArchivo = hashing.hashing(self.zonas, contacto.telefono.caracteristica).buscar(
                            contacto).info  # obtenemos el nodoArchivo
                        nodoArchivo.info = contactoEditado  # pisamos el contacto viejo
                        posicion = nodoArchivo.indice  # obtenemos el indice del nodoArchivo

                        self.archivo_contactos.modificar(posicion, nodoArchivo)  # guardamos el nodoArchivo nuevo

                        self.respuesta(GuiaApp.MSJ_OPERACION_EXITOSA)
                        self.restaurarPlaceholders()
                        self.inicializarZonasYContactos()
                        self.cargarTabla(hashing.hashing(self.zonas,
                                                         contactoEditado.telefono.caracteristica))  # refrescamos la tabla

                    elif estaEnLista and not (esElMismoContacto):
                        self.respuesta(GuiaApp.MSJ_CONTACTO_EXISTENTE)

                    else:
                        self.respuesta(GuiaApp.MSJ_OPERACION_CANCELADA)
                        self.restaurarPlaceholders()
                else:
                    if not (laCaracteristicaEsValida):
                        self.avisar(GuiaApp.MSJ_CARACTERISTICA_INVALIDA)

                    elif not (elTelefonoEsValido):
                        self.avisar(GuiaApp.MSJ_TELEFONO_INVALIDO)

                    elif hayCaracteresInvalidos:
                        self.avisar(GuiaApp.MSJ_CARACTERES_INVALIDOS)
            else:
                while self.boton_editar.isCheckable():
                    esperar_edicion(self)

    def buscar(self):
        """
        #Busca un elemento en la lista de contactos, si esta lo contiene, es listado en la tabla.
        """
        lista = Lista()

        for contacto in range(len(self.lista_contactos)):

            esIgualAlBuscado = criterio(self.lista_contactos.obtener(contacto),
                                        self.combo_buscar.currentText()) == self.input_buscar.text()

            if esIgualAlBuscado:
                lista.insertar(self.lista_contactos.obtener(contacto), self.combo_buscar.currentText())

        if lista.esVacia():
            self.avisar(GuiaApp.MSJ_DIVERGENCIA)

        else:
            self.cargarTabla(lista)

    def listar(self):
        """
        #Lista segun el campo seleccionado.
        """
        lista = Lista()

        for contacto in range(len(self.lista_contactos)):
            lista.insertar(self.lista_contactos.obtener(contacto), self.combo_listar.currentText())

        self.cargarTabla(lista)

    def cargarTabla(self, lista):
        """
        #Carga en la tabla todos los elementos.
        """
        self.tabla_listado.clearContents()

        for i in range(len(lista)):
            self.tabla_listado.setRowCount(i + 1)
            # accedemos a los campos nombre, apellido, etc del nodo archivo obtenido de la lista
            self.tabla_listado.setItem(i, 0, QTableWidgetItem("%s" % lista.obtener(i).info.nombre))
            self.tabla_listado.setItem(i, 1, QTableWidgetItem("%s" % lista.obtener(i).info.apellido))
            self.tabla_listado.setItem(i, 2, QTableWidgetItem("%s" % lista.obtener(i).info.localidad))
            self.tabla_listado.setItem(i, 3, QTableWidgetItem("%s" % lista.obtener(i).info.direccion))
            self.tabla_listado.setItem(i, 4, QTableWidgetItem(
                "%s-%s" % (lista.obtener(i).info.telefono.caracteristica, lista.obtener(i).info.telefono.numero)))

    def confirmacion(self, mensaje=None):
        """
        #Crea un dialogo de confirmacion y envia una respuesta booleana.
        #@return boolean
        """
        mensaje = Confirmacion(mensaje)
        mensaje.exec_()
        return mensaje.acepto

    def avisar(self, mensaje):
        """
        #Dado un mensaje crea un aviso.
        """
        self.label_avisos.setText(mensaje)
        QtTest.QTest.qWait(2500)
        self.label_avisos.clear()

    def inicializarZonasYContactos(self):
        """
        #Inicializa una lista de zonas y una lista con todos los contactos.
        """
        self.lista_contactos_inactivos = Lista()
        self.lista_contactos = Lista()
        self.zonas = hashing.inicializarZonas()

        for nodo in range(len(self.archivo_contactos)):

            nodoArchivo = self.archivo_contactos.leer(nodo)
            estaDadoDeAlta = nodoArchivo.info.activo is True

            if estaDadoDeAlta:

                caracteristica = int(
                    nodoArchivo.info.telefono.caracteristica)  # obtenemos cada caracteristica de cada contacto
                hashing.hashing(self.zonas, caracteristica).append(
                    nodoArchivo)  # cargamos cada zona correspondiente con los contactos activos
                self.lista_contactos.append(nodoArchivo)  # cargamos una lista() con todos los contactos activos
            else:
                self.lista_contactos_inactivos.append(
                    nodoArchivo)  # cargamos una lista() con todos los contactos inactivos

    def verificarCamposCompletos(self):
        """
        Devuelve True si todos los campos estan completos, False caso contrario.
        @return boolean
        """
        for i in self.inputs:
            estaVacio = len(i.text()) == 0
            if estaVacio:
                return False
        return True

    def verificarCaracteresInvalidos(self):
        """
        Devuelve True si ningun campo contiene caracteres no permitidos
        @return boolean
        """
        for i in self.inputs:
            return validaciones.caracteresEspeciales(i.text())

    def respuesta(self, mensaje):

        self.avisar(mensaje)
        self.limpiarInputs()
        self.soloLecturaInputs(False)

    def obtenerFilaTabla(self):
        """
        Una vez seleccionada la fila de la tabla, obtiene cada una de las columnas asociadas a la fila,
        la columna telefono la separa en caracteristica y numero.
        
        @return list
        """
        fila = [campo.text() for campo in (self.tabla_listado.selectedItems())]
        listaUtil = []

        for columna in fila:

            if "-" in columna:
                aux = columna.split("-")
                listaUtil.append(aux[0])
                listaUtil.append(aux[1])
            else:
                listaUtil.append(columna)

        return listaUtil

    def setInputsText(self, lista):
        """
        #Carga los imputs dada una lista de datos de una fila de la tabla.
        """
        for i, d in enumerate(lista):
            self.inputs[i].setText(d)

    def restaurarPlaceholders(self):
        "Devuelve el placeholder de cada input a su estado inicial."

        self.input_nombre.setPlaceholderText(self.placeholders_inputs[0])
        self.input_apellido.setPlaceholderText(self.placeholders_inputs[1])
        self.input_caracteristica.setPlaceholderText(self.placeholders_inputs[3])
        self.input_telefono.setPlaceholderText(self.placeholders_inputs[4])
        self.input_direccion.setPlaceholderText(self.placeholders_inputs[2])
        self.input_localidad.setPlaceholderText(self.placeholders_inputs[5])

    def setPlaceholders(self, lista):
        """
        Dada una lista, setea los valores en un placeholder.
        """
        self.input_nombre.setPlaceholderText(lista[0])
        self.input_apellido.setPlaceholderText(lista[1])
        self.input_caracteristica.setPlaceholderText(lista[4])
        self.input_telefono.setPlaceholderText(lista[5])
        self.input_direccion.setPlaceholderText(lista[3])
        self.input_localidad.setPlaceholderText(lista[2])

    def getPlaceholders(self):
        return [validaciones.upperLowerWord(p.placeholderText()) for p in self.inputs]

    def getInputsText(self):
        return [validaciones.upperLowerWord(campo.text()) for campo in self.inputs]

    def obtenerContactoEditado(self):
        """
        """
        datosContacto = []

        camposEditados = self.getInputsText()

        for i, p in enumerate(self.getPlaceholders()):
            if camposEditados[i] == "":
                datosContacto.append(p)
            else:
                datosContacto.append(camposEditados[i])

        return Contacto(datosContacto[0], datosContacto[1], Telefono(datosContacto[3], datosContacto[4]),
                        datosContacto[2], datosContacto[5])

    def mostrarInputs(self, boolean=False):

        for i in self.inputs:
            i.setEnabled(boolean)

    def soloLecturaInputs(self, boolean=False):

        for i in self.inputs:
            i.setReadOnly(boolean)

    def mostrarBotones(self, boolean=False, boton=None, combo=None):

        for b in self.botones:
            if b != boton:
                b.setEnabled(boolean)

    def restaurarBotones(self):
        for b in self.botones:
            b.setEnabled(True)

    def limpiarInputs(self):

        for i in self.inputs:
            i.clear()

    def prueba(self):
        print("funcionando")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuiaApp()
    ex.show()
    sys.exit(app.exec_())
