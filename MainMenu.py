from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                               QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QWidget, QMessageBox)
import iconlar
import sqlite3
import yfinance as yf
import datetime
import pandas_ta as ta
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import json

with open('day_value.json', 'r') as file:
    data = json.load(file)
gun_sayisi = data.get('gunsayisi')


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(716, 469)
        icon = QIcon()
        icon.addFile(u"iconlar/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 83, 100, 1), stop:1 rgba(15, 32, 39, 1)); \n"
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
        self.Account = QAction(mainWindow)
        self.Account.setObjectName(u"Account")
        self.Account.setCheckable(False)
        self.Account.setChecked(False)
        icon2 = QIcon()
        icon2.addFile(u"iconlar/Profileicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Account.setIcon(icon2)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.Account.setFont(font)
        self.Account.setVisible(True)
        self.Account.setMenuRole(QAction.ApplicationSpecificRole)
        self.Stock_operations = QAction(mainWindow)
        self.Stock_operations.setObjectName(u"Stock_operations")
        icon3 = QIcon()
        icon3.addFile(u"iconlar/Trendingicon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Stock_operations.setIcon(icon3)
        font1 = QFont()
        font1.setPointSize(10)
        self.Stock_operations.setFont(font1)
        self.Contact_2 = QAction(mainWindow)
        self.Contact_2.setObjectName(u"Contact_2")
        icon4 = QIcon()
        icon4.addFile(u"iconlar/Contact.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Contact_2.setIcon(icon4)
        self.Contact_2.setFont(font1)
        self.Information = QAction(mainWindow)
        self.Information.setObjectName(u"Information")
        icon5 = QIcon()
        icon5.addFile(u"iconlar/informationIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Information.setIcon(icon5)
        self.Information.setFont(font1)
        self.Log_Out = QAction(mainWindow)
        self.Log_Out.setObjectName(u"Log_Out")
        icon6 = QIcon()
        icon6.addFile(u"iconlar/LogOutIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Log_Out.setIcon(icon6)
        self.Log_Out.setFont(font1)
        self.Log_Out.setMenuRole(QAction.QuitRole)
        self.MaininIci = QWidget(mainWindow)
        self.MaininIci.setObjectName(u"MaininIci")
        self.SymbolBox = QComboBox(self.MaininIci)
        self.SymbolBox.setObjectName(u"SymbolBox")
        self.SymbolBox.setEnabled(True)
        self.SymbolBox.setGeometry(QRect(80, 50, 581, 31))
        self.SymbolBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.SymbolBox.setStyleSheet(u"background-color: rgba(255, 255, 255,50)")
        self.SymbolBox.setEditable(True)
        self.SymbolBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.SymbolBox.setIconSize(QSize(16, 16))
        self.SymbolBox.setFrame(True)
        self.Copyrighttxt = QLabel(self.MaininIci)
        self.Copyrighttxt.setObjectName(u"Copyrighttxt")
        self.Copyrighttxt.setGeometry(QRect(500, 420, 211, 20))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans"])
        font2.setItalic(True)
        self.Copyrighttxt.setFont(font2)
        self.Copyrighttxt.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
                                        "border : none;\n"
                                        "color: rgba(255, 255, 255,100)")
        self.ShowButton = QPushButton(self.MaininIci)
        self.ShowButton.setObjectName(u"ShowButton")
        self.ShowButton.setGeometry(QRect(330, 180, 71, 21))
        self.ShowButton.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        icon7 = QIcon()
        icon7.addFile(u"iconlar/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ShowButton.setIcon(icon7)
        self.ShowButton.setIconSize(QSize(18, 18))
        self.UcanBuy = QLabel(self.MaininIci)
        self.UcanBuy.setObjectName(u"UcanBuy")
        self.UcanBuy.setGeometry(QRect(60, 370, 111, 31))
        self.UcanBuy.setStyleSheet(u"background-color: rgba(255, 255, 255,50);\n"
                                   "font: 700 9pt \"Segoe UI\";")
        self.UcanSell = QLabel(self.MaininIci)
        self.UcanSell.setObjectName(u"UcanSell")
        self.UcanSell.setGeometry(QRect(190, 370, 111, 31))
        self.UcanSell.setStyleSheet(u"background-color: rgba(255, 255, 255,50);\n"
                                    "font: 700 9pt \"Segoe UI\";")
        self.IndicatorBox2 = QComboBox(self.MaininIci)
        self.IndicatorBox2.setObjectName(u"IndicatorBox2")
        self.IndicatorBox2.setGeometry(QRect(230, 110, 251, 31))
        self.IndicatorBox2.setStyleSheet(u"background-color: rgba(255, 255, 255,70)")
        indicators = self.combineData('indicator_momentum.json', 'indicator_overlap.json')
        self.fillCombobox(indicators)
        self.ChooseSymboltxt = QLabel(self.MaininIci)
        self.ChooseSymboltxt.setObjectName(u"ChooseSymboltxt")
        self.ChooseSymboltxt.setGeometry(QRect(300, 30, 131, 16))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans"])
        font3.setBold(True)
        self.ChooseSymboltxt.setFont(font3)
        self.ChooseSymboltxt.setStyleSheet(u"background-color: rgba(255, 255, 255,)")
        self.ChooseIndictrtxt = QLabel(self.MaininIci)
        self.ChooseIndictrtxt.setObjectName(u"ChooseIndictrtxt")
        self.ChooseIndictrtxt.setGeometry(QRect(310, 90, 111, 16))
        self.ChooseIndictrtxt.setFont(font3)
        self.ChooseIndictrtxt.setStyleSheet(u"background-color: rgba(255, 255, 255,)")
        mainWindow.setCentralWidget(self.MaininIci)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 716, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(319, 225, 168, 149))
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
        self.menuMenu.addAction(self.Account)
        self.menuMenu.addAction(self.Stock_operations)
        self.menuMenu.addAction(self.Contact_2)
        self.menuMenu.addAction(self.Information)
        self.menuMenu.addAction(self.Log_Out)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)

        self.databaseVeriCek()
        self.Log_Out.triggered.connect(self.logout_button)
        self.Information.triggered.connect(self.info_button)
        self.Contact_2.triggered.connect(self.contact_us)
        self.ShowButton.clicked.connect(self.show_graph)
    def show_graph(self):
        # comboboxtan stoc isimlerini çekme
        stock_Symbol = self.SymbolBox.currentText()
        # 10 yıllık zaman periyodu ayarlama
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=gun_sayisi)
        stock_data = yf.download(stock_Symbol, start=start_date, end=end_date)
        # indicator ayarlama

        rsi = stock_data.ta.rsi(length=14)
        # graph için verileri ayarlama
        ohlc_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].reset_index()
        ohlc_data['Date'] = ohlc_data['Date'].map(mdates.date2num)
        # grafiği plotlama
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, ohlc_data.values, width=0.6, colorup='green', colordown='red')
        # Customize the graph
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Candlestick Chart')

        # Display the SMA indicator as a line graph


        # Display the RSI indicator as a line graph
        if self.IndicatorBox2.currentText() == 'sma':
            sma = stock_data.ta.sma(length=20)
            plt.plot(stock_data.index, sma, label='SMA')
        plt.plot(stock_data.index, rsi, label='RSI')

        # Customize the graph
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Indicator Line Chart')
        plt.legend()

        # Display the graph
        plt.show()

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Istanbul Exchange Software", None))
        self.actionSearch.setText(QCoreApplication.translate("mainWindow", u"Stock Operation", None))
        self.actionContact.setText(QCoreApplication.translate("mainWindow", u"Contact", None))
        self.Account.setText(QCoreApplication.translate("mainWindow", u"Account", None))
        self.Stock_operations.setText(QCoreApplication.translate("mainWindow", u"Stock operations", None))
        self.Contact_2.setText(QCoreApplication.translate("mainWindow", u"Contact", None))
        self.Information.setText(QCoreApplication.translate("mainWindow", u"Information", None))
        self.Log_Out.setText(QCoreApplication.translate("mainWindow", u"Log Out", None))
        self.Copyrighttxt.setText(QCoreApplication.translate("mainWindow",
                                                             u"<html><head/><body><p>Copyright \u00a9 2024-All Rights Reserved</p></body></html>",
                                                             None))
        self.ShowButton.setText(QCoreApplication.translate("mainWindow", u"Show", None))
        self.UcanBuy.setText(QCoreApplication.translate("mainWindow", u"     You can Buy", None))
        self.UcanSell.setText(QCoreApplication.translate("mainWindow", u"     You can Sell", None))
        self.ChooseSymboltxt.setText(
            QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Choose Stock Symbol</p></body></html>",
                                       None))
        self.ChooseIndictrtxt.setText(
            QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Choose Indicators</p></body></html>",
                                       None))
        self.menuMenu.setTitle(QCoreApplication.translate("mainWindow", u"Menu", None))
        # retranslateUi

    def logout_button(self):
        app = QApplication.instance()
        app.exit()

    def info_button(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText('Hüseyin Sarkut\nYiğit Emre Ünlü\nPerviz Guliyev\nMuhammed Aydın')
        msg_box.setWindowTitle('Team Info')
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def databaseVeriCek(self):
        self.SymbolBox.clear()
        connection = sqlite3.connect("stock_data.db")
        cursor = connection.cursor()

        cursor.execute("SELECT ticker FROM stock_data")
        veriler = cursor.fetchall()
        for veri in veriler:
            self.SymbolBox.addItem(veri[0])
        connection.close()


    def jsonPull(self, filename):
        try:
            with open(filename, 'r', encoding='ISO-8859-1') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Json dosyası okunamadı {e}")
            return None

    def combineData(self, filename1, filename2):
        data1 = self.jsonPull(filename1)
        data2 = self.jsonPull(filename2)

        combinedValues = []

        if data1:
            combinedValues.extend(data1.values())

        if data2:
            combinedValues.extend(data2.values())

        return combinedValues

    def fillCombobox(self, data):
        if data:
            for item in data:

              self.IndicatorBox2.addItem(str(item))



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

