# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 680)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("box-shadow: inset 0 -1px 1px rgba(255,255,255,0.3);\n"
"background: #555;\n"
"-moz-border-radius: 25px;\n"
"-webkit-border-radius: 25px;\n"
"border-radius: 25px;")
        self.Signin = QtWidgets.QWidget(MainWindow)
        self.Signin.setStyleSheet("background-color: #330033;\n"
"background-image: url(\"/Users/A/Desktop/Application 2/endless.svg\");")
        self.Signin.setObjectName("Signin")
        self.Login = QtWidgets.QPushButton(self.Signin)
        self.Login.setGeometry(QtCore.QRect(510, 300, 221, 51))
        self.Login.setStyleSheet("    color:rgb(5, 127, 127);\n"
"    text-transform: none;\n"
"    text-indent: 0px;\n"
"    text-shadow: none;\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    cursor: default;\n"
"    font: 400 13.3333px Arial;\n"
"    border-width: 2px;\n"
"    border-style: outset;")
        self.Login.setObjectName("Login")
        self.label = QtWidgets.QLabel(self.Signin)
        self.label.setGeometry(QtCore.QRect(450, 180, 351, 61))
        self.label.setStyleSheet("color: white;\n"
"font: 75 8pt \"Montserrat\";\n"
"font-size: 50px;")
        self.label.setObjectName("label")
        self.Register = QtWidgets.QPushButton(self.Signin)
        self.Register.setGeometry(QtCore.QRect(510, 370, 221, 51))
        self.Register.setStyleSheet("    color: rgb(108, 53, 108);\n"
"    text-transform: none;\n"
"    text-indent: 0px;\n"
"    text-shadow: none;\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    cursor: default;\n"
"    font: 400 13.3333px Arial;\n"
"    border-width: 2px;\n"
"    border-style: outset;\n"
"    border-color: -internal-light-dark(rgb(118, 118, 118), rgb(133, 133, 133));")
        self.Register.setObjectName("Register")
        self.label_2 = QtWidgets.QLabel(self.Signin)
        self.label_2.setGeometry(QtCore.QRect(450, 260, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.Signin)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Авторизация"))
        self.Register.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
