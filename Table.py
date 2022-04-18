# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Table(object):
    def setupUi(self, Table):
        Table.setObjectName("Table")
        Table.resize(600, 350)
        Table.setMaximumSize(QtCore.QSize(600, 350))
        self.centralwidget = QtWidgets.QWidget(Table)
        self.centralwidget.setObjectName("centralwidget")
        self.AffTR = QtWidgets.QTextEdit(self.centralwidget)
        self.AffTR.setGeometry(QtCore.QRect(10, 10, 570, 240))
        self.AffTR.setMaximumSize(QtCore.QSize(570, 240))
        self.AffTR.setObjectName("AffTR")
        self.MajTable = QtWidgets.QPushButton(self.centralwidget)
        self.MajTable.setGeometry(QtCore.QRect(260, 260, 111, 40))
        self.MajTable.setMaximumSize(QtCore.QSize(120, 40))
        self.MajTable.setObjectName("MajTable")
        Table.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Table)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Table.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Table)
        self.statusbar.setObjectName("statusbar")
        Table.setStatusBar(self.statusbar)

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "Table de Routage"))
        self.MajTable.setText(_translate("Table", "Mise a jour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Table = QtWidgets.QMainWindow()
    ui = Ui_Table()
    ui.setupUi(Table)
    Table.show()
    sys.exit(app.exec_())

