import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from mainwin import Ui_MainWindow
from logwin import Ui_Login
from regwin import Ui_Register
from suc_log import Ui_suc_log
from db import *

connection = create_connection("db4free.net", "dgu_soc", "fmikn_social", "autorization_bd")
mycursor = connection.cursor()
mycursor.execute('SELECT user_name, user_pass FROM users')
myresult = mycursor.fetchall()


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
        self.back = MainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_b.clicked.connect(lambda: (self.back_butt()))
        self.setWindowTitle("Login")
        self.ui.log_b.clicked.connect(lambda: (self.log_butt()))

    def back_butt(self):
        self.close()
        self.back.show()

    def success_log(self):
        self.close()
        self.suc_log = Suc_log()
        self.suc_log.show()

    def failed_log(self):
        self.ui.error_lb.setText('Не верный логин или пароль')

    def log_butt(self):
        log = self.ui.lineEdit.text()

        try:
            passwd = int(self.ui.lineEdit_2.text())
        except ValueError:
            self.failed_log()
            return

        logining = (log, passwd)
        if logining in myresult:
            self.success_log()
        else:
            self.failed_log()


class Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super().__init__()
        self.back = MainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_b2.clicked.connect(lambda: (self.back_butt()))
        self.setWindowTitle("Registration")

    def back_butt(self):
        self.close()
        self.back.show()


class Suc_log(QtWidgets.QMainWindow, Ui_suc_log):
    def __init__(self):
        super().__init__()
        self.back = MainWindow()
        self.ui = Ui_suc_log()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.back_button.clicked.connect(lambda: (self.back_butt()))

    def back_butt(self):
        self.close()
        self.back.show()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
