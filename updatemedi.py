# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatemedi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m4
import mysql.connector
import sys
import os

#old name
#new name
#old price
#new price
#qty
#exp_dt

class Ui_obj1(object):
    def print1(self):

        m_nm = self.textEdit_7.text()
        m_nm= self.textEdit_8.text()

        query = "UPDATE medicine SET m_nm = '%s' WHERE n_mn;" % m_nm
        cor = mysql.connector.connect(host="localhost", user="ph", passwd="pass", db="sni")
        conn = cor.cursor()
        conn.execute(query)

        print('print is clicked')


        #m_price = self.textEdit_12.text()
        #m_price = self.textEdit_11.text()

        #m_qty = self.textEdit_9.text()
        #exp_dt = self.textEdit_10.text()
        print(m_nm,"==>")

        cor.commit()
        conn.close()
        cor.close()

        # cur.execute("create database pharma")
        # conn.commit()
        # cur.execute("""use pharma""")
        # cur.execute('CREATE TABLE medicine(m_nm varchar(45),exp_dt date,m_qty int(11),m_price int(11)')



        #cur.execute("UPDATE medicine SET m_nm=\'\' WHERE m_nm = \'\'".format(m_nm).format(m_nm))
       # print('data updated successfully')


    def setupUi(self, obj1):
        obj1.setObjectName("obj1")
        obj1.resize(1325, 1076)
        obj1.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539323620956.jpg)")
        self.centralwidget = QtWidgets.QWidget(obj1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(426, 276, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(426, 344, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(426, 484, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_10.setObjectName("label_10")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(616, 624, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_ok.setObjectName("btn_ok")

        self.btn_ok.clicked.connect(self.print1)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(426, 214, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_11.setObjectName("label_11")
        self.textEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(536, 214, 341, 41))
        self.textEdit_7.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(536, 274, 341, 41))
        self.textEdit_8.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(536, 484, 341, 41))
        self.textEdit_9.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(536, 554, 341, 41))
        self.textEdit_10.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_10.setObjectName("textEdit_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(426, 414, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_12.setObjectName("label_12")
        self.textEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(536, 414, 341, 41))
        self.textEdit_11.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(426, 554, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label_13.setObjectName("label_13")
        self.textEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(536, 344, 341, 41))
        self.textEdit_12.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.textEdit_12.setObjectName("textEdit_12")
        obj1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(obj1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1325, 21))
        self.menubar.setObjectName("menubar")
        obj1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(obj1)
        self.statusbar.setObjectName("statusbar")
        obj1.setStatusBar(self.statusbar)

        self.retranslateUi(obj1)
        QtCore.QMetaObject.connectSlotsByName(obj1)

    def retranslateUi(self, obj1):
        _translate = QtCore.QCoreApplication.translate
        obj1.setWindowTitle(_translate("obj1", "MainWindow"))
        self.label_8.setText(_translate("obj1", "NEW NAME"))
        self.label_9.setText(_translate("obj1", "OLD PRICE"))
        self.label_10.setText(_translate("obj1", "QUANTITY"))
        self.btn_ok.setText(_translate("obj1", "OK"))
        self.label_11.setText(_translate("obj1", "OLD NAME"))
        self.label_12.setText(_translate("obj1", "NEW PRICE"))
        self.label_13.setText(_translate("obj1", "EXP DATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj1 = QtWidgets.QMainWindow()
    ui = Ui_obj1()
    ui.setupUi(obj1)
    obj1.show()
    sys.exit(app.exec_())

