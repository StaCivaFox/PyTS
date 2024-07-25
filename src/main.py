import sys
import os
from login_ui import *
from login import *

import design

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import datetime
import time

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = design.Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_state, login_user, tasks = login_window(app)
    window = MainWindow()
    window.show()
    if login_state:
        sys.exit(app.exec())
    else:
        sys.exit(1)
