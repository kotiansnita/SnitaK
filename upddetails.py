# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upddetails.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m5
from updatemedi import Ui_obj1
from addmedi import Ui_obj2
from delmedi import Ui_obj3

class Ui_nobj(object):

    def openWindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_obj1()
        self.ui2.setupUi(self.window)
        self.window.show()

    def openWindow6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_obj2()
        self.ui2.setupUi(self.window)
        self.window.show()

    def openWindow7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_obj3()
        self.ui2.setupUi(self.window)
        self.window.show()

    def setupUi(self, nobj):
        nobj.setObjectName("nobj")
        nobj.resize(1392, 785)
        nobj.setStyleSheet("border-image:url(:/newPrefix/q10.jpg)")
        self.centralwidget = QtWidgets.QWidget(nobj)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_addmedi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addmedi.setGeometry(QtCore.QRect(930, 154, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addmedi.setFont(font)
        self.btn_addmedi.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_addmedi.setObjectName("btn_addmedi")

        self.btn_addmedi.clicked.connect(self.openWindow6)

        self.btn_delmedi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delmedi.setGeometry(QtCore.QRect(930, 284, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delmedi.setFont(font)
        self.btn_delmedi.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_delmedi.setObjectName("btn_delmedi")

        self.btn_delmedi.clicked.connect(self.openWindow7)

        self.btn_updatemedi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_updatemedi.setGeometry(QtCore.QRect(930, 414, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_updatemedi.setFont(font)
        self.btn_updatemedi.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_updatemedi.setObjectName("btn_updatemedi")

        self.btn_updatemedi.clicked.connect(self.openWindow5)

        nobj.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(nobj)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1392, 21))
        self.menubar.setObjectName("menubar")
        nobj.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(nobj)
        self.statusbar.setObjectName("statusbar")
        nobj.setStatusBar(self.statusbar)

        self.retranslateUi(nobj)
        QtCore.QMetaObject.connectSlotsByName(nobj)

    def retranslateUi(self, nobj):
        _translate = QtCore.QCoreApplication.translate
        nobj.setWindowTitle(_translate("nobj", "MainWindow"))
        self.btn_addmedi.setText(_translate("nobj", "ADD MEDICINE"))
        self.btn_delmedi.setText(_translate("nobj", "DELETE MEDICINE"))
        self.btn_updatemedi.setText(_translate("nobj", "UPDATE DETAILS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nobj = QtWidgets.QMainWindow()
    ui = Ui_nobj()
    ui.setupUi(nobj)
    nobj.show()
    sys.exit(app.exec_())

