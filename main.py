import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from mainwin import Ui_MainWindow
from logwin import Ui_Login
from regwin import Ui_Register


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.Login.clicked.connect(lambda: (self.Log()))
        self.ui.Register.clicked.connect(lambda: (self.Reg()))
        self.setWindowTitle("Authorization")

    def Log(self):
        self.close()
        self.logwin = Login()
        self.logwin.show()

    def Reg(self):
        self.close()
        self.regwin = Register()
        self.regwin.show()


class Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_b.clicked.connect(lambda: (self.back_butt()))
        self.setWindowTitle("Login")

    def back_butt(self):
        self.close()
        self.back = MainWindow()
        self.back.show()

class Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_b2.clicked.connect(lambda: (self.back_butt()))

    def back_butt(self):
        self.close()
        self.back = MainWindow()
        self.back.show()



app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
