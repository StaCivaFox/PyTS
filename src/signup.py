from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setFixedSize(400, 300)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)

    def signup(self):
        global username
        global login_user
        global tasks
        global login_state
        username = self.username_input.text()
        password = self.password_input.text()

if __name__ == "__main__":
    app = QApplication([])

    window = SignUpWindow()
    window.show()

    app.exec()