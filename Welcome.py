from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import iconlar

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        if not WelcomePage.objectName():
            WelcomePage.setObjectName(u"WelcomePage")
        WelcomePage.resize(308, 300)
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

        self.retranslateUi(WelcomePage)

        self.LogInbutton.setDefault(False)


        QMetaObject.connectSlotsByName(WelcomePage)
    # setupUi

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