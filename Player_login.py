# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Player_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from secondwindow import Ui_otherWindow

class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_otherWindow()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 490)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 410, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.player1 = QtWidgets.QLabel(Dialog)
        self.player1.setGeometry(QtCore.QRect(210, 210, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player1.setFont(font)
        self.player1.setObjectName("player1")
        self.player2 = QtWidgets.QLabel(Dialog)
        self.player2.setGeometry(QtCore.QRect(210, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.player2.setFont(font)
        self.player2.setObjectName("player2")
        self.p1 = QtWidgets.QLineEdit(Dialog)
        self.p1.setGeometry(QtCore.QRect(410, 220, 131, 31))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QLineEdit(Dialog)
        self.p2.setGeometry(QtCore.QRect(410, 300, 131, 31))
        self.p2.setObjectName("p2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.detail)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Python GUI"))
        self.pushButton.setText(_translate("Dialog", "Start Game"))
        self.player1.setText(_translate("Dialog", "Player 1"))
        self.player2.setText(_translate("Dialog", "Player 2"))


    def detail(self):
        print("ASD")
        a = self.p1.text()
        b = self.p2.text()

        self.openWindow()
        print(a,b)


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 290)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "WELCOME TO TIC-TAC-TOE"))









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

