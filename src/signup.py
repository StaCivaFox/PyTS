from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from login import *

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

        self.password_confirm_label = QLabel("Confirm Password")
        self.password_confirm_input = QLineEdit()
        self.password_confirm_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.password_confirm_label)
        self.layout.addWidget(self.password_confirm_input)
        self.layout.addWidget(self.signup_button)

        self.setLayout(self.layout)

    def signup(self):
        username = self.username_input.text()
        password = self.password_input.text()
        password_confirm = self.password_confirm_input.text()
        if not username or not password or not password_confirm:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        elif password != password_confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return
        else:
            result, msg = add_person(username, password)
            if result:
                QMessageBox.information(self, "Success", "Sign up successful. Welcome, " + username + "!")
                self.username_input.clear()
                self.password_input.clear()
                self.password_confirm_input.clear()
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Sign up failed. " + msg + "Please try again.")
                self.username_input.clear()
                self.password_input.clear()
                self.password_confirm_input.clear()

if __name__ == "__main__":
    app = QApplication([])

    window = SignUpWindow()
    window.show()

    app.exec()