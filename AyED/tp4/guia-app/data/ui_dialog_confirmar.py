
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_confirmar(object):
    def setupUi(self, dialog_confirmar):
        dialog_confirmar.setObjectName("dialog_confirmar")
        dialog_confirmar.resize(400, 160)
        dialog_confirmar.setMinimumSize(QtCore.QSize(400, 160))
        dialog_confirmar.setMaximumSize(QtCore.QSize(400, 160))
        self.label_confirmar = QtWidgets.QLabel(dialog_confirmar)
        self.label_confirmar.setGeometry(QtCore.QRect(0, 30, 401, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_confirmar.setFont(font)
        self.label_confirmar.setText("")
        self.label_confirmar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_confirmar.setObjectName("label_confirmar")
        self.layoutWidget = QtWidgets.QWidget(dialog_confirmar)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 110, 262, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_cancelar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_cancelar.setMinimumSize(QtCore.QSize(100, 20))
        self.boton_cancelar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_cancelar.setAutoDefault(False)
        self.boton_cancelar.setObjectName("boton_cancelar")
        self.horizontalLayout.addWidget(self.boton_cancelar)
        self.boton_aceptar = QtWidgets.QPushButton(self.layoutWidget)
        self.boton_aceptar.setMinimumSize(QtCore.QSize(100, 20))
        self.boton_aceptar.setMaximumSize(QtCore.QSize(45, 45))
        self.boton_aceptar.setAutoDefault(False)
        self.boton_aceptar.setObjectName("boton_aceptar")
        self.horizontalLayout.addWidget(self.boton_aceptar)

        self.retranslateUi(dialog_confirmar)
        QtCore.QMetaObject.connectSlotsByName(dialog_confirmar)

    def retranslateUi(self, dialog_confirmar):
        _translate = QtCore.QCoreApplication.translate
        dialog_confirmar.setWindowTitle(_translate("dialog_confirmar", "Mensaje"))
        self.boton_cancelar.setText(_translate("dialog_confirmar", "Cancelar"))
        self.boton_aceptar.setText(_translate("dialog_confirmar", "Aceptar"))


from recursos import imagenes_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog_confirmar = QtWidgets.QDialog()
    ui = Ui_dialog_confirmar()
    ui.setupUi(dialog_confirmar)
    dialog_confirmar.show()
    sys.exit(app.exec_())
