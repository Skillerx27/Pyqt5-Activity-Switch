# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_otherWindow(object):
    def setupUi(self, otherWindow):
        otherWindow.setObjectName("otherWindow")
        otherWindow.resize(619, 313)
        self.label = QtWidgets.QLabel(otherWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 411, 91))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(otherWindow)
        QtCore.QMetaObject.connectSlotsByName(otherWindow)

    def retranslateUi(self, otherWindow):
        _translate = QtCore.QCoreApplication.translate
        otherWindow.setWindowTitle(_translate("otherWindow", "Dialog"))
        self.label.setText(_translate("otherWindow", "WELCOME TO TIC-TAC-TOE GAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherWindow = QtWidgets.QDialog()
    ui = Ui_otherWindow()
    ui.setupUi(otherWindow)
    otherWindow.show()
    sys.exit(app.exec_())

