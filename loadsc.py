# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadsc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 680)
        Form.setStyleSheet("background-color: #330033;\n"
"background-image: url(\"/Users/A/Desktop/Application 2/endless.svg\");")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 40, 800, 600))
        self.label.setObjectName("label")
        self.div = QtWidgets.QAction(Form)
        self.div.setObjectName("div")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.div.setText(_translate("Form", "div1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_load()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())