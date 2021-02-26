import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from mainwin import Ui_MainWindow
from logwin import Ui_Login
from regwin import Ui_Register
from suc_log import Ui_suc_log
from db import *
from capt import *

# from loadsc import Ui_load


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.Login.clicked.connect(lambda: (self.Log()))
        self.ui.Register.clicked.connect(lambda: (self.Reg()))
        self.setWindowTitle("Авторизация")
        self.ui.label.setText('Авторизация')

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
        self.setWindowTitle("Вход")
        self.ui.label.setText('Вход')
        self.ui.log_b.clicked.connect(lambda: (self.log_butt()))
        self.ui.lineEdit.setPlaceholderText('Логин')
        self.ui.lineEdit_2.setPlaceholderText('Пароль')

    def back_butt(self):
        self.close()
        self.back.show()

    def success_log(self):
        self.close()
        self.suc_log = Suc_log()
        self.suc_log.show()

    def failed_log(self):
        self.ui.error_lb.setText('Неверный логин или пароль')

    def log_butt(self):
        log = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()

        connection = create_connection("db4free.net", "dgu_soc", "fmikn_social", "autorization_bd")
        mycursor = connection.cursor()
        mycursor.execute('SELECT user_name, user_pass FROM users')
        myresult = mycursor.fetchall()

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
        self.capcreate()

    def init_ui(self):
        self.ui.back_b.clicked.connect(lambda: (self.back_butt()))
        self.ui.log_b.clicked.connect(lambda: (self.register()))
        self.setWindowTitle("Регистрация")
        self.ui.lineEdit.setPlaceholderText('Логин')
        self.ui.lineEdit_2.setPlaceholderText('Пароль')
        self.ui.err_label.setText('')

    def register(self):
        global log
        global passwd
        log = None
        passwd = None
        if self.checksym == self.ui.capline.text():

            if self.ui.lineEdit.text() and self.ui.lineEdit_2.text() is not None:
                log = self.ui.lineEdit.text()
                passwd = self.ui.lineEdit_2.text()
            else:
                self.ui.err_label.setText('Заполните все поля')
                self.ui.err_label.setStyleSheet('color: red; font-size: 18px; text-aling: center;')
                return

            connection = create_connection("db4free.net", "dgu_soc", "fmikn_social", "autorization_bd")
            mycursor = connection.cursor()

            id_user = mycursor.execute('SELECT id FROM users WHERE id = ( SELECT MAX(id) FROM users )')
            id_user = mycursor.fetchone()
            idid = int(id_user[0]) + 1
            user_data = (idid, log, passwd)

            print(user_data)

            sqlFormula = 'INSERT INTO users (id, user_name, user_pass) VALUES (%s, %s, %s)'
            mycursor.execute(sqlFormula, user_data)
            connection.commit()

            print('yes')

            self.succ_reg()

        else:
            self.ui.err_label.setText('Неправильный ответ на капчу')
            self.ui.err_label.setStyleSheet('color: red; font-size: 18px; text-aling: center;')

    def back_butt(self):
        self.close()
        self.back.show()

    def succ_reg(self):
        self.close()
        self.mainwin = MainWindow()
        self.mainwin.show()
        self.mainwin.ui.label_2.setText('Успешная регистрация, войдите чтобы продолжить')
        self.mainwin.ui.label_2.setStyleSheet('color: rgb(0, 255, 127); font-size: 14px;')

    def capcreate(self):
        self.checksym = capgenerate()
        pixmap = QPixmap('out.png')
        self.ui.label_2.setPixmap(pixmap)

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
