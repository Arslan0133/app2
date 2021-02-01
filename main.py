import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from mainwin import Ui_MainWindow
from logwin import Ui_Form


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.Login.clicked.connect(lambda: (self.Log()))

    def Log(self):
        self.w = Login
        self.setWindowTitle("Login")
        self.w.show()
        self.hide()


class Login(QMainWindow, Ui_Form):
    def __init__(self):
        Form = QtWidgets.QWidget()
        super(Ui_Form).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(Form)
        self.init_ui()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
