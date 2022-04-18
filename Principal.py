# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(500, 150)
        Principal.setMaximumSize(QtCore.QSize(500, 150))
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 450, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(450, 100))
        self.groupBox.setObjectName("Routeurs")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(40, 30, 370, 40))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.R1 = QtWidgets.QPushButton(self.splitter)
        self.R1.setMaximumSize(QtCore.QSize(120, 40))
        self.R1.setObjectName("R1")
        self.R2 = QtWidgets.QPushButton(self.splitter)
        self.R2.setMaximumSize(QtCore.QSize(120, 40))
        self.R2.setObjectName("R2")
        self.R3 = QtWidgets.QPushButton(self.splitter)
        self.R3.setMaximumSize(QtCore.QSize(120, 40))
        self.R3.setObjectName("R3")
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)
        self.actionEnregistrer = QtWidgets.QAction(Principal)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionOuvrir = QtWidgets.QAction(Principal)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionQuitter = QtWidgets.QAction(Principal)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Principal"))
        self.groupBox.setTitle(_translate("Principal", "Routeurs"))
        self.R1.setText(_translate("Principal", "Routeur 1"))
        self.R2.setText(_translate("Principal", "Routeur 2"))
        self.R3.setText(_translate("Principal", "Routeur 3"))
        self.menuFichier.setTitle(_translate("Principal", "Fichier"))
        self.actionEnregistrer.setText(_translate("Principal", "Enregistrer"))
        self.actionOuvrir.setText(_translate("Principal", "Ouvrir"))
        self.actionQuitter.setText(_translate("Principal", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())

