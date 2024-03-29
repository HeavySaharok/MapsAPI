import PyQt5

import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from get_image import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ПУНКТ 3")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(340, 440, 98, 29))
        self.save.setObjectName("save")
        self.massh = QtWidgets.QLineEdit(self.centralwidget)
        self.massh.setGeometry(QtCore.QRect(70, 380, 191, 41))
        self.massh.setObjectName("massh")
        self.massh.setEnabled(False)

        self.coord = QtWidgets.QLineEdit(self.centralwidget)
        self.coord.setGeometry(QtCore.QRect(540, 380, 171, 41))
        self.coord.setObjectName("coord")
        self.coord.setEnabled(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 561, 331))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")



        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save.setText(_translate("MainWindow", "сохранить"))
        self.massh.setText(_translate("MainWindow", "масштаб"))
        self.coord.setText(_translate("MainWindow", "координаты"))
        self.massh.setText('0.005,0.005')
        self.coord.setText('66,66')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save.clicked.connect(self.show_map)

    # отображает картинку
    def show_map(self):
        ll, spn = '66,66', '0.005,0.005'
        get_image(ll, spn)

        self.label.setPixmap(QPixmap('map.png'))

    def coord_mas(self):
        '''
        return: self.coord, self.massh
        '''
        return self.coord.text(), self.massh.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())