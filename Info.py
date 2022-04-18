# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(600, 700)
        Info.setMaximumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")
        self.AffInfo = QtWidgets.QTextEdit(self.centralwidget)
        self.AffInfo.setGeometry(QtCore.QRect(20, 10, 560, 591))
        self.AffInfo.setMaximumSize(QtCore.QSize(560, 600))
        self.AffInfo.setObjectName("AffInfo")
        self.MajInfo = QtWidgets.QPushButton(self.centralwidget)
        self.MajInfo.setGeometry(QtCore.QRect(240, 610, 111, 40))
        self.MajInfo.setMaximumSize(QtCore.QSize(120, 40))
        self.MajInfo.setObjectName("MajInfo")
        Info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Info)
        self.statusbar.setObjectName("statusbar")
        Info.setStatusBar(self.statusbar)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Informations du Routeur"))
        self.MajInfo.setText(_translate("Info", "Mise a jour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info = QtWidgets.QMainWindow()
    ui = Ui_Info()
    ui.setupUi(Info)
    Info.show()
    sys.exit(app.exec_())

