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
import subprocess
import os


import os
import subprocess
def open_file1():
    try:
        # Get the current working directory
        current_dir = os.getcwd()

        # Construct the path to LogIn.py relative to the current directory
        file1_path = os.path.join(current_dir, 'LogIn.py')

        if os.path.exists(file1_path):  # Check if the file exists
            # Execute the first Python file
            subprocess.Popen(['python3.12', file1_path])
        else:
            print("Error: File 1 not found.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function
open_file1()


def open_file2():
    try:
        # Get the current working directory
        current_dir = os.getcwd()

        # Construct the path to LogIn.py relative to the current directory
        file2_path = os.path.join(current_dir, 'SigUp.py')

        if os.path.exists(file2_path):  # Check if the file exists
            # Execute the first Python file
            subprocess.Popen(['python3.12', file2_path])
        else:
            print("Error: File 1 not found.")
    except Exception as e:
        print(f"Error: {e}")

    # Call the function


open_file2()
class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.setFixedSize(288, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
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
        self.pushButton_2.clicked.connect(open_file1())
        self.pushButton_3.clicked.connect(open_file2())


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