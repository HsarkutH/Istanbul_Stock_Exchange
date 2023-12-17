import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon

class LoginScreen(QWidget):
    def __init__(self, db_connection):
        super().__init__()

        self.setWindowTitle("Stock Exchange App - Login")
        self.layout = QVBoxLayout()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Login")
        self.signup_button = QPushButton("Sign Up")
        self.login_status_label = QLabel("")

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.signup_button)
        self.layout.addWidget(self.login_status_label)

        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup)

        self.setLayout(self.layout)

        self.db_connection = db_connection

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            self.login_status_label.setText("Login successful")
        else:
            self.login_status_label.setText("Login failed")

    def signup(self):
        # Open Sign Up screen
        self.sign_up_screen = SignUpScreen(self.db_connection)
        self.sign_up_screen.show()
        self.close()

class SignUpScreen(QWidget):
    def __init__(self, db_connection):
        super().__init__()

        self.setWindowTitle("Stock Exchange App - Sign Up")
        self.layout = QVBoxLayout()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_button = QPushButton("Sign Up")
        self.back_button = QPushButton("Back")

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.confirm_password_label)
        self.layout.addWidget(self.confirm_password_input)
        self.layout.addWidget(self.signup_button)
        self.layout.addWidget(self.back_button)

        self.signup_button.clicked.connect(self.sign_up)
        self.back_button.clicked.connect(self.back)

        self.setLayout(self.layout)

        self.db_connection = db_connection

    def sign_up(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password == confirm_password:
            cursor = self.db_connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.db_connection.commit()
            self.back()
        else:
            self.username_input.clear()
            self.password_input.clear()
            self.confirm_password_input.clear()
            self.username_input.setFocus()
            self.status_label.setText("Password and Confirm Password do not match.")

    def back(self):
        # Go back to Login screen
        self.login_screen = LoginScreen(self.db_connection)
        self.login_screen.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stock Exchange App")
        self.db_connection = sqlite3.connect("users.db")
        self.setup_database()
        self.login_screen = LoginScreen(self.db_connection)
        self.setCentralWidget(self.login_screen)

    def setup_database(self):
        cursor = self.db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")
        self.db_connection.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    dir_path = os.getcwd()
    db_file_path = os.path.join(dir_path, 'users.db')
    print("Database file path:", db_file_path)