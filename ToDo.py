# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToDo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_AddItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.adicionar())
        self.btn_AddItem.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.btn_AddItem.setObjectName("btn_AddItem")
        self.btn_DeleteItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remover())
        self.btn_DeleteItem.setGeometry(QtCore.QRect(120, 40, 75, 23))
        self.btn_DeleteItem.setObjectName("btn_DeleteItem")
        self.btn_Clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.limpar())
        self.btn_Clear.setGeometry(QtCore.QRect(230, 40, 75, 23))
        self.btn_Clear.setObjectName("btn_Clear")
        self.txb_item = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_item.setGeometry(QtCore.QRect(10, 10, 301, 20))
        self.txb_item.setObjectName("txb_item")
        self.View_minhaLista = QtWidgets.QListWidget(self.centralwidget)
        self.View_minhaLista.setGeometry(QtCore.QRect(10, 80, 301, 441))
        self.View_minhaLista.setObjectName("View_minhaLista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def adicionar(self,):
        #Pegando o valor do textbox
        item = self.txb_item.text()
        #Armazenando na View
        self.View_minhaLista.addItem(item)
        #Limpando o textbox
        self.txb_item.setText("")
    
    def remover(self):
        #Pegando o indice do selecionado
        clicked = self.View_minhaLista.currentRow()
        #Deletando linha
        self.View_minhaLista.takeItem(clicked)
    
    def limpar(self):
        self.View_minhaLista.clear()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To do List"))
        self.btn_AddItem.setText(_translate("MainWindow", "Add"))
        self.btn_DeleteItem.setText(_translate("MainWindow", "Delete"))
        self.btn_Clear.setText(_translate("MainWindow", "Clear List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
