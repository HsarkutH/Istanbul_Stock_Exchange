from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget, QMainWindow)
import iconlar
import Helper
import LogIn
import SigUp

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        if not WelcomePage.objectName():
            WelcomePage.setObjectName(u"WelcomePage")
        WelcomePage.setFixedSize(308, 300)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        WelcomePage.setWindowIcon(icon)
        WelcomePage.setStyleSheet(u"QWidget { background-color:rgb(0, 0, 17)\n"
"}\n"
"QPushButton { background-color: rgb(107, 114, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {background-color: #9ca3af\n"
"}\n"
"")
        WelcomePage.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.IESicoNlabel = QLabel(WelcomePage)
        self.IESicoNlabel.setObjectName(u"IESicoNlabel")
        self.IESicoNlabel.setGeometry(QRect(0, 0, 311, 301))
        self.IESicoNlabel.setMaximumSize(QSize(482, 390))
        self.IESicoNlabel.setAutoFillBackground(False)
        self.IESicoNlabel.setStyleSheet(u"")
        self.IESicoNlabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.IESicoNlabel.setFrameShadow(QFrame.Plain)
        self.IESicoNlabel.setPixmap(QPixmap(u"iconlar/FullLogo.png"))
        self.IESicoNlabel.setScaledContents(True)
        self.IESicoNlabel.setWordWrap(False)
        self.LogInbutton = QPushButton(WelcomePage)
        self.LogInbutton.setObjectName(u"LogInbutton")
        self.LogInbutton.setGeometry(QRect(10, 260, 91, 25))
        self.LogInbutton.setAutoDefault(True)
        self.LogInbutton.setFlat(False)
        self.SignUpbutton = QPushButton(WelcomePage)
        self.SignUpbutton.setObjectName(u"SignUpbutton")
        self.SignUpbutton.setGeometry(QRect(210, 260, 91, 25))
        self.AdminButton = QPushButton(WelcomePage)
        self.AdminButton.setObjectName(u"AdminButton")
        self.AdminButton.setGeometry(QRect(260, 10, 41, 31))
        icon1 = QIcon()
        icon1.addFile(u"iconlar/Profileicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AdminButton.setIcon(icon1)
        self.AdminButton.setIconSize(QSize(27, 27))

        self.retranslateUi(WelcomePage)

        self.LogInbutton.setDefault(False)

        self.LogInbutton.clicked.connect(self.open_login_menu)
        self.SignUpbutton.clicked.connect(self.open_signup_menu)

        QMetaObject.connectSlotsByName(WelcomePage)
    # setupUi

    def open_login_menu(self):
        self.login_menum = QMainWindow()
        # Ui_mainWindow'daki arayüzü bu ana pencereye yükleyin
        ui_login_menu = LogIn.Ui_Form()
        ui_login_menu.setupUi(self.login_menum)
        # Ana pencereyi gösterin
        def connect_login():
            ui_login_menu.login()
        ui_login_menu.pushButton.clicked.connect(connect_login)
        self.login_menum.show()

    def open_signup_menu(self):
        self.signup_menum = QMainWindow()
        # Ui_mainWindow'daki arayüzü bu ana pencereye yükleyin
        ui_signup_menu = SigUp.Ui_Form()
        ui_signup_menu.setupUi(self.signup_menum)
        ui_signup_menu.retranslateUi(self.signup_menum)
        def connect_signup():
            ui_signup_menu.signup()
            #app.exit()
        # Ana pencereyi gösterin
        ui_signup_menu.pushButton.clicked.connect(connect_signup)
        self.signup_menum.show()

    def retranslateUi(self, WelcomePage):
        WelcomePage.setWindowTitle(QCoreApplication.translate("WelcomePage", u"Istanbul Exchange Software", None))
        self.IESicoNlabel.setText("")
        self.LogInbutton.setText(QCoreApplication.translate("WelcomePage", u"Log In", None))
        self.SignUpbutton.setText(QCoreApplication.translate("WelcomePage", u"Sign up", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])

    dialog = QWidget()
    ui = Ui_WelcomePage()
    ui.setupUi(dialog)

    dialog.show()

    app.exec()