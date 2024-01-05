from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)
import iconlar
import json

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.setFixedSize(401, 273)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        AdminWindow.setWindowIcon(icon)
        AdminWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 83, 100, 1), stop:1 rgba(15, 32, 39, 1)); \n"
"font-family: Noto Sans;\n"
"color : rgb(255, 255, 255);\n"
"QMenuBar{\n"
"backgroun-color: rgba(255, 255, 255,50)\n"
"}\n"
"\n"
"")
        AdminWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.refresh = QPushButton(AdminWindow)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(30, 200, 111, 21))
        icon1 = QIcon()
        icon1.addFile(u"iconlar/refresh_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh.setIcon(icon1)
        self.refresh.setIconSize(QSize(24, 24))
        self.userdelete = QPushButton(AdminWindow)
        self.userdelete.setObjectName(u"userdelete")
        self.userdelete.setGeometry(QRect(280, 110, 111, 21))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(10)
        self.userdelete.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"iconlar/delete user icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userdelete.setIcon(icon2)
        self.userdelete.setIconSize(QSize(21, 21))
        self.UserList = QComboBox(AdminWindow)
        self.UserList.setObjectName(u"UserList")
        self.UserList.setGeometry(QRect(30, 70, 361, 31))
        self.UserList.setStyleSheet(u"background-color: rgba(255, 255, 255,50)")
        self.logout = QPushButton(AdminWindow)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(320, 230, 71, 31))
        icon3 = QIcon()
        icon3.addFile(u"iconlar/LogOutIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon3)
        self.logout.setIconSize(QSize(25, 25))
        self.Userslisttxt = QLabel(AdminWindow)
        self.Userslisttxt.setObjectName(u"Userslisttxt")
        self.Userslisttxt.setGeometry(QRect(30, 50, 61, 16))
        self.Userslisttxt.setStyleSheet(u"background-color: rgba(255, 255, 255,)")
        self.Gunsaygac = QSpinBox(AdminWindow)
        self.Gunsaygac.setObjectName(u"Gunsaygac")
        self.Gunsaygac.setGeometry(QRect(30, 170, 71, 22))
        self.Gunsaygac.setAcceptDrops(False)
        self.Gunsaygac.setMinimum(1)
        self.Gunsaygac.setMaximum(365)

        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi
        self.refresh.clicked.connect(self.gunCek)
        with open('day_value.json', 'r') as file:
            data = json.load(file)
            self.Gunsaygac.setValue(data.get('gunsayisi'))
    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Administrator", None))
        self.refresh.setText(QCoreApplication.translate("AdminWindow", u"Day's Refresh", None))
        self.userdelete.setText(QCoreApplication.translate("AdminWindow", u"User delete", None))
#if QT_CONFIG(tooltip)
        self.UserList.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.UserList.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.UserList.setCurrentText("")
        self.logout.setText(QCoreApplication.translate("AdminWindow", u"LogOut", None))
        self.Userslisttxt.setText(QCoreApplication.translate("AdminWindow", u" User's List", None))
    def gunCek(self):
        gunSayisi = self.Gunsaygac.value()
        data = {'gunsayisi': gunSayisi}
        with open('day_value.json', 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
        app = QApplication([])

        dialog = QWidget()
        ui = Ui_AdminWindow()
        ui.setupUi(dialog)

        dialog.show()

        app.exec()
