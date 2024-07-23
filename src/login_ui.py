from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#TODO: import signup

class LoginUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.signup_window)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.signup_button)

        self.central_widget.setLayout(self.layout)

    def login(self):
        global username
        global login_user
        global tasks
        global login_state
        username = self.username_input.text()
        password = self.password_input.text()
        #TODO: 调用数据库接口，实现登录，返回登录的用户对象和获得的tasks
        result = True
        if result:
            QMessageBox.information(self, "Success", "Login successful. Welcome, " + username + "!")
            self.username_input.clear()
            self.password_input.clear()
            self.close()
            login_state = True
        else:
            QMessageBox.warning(self, "Failed", "Login failed. Please check your username and password.")
            self.username_input.clear()
            self.password_input.clear()
        #print("Login button clicked")

    def signup_window(self):

        print("Sign Up button clicked")

if __name__ == "__main__":
    app = QApplication([])

    window = LoginUI()
    window.show()

    app.exec()