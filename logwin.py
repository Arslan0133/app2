# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets, uic

new_window = None


def back_butt():
    global new_window
    new_window = uic.loadUi("MainWindow.ui")
    new_window.setWindowTitle("Main")
    new_window.show()
    Form.close()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 680)
        Form.setStyleSheet("background-color: #330033;\n"
"background-image: url(\"/Users/A/Desktop/Application 2/endless.svg\");")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(560, 200, 151, 61))
        self.label.setStyleSheet("color: white;\n"
"font: 75 8pt \"Montserrat\";\n"
"font-size: 50px;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(500, 320, 281, 31))
        self.lineEdit.setStyleSheet("  border: none;\n"
"  border-bottom: 1px solid #ccc;\n"
"color: white;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 380, 281, 31))
        self.lineEdit_2.setStyleSheet("  border: none;\n"
"  border-bottom: 1px solid #ccc;\n"
"color: white;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.back_b = QtWidgets.QPushButton(Form)
        self.back_b.setGeometry(QtCore.QRect(500, 430, 131, 51))
        self.back_b.setStyleSheet("    color:rgb(5, 127, 127);\n"
"    text-transform: none;\n"
"    text-indent: 0px;\n"
"    text-shadow: none;\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    cursor: default;\n"
"    font: 400 13.3333px Arial;\n"
"    border-width: 2px;\n"
"    border-style: outset;\n"
"    font-size: 30px;")
        self.back_b.setObjectName("back_b")
        self.log_b = QtWidgets.QPushButton(Form)
        self.log_b.setGeometry(QtCore.QRect(650, 430, 131, 51))
        self.log_b.setStyleSheet("    color:rgb(5, 127, 127);\n"
"    text-transform: none;\n"
"    text-indent: 0px;\n"
"    text-shadow: none;\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    cursor: default;\n"
"    font: 400 13.3333px Arial;\n"
"    border-width: 2px;\n"
"    border-style: outset;\n"
"    font-size:30px;")
        self.log_b.setObjectName("log_b")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Login"))
        self.back_b.setText(_translate("Form", "Back"))
        self.log_b.setText(_translate("Form", "Login"))

    def init_ui(self):
        self.ui.back_b.clicked.connect(lambda: (back_butt()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())