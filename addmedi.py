# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmedi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m6
import mysql.connector
import sys
import os

class Ui_obj2(object):
    def print1(self):
        print('print is clicked')
        m_nm = self.textEdit_1.text()
        exp_dt = self.textEdit_2.text()
        m_qty = self.textEdit_3.text()
        m_price = self.textEdit_4.text()

        conn = mysql.connector.connect(host="localhost", user="ph", passwd="pass", db="sni")
        cur = conn.cursor()

        # cur.execute("create database pharma")
        # conn.commit()
        # cur.execute("""use pharma""")
        # cur.execute('CREATE TABLE medicine(m_nm varchar(45),exp_dt date,m_qty int(11),m_price int(11)')

        cur.execute("INSERT INTO medicine(m_nm,exp_dt,m_qty,m_price) values(%s,%s,%s,%s)", (m_nm, exp_dt, m_qty, m_price))
        print('data inserted successfully')
        conn.commit()
        cur.close()
        conn.close()

    def setupUi(self, obj2):
        obj2.setObjectName("obj2")
        obj2.resize(1395, 646)
        obj2.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539338412363.jpg)")
        self.centralwidget = QtWidgets.QWidget(obj2)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(435, 555, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.print1)
        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(373, 448, 421, 41))
        self.textEdit_4.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(373, 198, 421, 41))
        self.textEdit_1.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_1.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(201, 195, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(375, 365, 421, 41))
        self.textEdit_3.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(373, 278, 421, 41))
        self.textEdit_2.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(201, 275, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(201, 365, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(201, 445, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_5.setObjectName("label_5")
        obj2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(obj2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 21))
        self.menubar.setObjectName("menubar")
        obj2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(obj2)
        self.statusbar.setObjectName("statusbar")
        obj2.setStatusBar(self.statusbar)

        self.retranslateUi(obj2)
        QtCore.QMetaObject.connectSlotsByName(obj2)

    def retranslateUi(self, obj2):
        _translate = QtCore.QCoreApplication.translate
        obj2.setWindowTitle(_translate("obj2", "MainWindow"))
        self.btn_add.setText(_translate("obj2", "ADD"))
        self.label_2.setText(_translate("obj2", "Name"))
        self.label_3.setText(_translate("obj2", "EXP. DATE"))
        self.label_4.setText(_translate("obj2", "QUANTITY"))
        self.label_5.setText(_translate("obj2", "PRICE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj2 = QtWidgets.QMainWindow()
    ui = Ui_obj2()
    ui.setupUi(obj2)
    obj2.show()
    sys.exit(app.exec_())

