import sys
from PyQt5 import QtGui, QtWidgets
from loadsc import Ui_load


class LoadScreen(QtWidgets.QMainWindow, Ui_load):
    def __init__(self):
        super(LoadScreen, self).__init__()
        self.ui = Ui_load()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        path = 'load.gif'
        gif = QtGui.QMovie(path)
        self.ui.label.setMovie(gif)
        gif.start()


def run_load():
    app = QtWidgets.QApplication([])
    application = LoadScreen()
    application.show()
    sys.exit(app.exec())
