# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delmedi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m7
import mysql.connector
import sys
import os

class Ui_obj3(object):

    def print1(self):
        print('print is clicked')
        m_nm = self.textEdit_1.text()

        print(m_nm,"==>")
        conn = mysql.connector.connect(host="localhost", user="ph", passwd="pass", db="sni")
        cur = conn.cursor()

        # cur.execute("create database sni")
        # conn.commit()
        # cur.execute("""use sni""")
        # cur.execute('CREATE TABLE medicine(m_nm varchar(45),exp_dt date,m_qty int(11),m_price int(11)')
        print("DELETE FROM medicine WHERE m_nm = \'{}\'".format(m_nm))
        cur.execute("DELETE FROM medicine WHERE m_nm = \'{}\'".format(m_nm))
        print('data deleted successfully')
        conn.commit()
        cur.close()
        conn.close()

    def setupUi(self, obj3):
        obj3.setObjectName("obj3")
        obj3.resize(1432, 787)
        obj3.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539338549843.jpg)")
        self.centralwidget = QtWidgets.QWidget(obj3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 280, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label.setObjectName("label")
        self.textEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(300, 290, 471, 61))
        self.textEdit_1.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_1.setObjectName("textEdit_1")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(280, 470, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.print1)
        obj3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(obj3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1432, 21))
        self.menubar.setObjectName("menubar")
        obj3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(obj3)
        self.statusbar.setObjectName("statusbar")
        obj3.setStatusBar(self.statusbar)

        self.retranslateUi(obj3)
        QtCore.QMetaObject.connectSlotsByName(obj3)

    def retranslateUi(self, obj3):
        _translate = QtCore.QCoreApplication.translate
        obj3.setWindowTitle(_translate("obj3", "MainWindow"))
        self.label.setText(_translate("obj3", "NAME"))
        self.btn_delete.setText(_translate("obj3", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj3 = QtWidgets.QMainWindow()
    ui = Ui_obj3()
    ui.setupUi(obj3)
    obj3.show()
    sys.exit(app.exec_())
