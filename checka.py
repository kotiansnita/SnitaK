# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checka.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import m8
import mysql.connector
import sys

class Ui_otherwindow1_3(object):
    def check(self):
        query="select *from medicine"
        cor = mysql.connector.connect(host="localhost", user="ph", passwd="pass", db="sni")
        conn = cor.cursor()
        conn.execute(query)
        result = conn.fetchall()

        self.tableWidget.setRowCount(0)


        print('res',result)

        for row_number,row_data in enumerate(result):
            print(row_number,"---")
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(column_number)
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        conn.close()


    def setupUi(self, otherwindow1_3):
        otherwindow1_3.setObjectName("otherwindow1_3")
        otherwindow1_3.resize(973, 641)
        otherwindow1_3.setStyleSheet("border-image:url(:/newPrefix/14.jpg)")
        self.centralwidget = QtWidgets.QWidget(otherwindow1_3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(352, 25, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(282, 115, 431, 351))
        self.tableWidget.setStyleSheet("border-image:url(:/newPrefix/a2.jpg)")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(412, 505, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_check.setFont(font)
        self.btn_check.setStyleSheet("border-image:url(:/newPrefix/PicsArt_1539249712352.jpg)")
        self.btn_check.setObjectName("btn_check")

        self.btn_check.clicked.connect(self.check)

        otherwindow1_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(otherwindow1_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 21))
        self.menubar.setObjectName("menubar")
        otherwindow1_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(otherwindow1_3)
        self.statusbar.setObjectName("statusbar")
        otherwindow1_3.setStatusBar(self.statusbar)

        self.retranslateUi(otherwindow1_3)
        QtCore.QMetaObject.connectSlotsByName(otherwindow1_3)

    def retranslateUi(self, otherwindow1_3):
        _translate = QtCore.QCoreApplication.translate
        otherwindow1_3.setWindowTitle(_translate("otherwindow1_3", "MainWindow"))
        self.label.setText(_translate("otherwindow1_3", "CHECK AVAILABILITY"))
        self.btn_check.setText(_translate("otherwindow1_3", "CHECK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherwindow1_3 = QtWidgets.QMainWindow()
    ui = Ui_otherwindow1_3()
    ui.setupUi(otherwindow1_3)
    otherwindow1_3.show()
    sys.exit(app.exec_())

