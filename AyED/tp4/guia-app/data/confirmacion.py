
from PyQt5.QtWidgets import QDialog
from ui_dialog_confirmar import Ui_dialog_confirmar


class Confirmacion(Ui_dialog_confirmar, QDialog):
    """
    """

    def __init__(self, mensaje=None):
        super().__init__()
        Ui_dialog_confirmar.__init__(self)
        self.setupUi(self)
        self.show()

        self.label_confirmar.setText(mensaje)

        self.acepto = False

        self.boton_aceptar.clicked.connect(self.aceptado)
        self.boton_cancelar.clicked.connect(self.rechazado)

    def aceptado(self):
        self.acepto = True
        self.close()

    def rechazado(self):
        self.close()
