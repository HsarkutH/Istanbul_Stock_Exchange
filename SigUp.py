from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QMessageBox)
import iconlar
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(277, 277)
        #Form.setMaximumSize(QSize(482, 390))
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget { background-color :#d1d5db;\n"
"}\n"
"QPushButton { background-color: rgb(107, 114, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {background-color: #9ca3af\n"
"}\n"
"QLineEdit{ color: rgb(0, 0, 0);\n"
"border: 0px;\n"
"border-radius:10px\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 210, 160, 31))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 261, 31))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 261, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 150, 261, 31))
        self.lineEdit_3.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_3.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 81, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 101, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Istanbul Exchange Software", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Set Password:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Confirm Password:", None))
        #self.pushButton.clicked.connect(self.signup)

    # retranslateUi

    def signup(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()

        if password != confirm_password:
            print("Passwords do not match.")
            return

        connection = sqlite3.connect("user.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        data = cursor.fetchone()
        if not username or not password or not confirm_password:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText('Please fill in all fields!')
            msg_box.setWindowTitle('Warning')
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()

            return
        else:
            if data is not None:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText('User Already Exists!')
                msg_box.setWindowTitle('Warning')
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
            else:
                cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
                connection.commit()
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText('User Created Succesfully!')
                msg_box.setWindowTitle('Succesful')
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()

if __name__ == "__main__":
        app = QApplication([])

        dialog = QWidget()
        ui = Ui_Form()
        ui.setupUi(dialog)

        dialog.show()

        app.exec()