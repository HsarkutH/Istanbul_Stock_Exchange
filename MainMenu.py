from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QWidget, QMessageBox)
import iconlar
import sqlite3
import yfinance as yf
import datetime
import pandas_ta as ta
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(976, 655)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 83, 100, 1), stop:1 rgba(15, 32, 39, 1)); \n"
"font-family: Noto Sans;\n"
"color : rgb(255, 255, 255);\n"
"QMenuBar{\n"
"backgroun-color: rgba(255, 255, 255,50)\n"
"}\n"
"")
        mainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        mainWindow.setIconSize(QSize(30, 30))
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(False)
        self.actionSearch = QAction(mainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        icon1 = QIcon()
        icon1.addFile(u"iconlar/Hamburger.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSearch.setIcon(icon1)
        self.actionContact = QAction(mainWindow)
        self.actionContact.setObjectName(u"actionContact")
        self.actionAccount = QAction(mainWindow)
        self.actionAccount.setObjectName(u"actionAccount")
        self.actionAccount.setCheckable(False)
        self.actionAccount.setChecked(False)
        icon2 = QIcon()
        icon2.addFile(u"iconlar/Profileicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAccount.setIcon(icon2)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.actionAccount.setFont(font)
        self.actionAccount.setVisible(True)
        self.actionAccount.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionStock_operations = QAction(mainWindow)
        self.actionStock_operations.setObjectName(u"actionStock_operations")
        icon3 = QIcon()
        icon3.addFile(u"iconlar/Trendingicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStock_operations.setIcon(icon3)
        font1 = QFont()
        font1.setPointSize(10)
        self.actionStock_operations.setFont(font1)
        self.actionContact_2 = QAction(mainWindow)
        self.actionContact_2.setObjectName(u"actionContact_2")
        icon4 = QIcon()
        icon4.addFile(u"iconlar/Contact.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionContact_2.setIcon(icon4)
        self.actionContact_2.setFont(font1)
        self.actionLog_Out = QAction(mainWindow)
        self.actionLog_Out.setObjectName(u"actionLog_Out")
        icon5 = QIcon()
        icon5.addFile(u"iconlar/informationIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLog_Out.setIcon(icon5)
        self.actionLog_Out.setFont(font1)
        self.actionLog_Out_2 = QAction(mainWindow)
        self.actionLog_Out_2.setObjectName(u"actionLog_Out_2")
        icon6 = QIcon()
        icon6.addFile(u"iconlar/LogOutIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLog_Out_2.setIcon(icon6)
        self.actionLog_Out_2.setFont(font1)
        self.actionLog_Out_2.setMenuRole(QAction.QuitRole)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(190, 70, 581, 31))
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet(u"background-color: rgba(255, 255, 255,50)")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(760, 610, 211, 20))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border : none;\n"
"color: rgba(255, 255, 255,100)")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(190, 150, 581, 351))
        self.graphicsView.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(780, 70, 41, 31))
        icon7 = QIcon()
        icon7.addFile(u"iconlar/refresh_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 510, 71, 21))
        self.pushButton.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        icon8 = QIcon()
        icon8.addFile(u"iconlar/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(18, 18))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 520, 111, 31))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255,50);\n"
                                   "font: 700 9pt \"Segoe UI\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 520, 111, 31))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255,50);\n"
                                   "font: 700 9pt \"Segoe UI\";")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 976, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(199, 126, 168, 149))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuMenu.sizePolicy().hasHeightForWidth())
        self.menuMenu.setSizePolicy(sizePolicy)
        self.menuMenu.setMinimumSize(QSize(2, 0))
        self.menuMenu.setContextMenuPolicy(Qt.NoContextMenu)
        self.menuMenu.setAcceptDrops(False)
        self.menuMenu.setTearOffEnabled(False)
        self.menuMenu.setIcon(icon1)
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAccount)
        self.menuMenu.addAction(self.actionStock_operations)
        self.menuMenu.addAction(self.actionContact_2)
        self.menuMenu.addAction(self.actionLog_Out)
        self.menuMenu.addAction(self.actionLog_Out_2)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)

        self.databaseVeriCek()
        self.actionLog_Out_2.triggered.connect(self.logout_button)
        self.actionLog_Out.triggered.connect(self.info_button)
        self.actionContact_2.triggered.connect(self.contact_us)
        #comboboxtan stoc isimlerini çekme
        stock_Symbol =self.comboBox.currentText()
        #10 yıllık zaman periyodu ayarlama
        end_date =datetime.date.today()
        start_date =end_date - datetime.timedelta(days=365*10)
        stock_data = yf.download(stock_Symbol,start=start_date,end=end_date)
        #indicator ayarlama
        sma =stock_data.ta.sma(length=20)
        rsi = stock_data.ta.rsi(length=14)
        #graph için verileri ayarlama
        ohlc_data = stock_data[['Open','High','Low','Close','Volume']].reset_index()
        ohlc_data['Date'] = ohlc_data['Date'].map(mdates.date2num)
        #grafiği plotlama
        fig, ax = plt.subplots()
        candlestick_ohlc(ax,ohlc_data.values,width=0.6,colorup ='green',colordown='red')
        # Customize the graph
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Candlestick Chart')

        # Display the SMA indicator as a line graph
        plt.plot(stock_data.index, sma, label='SMA')

        # Display the RSI indicator as a line graph
        plt.plot(stock_data.index, rsi, label='RSI')

        # Customize the graph
        plt.xlabel('Date')
        plt.ylabel('Indicator Value')
        plt.title('Stock Indicator Line Chart')
        plt.legend()

        # Display the graph
        plt.show()


    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Istanbul Exchange Software", None))
        self.actionSearch.setText(QCoreApplication.translate("mainWindow", u"Stock Operation", None))
        self.actionContact.setText(QCoreApplication.translate("mainWindow", u"Contact", None))
        self.actionAccount.setText(QCoreApplication.translate("mainWindow", u"Account", None))
        self.actionStock_operations.setText(QCoreApplication.translate("mainWindow", u"Stock operations", None))
        self.actionContact_2.setText(QCoreApplication.translate("mainWindow", u"Contact", None))
        self.actionLog_Out.setText(QCoreApplication.translate("mainWindow", u"Information", None))
        self.actionLog_Out_2.setText(QCoreApplication.translate("mainWindow", u"Log Out", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Copyright \u00a9 2024-All Rights Reserved", None))
        self.pushButton_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"Show", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"     You can Buy", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"     You can Sell", None))
        self.menuMenu.setTitle(QCoreApplication.translate("mainWindow", u"Menu", None))
    # retranslateUi

    def logout_button(self):
        app.exit()

    def info_button(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText('Hüseyin Sarkut\nYiğit Emre Ünlü\nPerviz Alekperov\nMuhammed Aydın')
        msg_box.setWindowTitle('Team Info')
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
    def databaseVeriCek(self):
        self.comboBox.clear()
        connection = sqlite3.connect("stock_data.db")
        cursor = connection.cursor()

        cursor.execute("SELECT ticker FROM stock_data")
        veriler = cursor.fetchall()
        for veri in veriler:
            self.comboBox.addItem(veri[0])
        connection.close()

    def contact_us(self):
        url = QUrl("https://github.com/HsarkutH/Istanbul_Stock_Exchange")
        QDesktopServices.openUrl(url)

if __name__ == "__main__":
        app = QApplication([])

        dialog = QMainWindow()
        ui = Ui_mainWindow()
        ui.setupUi(dialog)

        dialog.show()

        app.exec()