# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Principal import Ui_Principal

class Ui_Accueil(object):
    
    def suivant(self):
        self.Fprincipale =QtWidgets.QMainWindow()
        self.ui = Ui_Principal()
        self.ui.setupUi(self.Fprincipale)
        self.Fprincipale.show()
        Accueil.hide()
        
    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.resize(440, 240)
        Accueil.setMaximumSize(QtCore.QSize(440, 240))
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(150, 130, 111, 31))
        self.open.setObjectName("open")
        
        self.open.clicked.connect(self.suivant)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 341, 91))
        self.label.setObjectName("label")
        Accueil.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Accueil)
        self.statusbar.setObjectName("statusbar")
        Accueil.setStatusBar(self.statusbar)

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Configuration des Routeurs"))
        self.open.setText(_translate("Accueil", "Cliquez ici Continuer"))
        self.label.setText(_translate("Accueil", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">Bienvenue dans la configuration de</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\"> vos Routeurs</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

