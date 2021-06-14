import sys, random, os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
from time import sleep
from random import choice
import mysql.connector
from datetime import date, datetime

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initID()
        self.dialog = Ui_Form(self)

    def initID(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='projekt')
        cursor = cnx.cursor()
        cursor.execute("SELECT max(ID_ogloszenia) FROM ogloszenia")
        self.iden = cursor.fetchall()
        self.iden = self.iden[0][0]
        cursor.close()
        cnx.close()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(730, 10, 31, 16))
        self.user_label.setObjectName("user_label")
        self.tedit_tresc = QtWidgets.QTextEdit(self.centralwidget)
        self.tedit_tresc.setGeometry(QtCore.QRect(120, 190, 541, 271))
        self.tedit_tresc.setObjectName("tedit_tresc")
        self.pbutton_utworz = QtWidgets.QPushButton(self.centralwidget)
        self.pbutton_utworz.setGeometry(QtCore.QRect(590, 490, 111, 51))
        self.pbutton_utworz.setObjectName("pbutton_utworz")
        self.pbutton_utworz.clicked.connect(self.buttonClicked)
        self.tedit_nazwa = QtWidgets.QTextEdit(self.centralwidget)
        self.tedit_nazwa.setGeometry(QtCore.QRect(120, 130, 541, 31))
        self.tedit_nazwa.setObjectName("tedit_nazwa")
        self.label_nazwa = QtWidgets.QLabel(self.centralwidget)
        self.label_nazwa.setGeometry(QtCore.QRect(120, 110, 91, 16))
        self.label_nazwa.setObjectName("label_nazwa")
        self.label_tresc = QtWidgets.QLabel(self.centralwidget)
        self.label_tresc.setGeometry(QtCore.QRect(120, 170, 81, 16))
        self.label_tresc.setObjectName("label_tresc")
        self.box_prom = QtWidgets.QCheckBox(self.centralwidget)
        self.box_prom.setGeometry(QtCore.QRect(120, 460, 111, 30))
        self.box_prom.setSizeIncrement(QtCore.QSize(0, 0))
        self.box_prom.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.box_prom.setFont(font)
        self.box_prom.setObjectName("box_prom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buttonClicked(self):
        nazwa_og = self.tedit_nazwa.toPlainText()
        tresc_og = self.tedit_tresc.toPlainText()
        promowanie = self.box_prom.checkState()
        if promowanie == 0:
            p = 0
        else:
            p = 1
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='projekt')
        with cnx:
            cursor = cnx.cursor()
            self.iden += 1
            add_ogloszenie = ("INSERT INTO ogloszenia "
                              "(ID_ogloszenia, ID_hydraulika, Nazwa_ogloszenia, Tresc, Promowanie, data_wystawienia_ogloszenia) "
                              "VALUES (%s, %s, %s, %s, %s, %s)")
            today = datetime.now().date()
            data_ogloszenie = (self.iden, self.iden,nazwa_og, tresc_og, promowanie, today)
            cursor.execute(add_ogloszenie, data_ogloszenie)
            cnx.commit()
            cursor.close()
            cnx.close()
            self.close()
            self.dialog.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_label.setText(_translate("MainWindow", "User"))
        self.tedit_tresc.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pbutton_utworz.setText(_translate("MainWindow", "Utwórz"))
        self.label_nazwa.setText(_translate("MainWindow", "Nazwa ogloszenia"))
        self.label_tresc.setText(_translate("MainWindow", "Treść ogłoszenia"))
        self.box_prom.setText(_translate("MainWindow", "Promowanie"))

class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.tresc()
        self.dialog2 = None
        self.setupUi(self)

    def zarezerwuj(self):
        self.close()
        t = QLabel(self)
        t.setGeometry(0,0,800,600)
        t.setStyleSheet("background-image: url(tlo.png); border : none")
        t.setObjectName("Form")
        self.calendarWidget = QtWidgets.QCalendarWidget(t)
        self.calendarWidget.setGeometry(QtCore.QRect(140, 80, 491, 351))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(t)
        self.pushButton.setGeometry(QtCore.QRect(650, 500, 111, 51))
        self.pushButton.setObjectName("pushButton")
        _translate = QtCore.QCoreApplication.translate
        t.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Potwierdź"))
        QtCore.QMetaObject.connectSlotsByName(t)
        self.show()


    def powrot(self):
        self.dialog2 = Ui_MainWindow()
        self.dialog2.show()

    def tresc(self):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='projekt')
        cursor = cnx.cursor()
        cursor.execute('Select count(ID_ogloszenia) FROM ogloszenia')
        self.ident = cursor.fetchall()
        self.ident = self.ident[0][0]
        cursor.execute("SELECT Tresc FROM ogloszenia")
        self.tresc = cursor.fetchall()
        self.tab = []
        for i in range(0, self.ident):
            self.tab.append(self.tresc[i][0])

        cursor.execute('Select promowanie from ogloszenia')
        self.promowanko = cursor.fetchall()
        self.p = []
        for i in range (0,self.ident):
            self.p.append(self.promowanko[i][0])

        cursor.close()
        cnx.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 311, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)


        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        if len(self.tab) > 0:
            self.textEdit.insertHtml(self.tab[0])
        else:
            self.textEdit.insertHtml("BRAK OGLOSZENIA")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 250, 311, 161))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        if self.p[0] == 1:
            font.setBold(True)
            self.textEdit.setFont(font)


        if len(self.tab) > 1:
            self.textEdit_2.insertHtml(self.tab[1])
        else:
            self.textEdit_2.insertHtml("BRAK OGLOSZENIA")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 420, 311, 161))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setFont(font)
        if len(self.tab) > 2:
            self.textEdit_3.insertHtml(self.tab[2])
        else:
            self.textEdit_3.insertHtml("BRAK OGLOSZENIA")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(470, 80, 311, 161))
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setFont(font)
        if len(self.tab) > 3:
            self.textEdit_4.insertHtml(self.tab[3])
        else:
            self.textEdit_4.insertHtml("BRAK OGLOSZENIA")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(470, 250, 311, 161))
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setFont(font)
        if len(self.tab) > 4:
            self.textEdit_5.insertHtml(self.tab[4])
        else:
            self.textEdit_5.insertHtml("BRAK OGLOSZENIA")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(470, 420, 311, 161))
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setFont(font)
        if len(self.tab) > 5:
            self.textEdit_6.insertHtml(self.tab[5])
        else:
            self.textEdit_6.insertHtml("BRAK OGLOSZENIA")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.utworz_og = QtWidgets.QPushButton(Form)
        self.utworz_og.setGeometry(QtCore.QRect(570, 12, 131, 41))
        self.utworz_og.setObjectName("utworz_og")
        self.utworz_og.clicked.connect(self.powrot)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 80, 75, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.zarezerwuj)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 190, 75, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 250, 75, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 360, 75, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 420, 75, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 530, 75, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Strona glowna"))
        self.label_2.setText(_translate("Form", "Ogloszenia:"))
        self.utworz_og.setText(_translate("Form", "Utworz ogloszenie"))
        self.pushButton.setText(_translate("Form", "Zarezerwuj"))
        self.pushButton_2.setText(_translate("Form", "Zarezerwuj"))
        self.pushButton_3.setText(_translate("Form", "Zarezerwuj"))
        self.pushButton_4.setText(_translate("Form", "Zarezerwuj"))
        self.pushButton_5.setText(_translate("Form", "Zarezerwuj"))
        self.pushButton_6.setText(_translate("Form", "Zarezerwuj"))

app = QApplication(sys.argv)
window = Ui_Form()
window.show()
app.exec_()

# cnx = mysql.connector.connect(user='root', password='',
#                                       host='127.0.0.1',
#                                       database='projekt')
# cursor = cnx.cursor()
# cursor.execute('Select count(ID_ogloszenia) FROM ogloszenia')
# ident = cursor.fetchall()
# ident = ident[0][0]
# cursor.execute("SELECT Tresc FROM ogloszenia")
# tresc = cursor.fetchall()
# tab = []
# for i in range(0, ident):
#     tab.append(tresc[i])
# print(tab)
# cursor.close()
# cnx.close()