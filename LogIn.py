
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
#import Icon

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(277, 277)
        Form.setMaximumSize(QSize(482, 390))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        Form.setWindowTitle(u"Istanbul Exchange Software")
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"QWidget { background-color :#d1d5db;\n"
"}\n"
"QPushButton { background-color: rgb(107, 114, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {background-color: #9ca3af\n"
"}\n"
"")
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 70, 211, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"QLineEdit{ color: rgb(0, 0, 0);\n"
"border: 0px;\n"
"border-radius:10px\n"
"}")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 140, 211, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QSize(482, 390))
        self.lineEdit_2.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{ color: rgb(0, 0, 0);\n"
"border: 0px;\n"
"border-radius:10px\n"
"}")
        self.lineEdit_2.setMaxLength(540)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 71, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 61, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 190, 211, 31))
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Log In", None))
        pass
    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])

    dialog = QWidget()
    ui = Ui_Form()
    ui.setupUi(dialog)

    dialog.show()

    app.exec()