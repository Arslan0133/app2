# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suc_log.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_suc_log(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 680)
        Form.setStyleSheet("background-color: #330033;\n"
"background-image: url(\"/Users/A/Desktop/Application 2/endless.svg\");")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(440, 280, 401, 61))
        self.label.setStyleSheet("color: rgb(12, 255, 146);\n"
"font: 75 8pt \"Montserrat\";\n"
"font-size: 50px;")
        self.label.setObjectName("label")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(560, 380, 151, 41))
        self.back_button.setStyleSheet("color: rgb(12, 255, 146);\n"
"font: 75 8pt \"Montserrat\";\n"
"font-size: 25px;\n"
"border: 2px solid rgb(39, 118, 115);\n"
"border-radius: 20px;\n"
"text-align: center;")
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Успешный вход"))
        self.back_button.setText(_translate("Form", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())