
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import iconlar

class Ui_AdminLogin(object):
    def setupUi(self, AdminLogin):
        if not AdminLogin.objectName():
            AdminLogin.setObjectName(u"AdminLogin")
        AdminLogin.resize(280, 277)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AdminLogin.setWindowIcon(icon)
        AdminLogin.setStyleSheet(u"QWidget { background-color :#d1d5db;\n"
"}\n"
"QPushButton { background-color: rgb(107, 114, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {background-color: #9ca3af\n"
"}\n"
"")
        AdminLogin.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Usernmtxt = QLabel(AdminLogin)
        self.Usernmtxt.setObjectName(u"Usernmtxt")
        self.Usernmtxt.setGeometry(QRect(30, 70, 71, 20))
        self.UserLine = QLineEdit(AdminLogin)
        self.UserLine.setObjectName(u"UserLine")
        self.UserLine.setGeometry(QRect(30, 90, 211, 31))
        self.UserLine.setAutoFillBackground(False)
        self.UserLine.setStyleSheet(u"QLineEdit{ color: rgb(0, 0, 0);\n"
"border: 0px;\n"
"border-radius:10px\n"
"}")
        self.UserLine_2 = QLineEdit(AdminLogin)
        self.UserLine_2.setObjectName(u"UserLine_2")
        self.UserLine_2.setGeometry(QRect(30, 150, 211, 31))
        self.UserLine_2.setAutoFillBackground(False)
        self.UserLine_2.setStyleSheet(u"QLineEdit{ color: rgb(0, 0, 0);\n"
"border: 0px;\n"
"border-radius:10px\n"
"}")
        self.PassTxt = QLabel(AdminLogin)
        self.PassTxt.setObjectName(u"PassTxt")
        self.PassTxt.setGeometry(QRect(30, 130, 61, 16))
        self.LogInbutton = QPushButton(AdminLogin)
        self.LogInbutton.setObjectName(u"LogInbutton")
        self.LogInbutton.setGeometry(QRect(30, 200, 211, 31))
        self.adminicon = QLabel(AdminLogin)
        self.adminicon.setObjectName(u"adminicon")
        self.adminicon.setGeometry(QRect(28, 30, 51, 21))
        self.adminicon.setPixmap(QPixmap(u"iconlar/admin_panel_settings_black_24dp.svg"))
        self.AdminLogintxt = QLabel(AdminLogin)
        self.AdminLogintxt.setObjectName(u"AdminLogintxt")
        self.AdminLogintxt.setGeometry(QRect(70, 30, 81, 21))

        self.retranslateUi(AdminLogin)

        QMetaObject.connectSlotsByName(AdminLogin)
    # setupUi

    def retranslateUi(self, AdminLogin):
        AdminLogin.setWindowTitle(QCoreApplication.translate("AdminLogin", u"Istanbul Exchange Software", None))
        self.Usernmtxt.setText(QCoreApplication.translate("AdminLogin", u"Admin:", None))
        self.UserLine.setText("")
        self.UserLine_2.setText("")
        self.PassTxt.setText(QCoreApplication.translate("AdminLogin", u"Password:", None))
        self.LogInbutton.setText(QCoreApplication.translate("AdminLogin", u"Log In", None))
        self.adminicon.setText("")
        self.AdminLogintxt.setText(QCoreApplication.translate("AdminLogin", u"Admin LogIn", None))



if __name__ == "__main__":
    app = QApplication([])

    dialog = QWidget()
    ui = Ui_AdminLogin()
    ui.setupUi(dialog)

    dialog.show()

    app.exec()