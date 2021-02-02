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
        self.close()
        self.logwin = Login()
        self.logwin.show()


class Login(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_b.clicked.connect(lambda: (self.back_butt()))

    def back_butt(self):
        self.close()
        self.back = MainWindow()
        self.back.show()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
