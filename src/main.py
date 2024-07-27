import sys
import os
from login_ui import *
from login import *

import homepage

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import datetime
import time
import globals

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.home = homepage.Ui_MainWindow()
        self.home.setupUi(self)
        #self.home.homepageGetLoginUserAndTasks(login_user, tasks)
        self.home.printTasks()
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window(app)
    window = MainWindow()
    #window.show()
    if globals.login_state:
        sys.exit(app.exec())
    else:
        sys.exit(1)
