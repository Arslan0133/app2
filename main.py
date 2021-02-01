import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from mainwin import Ui_MainWindow  # импорт UIWIND из ui.py для отображения
from logwin import Ui_Form

new_window = None


def reg_butt():
    global new_window
    new_window = uic.loadUi("reg.ui")
    new_window.setWindowTitle("Registration")
    new_window.show()
    application.close()


def log_butt():
    global new_window
    new_window = uic.loadUi("log.ui")
    new_window.setWindowTitle("Login")
    new_window.show()
    application.close()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.Register.clicked.connect(lambda: (reg_butt()))
        self.ui.Login.clicked.connect(lambda: (log_butt()))


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())

bulatpidor