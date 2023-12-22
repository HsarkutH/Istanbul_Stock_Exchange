from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPushButton, QSizePolicy, QWidget)
import iconlar

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(288, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMaximumSize(QSize(482, 390))
        dialog.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        dialog.setWindowIcon(icon)
        dialog.setStyleSheet(u"QWidget { background-color:rgb(0, 0, 17)\n"
"}\n"
"QPushButton { background-color: rgb(107, 114, 128);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {background-color: #9ca3af\n"
"}\n"
"")
        dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        dialog.setModal(False)
        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 600, 461, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 291, 281))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"iconlar/FullLogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.pushButton_3 = QPushButton(dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 250, 91, 25))
        self.pushButton_2 = QPushButton(dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 250, 91, 25))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setFlat(False)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Istanbul Exchange Software", None))
#if QT_CONFIG(tooltip)
        dialog.setToolTip(QCoreApplication.translate("dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        dialog.setWhatsThis(QCoreApplication.translate("dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("dialog", u"Sign up", None))
        self.pushButton_2.setText(QCoreApplication.translate("dialog", u"Log In", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication([])

    dialog = QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)

    dialog.show()

    app.exec()