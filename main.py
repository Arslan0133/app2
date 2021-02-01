import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from mainwin import Ui_MainWindow
from logwin import Ui_Form
from PyQt5.QtWidgets import QDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.Login.clicked.connect(lambda: (self.Log()))

    def Log(self):
        dialog = QtWidgets.QApplication([])
        loginwin = Login()
        loginwin.show()
        loginwin.exec_()


class Login(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Login).__init__(parent)
        self.setupUi(self)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
