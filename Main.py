# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m1
from Pharmacy import Ui_MainWindow1

class Ui_NewMainWindow(object):

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, NewMainWindow):
        NewMainWindow.setObjectName("NewMainWindow")
        NewMainWindow.resize(1253, 758)
        NewMainWindow.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539238548252.jpg)")
        self.centralwidget = QtWidgets.QWidget(NewMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(580, 280, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("border-image:url(:/newPrefix/b2.jpg)")
        self.btn_start.setObjectName("btn_start")

        self.btn_start.clicked.connect(self.openWindow1)

        NewMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1253, 21))
        self.menubar.setObjectName("menubar")
        NewMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewMainWindow)
        self.statusbar.setObjectName("statusbar")
        NewMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewMainWindow)
        QtCore.QMetaObject.connectSlotsByName(NewMainWindow)

    def retranslateUi(self, NewMainWindow):
        _translate = QtCore.QCoreApplication.translate
        NewMainWindow.setWindowTitle(_translate("NewMainWindow", "MainWindow"))
        self.btn_start.setText(_translate("NewMainWindow", "START"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewMainWindow = QtWidgets.QMainWindow()
    ui = Ui_NewMainWindow()
    ui.setupUi(NewMainWindow)
    NewMainWindow.show()
    sys.exit(app.exec_())

