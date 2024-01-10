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
import pandas as pd

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

        if self.IndicatorBox2.currentText() == 'sma':
            sma20 = stock_data.ta.sma(close= stock_data['Close'] ,length=20)
            plt.plot(stock_data.index, sma20, label='SMA-20')
            sma50 = stock_data.ta.sma(close= stock_data['Close'], length=50)
            plt.plot(stock_data.index, sma50, label='SMA-50')
            buy_signals = (sma20 > sma50) & (sma20.shift(1) <= sma50.shift(1))
            sell_signals = (sma20 < sma50) & (sma20.shift(1) >= sma50.shift(1))
            for index, signal in buy_signals[buy_signals].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))

            for index, signal in sell_signals[sell_signals].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'rsi':
            rsi = stock_data.ta.rsi(length=14)
            plt.plot(stock_data.index, rsi, label='RSI')
            overbought_threshold = 70
            oversold_threshold = 30
            buy_signals_rsi = (rsi < oversold_threshold) & (rsi.shift(1) >= oversold_threshold)
            sell_signals_rsi = (rsi > overbought_threshold) & (rsi.shift(1) <= overbought_threshold)
            for index, signal in buy_signals_rsi[buy_signals_rsi].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signals_rsi[sell_signals_rsi].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'ao':
            ao = stock_data.ta.ao(fast=9, slow=34)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, ao, label='AO')
            buy_signals_ao = (ao > 0) & (ao.shift(1) <= 0)
            sell_signals_ao = (ao < 0) & (ao.shift(1) >= 0)
            for index, signal in buy_signals_ao[buy_signals_ao].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signals_ao[sell_signals_ao].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'apo':
            apo = stock_data.ta.apo(fast=26, slow=50)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, apo, label='APO')
            buy_signals_apo = (apo > 0) & (apo.shift(1) <= 0)
            sell_signals_apo = (apo < 0) & (apo.shift(1) >= 0)
            for index, signal in buy_signals_apo[buy_signals_apo].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signals_apo[sell_signals_apo].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() =='bias':
            bias = stock_data.ta.dpo(length=50)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, bias, label= 'BIAS')
            buy_signals_bias = (bias > 0) & (bias.shift(1) <= 0)
            sell_signals_bias = (bias < 0) & (bias.shift(1) >= 0)
            for index, signal in buy_signals_bias[buy_signals_bias].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signals_bias[sell_signals_bias].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'bop':
            bop = stock_data.ta.bop()
            bop_long_ma = bop.rolling(window=100).mean()
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, bop, label= 'BOP')
            plt.plot(stock_data.index, bop_long_ma, label='BOP 100-Period MA', color='blue')
            buy_signals_bop = (bop > 0) & (bop.shift(1) <= 0)
            sell_signals_bop = (bop < 0) & (bop.shift(1) >= 0)
            for index, signal in buy_signals_bop[buy_signals_bop].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signals_bop[sell_signals_bop].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'cci':
            cci = stock_data.ta.cci(length=10)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, cci, label='CCI')
            buy_signal = cci > 100
            sell_signal = cci < -100
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'cfo':
            cfo = stock_data.ta.cfo()
            plt.plot(stock_data.index, cfo, label='CFO')
            plt.axhline(y=0, color='r', linestyle='--')
            buy_signal = cfo > 0
            sell_signal = cfo < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'cmo':
            cmo = stock_data.ta.cmo(length=14)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, cmo, label='CMO')
            buy_signal = cmo > 50
            sell_signal = cmo < -50
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'coppock':
            coppock10 = stock_data.ta.coppock(length=10)
            coppock20 = stock_data.ta.coppock(length=20)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, coppock10, label='COPPOCK-10')
            plt.plot(stock_data.index, coppock20, label='COPPOCK-20')
            buy_signal = (coppock10 > 0) & (coppock20 > 0)
            sell_signal = (coppock10 < 0) & (coppock20 < 0)
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'cti':
            cti9 = stock_data.ta.cti(length=20)
            cti14 = stock_data.ta.cti(length=50)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index, cti9, label='CTI-20')
            plt.plot(stock_data.index, cti14, label='CTI-50')
            buy_signal = (cti9 > 0) & (cti14 > 0)
            sell_signal = (cti9 < 0) & (cti14 < 0)
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'er':
            er = stock_data.ta.er(length=4)
            plt.plot(stock_data.index, er, label= 'ER')
            buy_signal = er > 0.8
            sell_signal = er < 0.2
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'inertia':
            inertia = stock_data.ta.inertia(length=50)
            plt.plot(stock_data.index,inertia,label= 'INERTIA')
            buy_signal = inertia > 0
            sell_signal = inertia < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'kdj':
            kdj = stock_data.ta.kdj(length=9, k_slowing=3)
            print(kdj.head())
            plt.plot(stock_data.index, kdj['K_9_3'], label='KDJ-K')
            plt.plot(stock_data.index, kdj['D_9_3'], label='KDJ-D')
            plt.plot(stock_data.index, kdj['J_9_3'], label='KDJ-J')
            overbought_condition = (kdj['K_9_3'] > 80) & (kdj['D_9_3'] > 80)
            oversold_condition = (kdj['K_9_3'] < 20) & (kdj['D_9_3'] < 20)
            for index, signal in overbought_condition[overbought_condition].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
            for index, signal in oversold_condition[oversold_condition].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'macd':
            macd = stock_data.ta.macd()
            print(macd.head())
            plt.plot(stock_data.index,macd['MACD_12_26_9'],label = 'MACD')
            plt.plot(stock_data.index, macd['MACDs_12_26_9'], label='Signal Line')
            buy_signal = macd['MACD_12_26_9'] > macd['MACDs_12_26_9']
            sell_signal = macd['MACD_12_26_9'] < macd['MACDs_12_26_9']
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'mom':
            mom = stock_data.ta.mom()
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index,mom,label='MOM')
            buy_signal = mom > 0
            sell_signal = mom < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'pgo':
            pgo = stock_data.ta.pgo()
            plt.axhline(y=0, color='r', linestyle='--')
            plt.plot(stock_data.index,pgo,label='PGO')
            buy_signal = pgo > 0
            sell_signal = pgo < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'psl':
            psl=stock_data.ta.psl(length=50, scalar=2.5)
            plt.plot(stock_data.index,psl,label='PSL')
            buy_signal = psl > 0
            sell_signal = psl < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'roc':
            roc=stock_data.ta.roc()
            plt.plot(stock_data.index,roc,label='ROC')
            plt.axhline(y=0, color='r', linestyle='--')
            buy_signal = roc > 0
            sell_signal = roc < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'rsx':
            rsx=stock_data.ta.rsx()
            plt.plot(stock_data.index,rsx,label='RSX')
            buy_signal = rsx < 30
            sell_signal = rsx > 70
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'slope':
            slope=stock_data.ta.slope()
            plt.plot(stock_data.index,slope,label='SLOPE')
            plt.axhline(y=0, color='r', linestyle='--')
            buy_signal = slope > 0
            sell_signal = slope < 0
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'squeeze':
         #   squeeze=stock_data.ta.squeeze()
          #  plt.plot(stock_data.index,squeeze,label='SQUEEZE')
        #elif self.IndicatorBox2.currentText() == 'squeeze_pro':
         #   squeeze_pro=stock_data.ta.squeeze_pro()
          #  plt.plot(stock_data.index,squeeze_pro,label='SQUEEZE PRO')
        elif self.IndicatorBox2.currentText() == 'stoch':
            stoch=stock_data.ta.stoch()
            print(stoch.columns)
            plt.plot(stoch.index,stoch['STOCHk_14_3_3'],label='STOCH %K')
            plt.plot(stoch.index,stoch['STOCHd_14_3_3'],label='STOCH %D')
            overbought = 80
            oversold = 20
            buy_signal = (stoch['STOCHk_14_3_3'] < oversold) & (stoch['STOCHd_14_3_3'] < oversold)
            sell_signal = (stoch['STOCHk_14_3_3'] > overbought) & (stoch['STOCHd_14_3_3'] > overbought)
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'stochrsi':
            #stochrsi=stock_data.ta.stochrsi()
            #plt.plot(stock_data.index,stochrsi,label='STOCH RSI')
        #elif self.IndicatorBox2.currentText() == 'td_seq':
         #   td_seq=stock_data.ta.td_seq()
          #  plt.plot(stock_data.index,td_seq,label='TD SEQ')
        #elif self.IndicatorBox2.currentText() == 'trix':
         #   trix=stock_data.ta.trix()
          #  plt.plot(stock_data.index,trix,label='TRIX')
        #elif self.IndicatorBox2.currentText() == 'tsi':
         #   tsi=stock_data.ta.tsi()
          #  plt.plot(stock_data.index,tsi,label='TSI')
           # plt.axhline(y=0, color='r', linestyle='--')
        elif self.IndicatorBox2.currentText() == 'uo':
            uo=stock_data.ta.uo()
            plt.plot(stock_data.index,uo,label='UO')
            overbought = 70
            oversold = 30
            buy_signal = uo < oversold
            sell_signal = uo > overbought
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'willr':
            willr=stock_data.ta.willr()
            plt.plot(stock_data.index,willr,label='WILLR')
            overbought = -20
            oversold = -80
            buy_signal = willr > oversold
            sell_signal = willr < overbought
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
            plt.axhline(y=0, color='r', linestyle='--')
        elif self.IndicatorBox2.currentText() == 'alma':
            alma=stock_data.ta.alma()
            plt.plot(stock_data.index,alma,label='ALMA')
            for index, signal in alma[alma > 0].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in alma[alma < 0].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'dema':
            dema=stock_data.ta.dema()
            plt.plot(stock_data.index,dema,label='DEMA')
            buy_signal = dema > stock_data['Close']
            sell_signal = dema < stock_data['Close']
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'ema':
            ema=stock_data.ta.ema()
            plt.plot(stock_data.index,ema,label='EMA')
            buy_signal = stock_data['Close'] > ema
            sell_signal = stock_data['Close'] < ema
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'fwma':
            fwma=stock_data.ta.fwma()
            plt.plot(stock_data.index,fwma,label='FWMA')
            buy_signal = stock_data['Close'] > fwma
            sell_signal = stock_data['Close'] < fwma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'hilo':
         #   hilo=stock_data.ta.hilo()
          #  plt.plot(stock_data.index,hilo,label='HILO')
        elif self.IndicatorBox2.currentText() == 'hl2':
            hl2=stock_data.ta.hl2()
            plt.plot(stock_data.index,hl2,label='HL2')
            buy_signal = stock_data['Close'] > hl2
            sell_signal = stock_data['Close'] < hl2
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'hlc3':
            hlc3=stock_data.ta.hlc3()
            plt.plot(stock_data.index,hlc3,label='HLC3')
            buy_signal = stock_data['Close'] > hlc3
            sell_signal = stock_data['Close'] < hlc3
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'hma':
            hma = stock_data.ta.hma()
            plt.plot(stock_data.index,hma,label='HMA')
            buy_signal = stock_data['Close'] > hma
            sell_signal = stock_data['Close'] < hma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'hwma':
            hwma = stock_data.ta.hwma()
            plt.plot(stock_data.index,hwma,label='HWMA')
            buy_signal = stock_data['Close'] > hwma
            sell_signal = stock_data['Close'] < hwma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'jma':
            jma=stock_data.ta.jma()
            plt.plot(stock_data.index,jma,label='JMA')
            buy_signal = stock_data['Close'] > jma
            sell_signal = stock_data['Close'] < jma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'kama':
         #   kama=stock_data.ta.kama()
          #  plt.plot(stock_data.index,kama,label='KAMA')
        #elif self.IndicatorBox2.currentText() == 'linreg':
         #   linreg = stock_data.ta.linreg()
          #  plt.plot(stock_data.index,linreg,label='LINREG')
        #elif self.IndicatorBox2.currentText() == 'midpoint':
         #   midpoint = stock_data.ta.midpoint()
          #  plt.plot(stock_data.index,midpoint,label='MIDPOINT')
        #elif self.IndicatorBox2.currentText() == 'midprice':
         #   midprice = stock_data.ta.midprice()
          #  plt.plot(stock_data.index,midprice,label='MIDPRICE')
        #elif self.IndicatorBox2.currentText() == 'ohlc4':
         #   ohlc4 = stock_data.ta.ohlc4()
          #  plt.plot(stock_data.index,ohlc4, label='OHLC4')
        elif self.IndicatorBox2.currentText() == 'pwma':
            pwma = stock_data.ta.pwma()
            plt.plot(stock_data.index,pwma,label='PWMA')
            buy_signal = stock_data['Close'] > pwma
            sell_signal = stock_data['Close'] < pwma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'rma':
            rma = stock_data.ta.rma()
            plt.plot(stock_data.index,rma,label='RMA')
            buy_signal = stock_data['Close'] > rma
            sell_signal = stock_data['Close'] < rma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'sinwma':
            sinwma = stock_data.ta.sinwma()
            plt.plot(stock_data.index,sinwma,label= 'SINWMA')
            buy_signal = stock_data['Close'] > sinwma
            sell_signal = stock_data['Close'] < sinwma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'ssf':
            ssf = stock_data.ta.ssf()
            plt.plot(stock_data.index,ssf,label='SSF')
            buy_signal = stock_data['Close'] > ssf
            sell_signal = stock_data['Close'] < ssf
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'supertrend':
         #   supertrend = stock_data.ta.supertrend()
          #  plt.plot(stock_data.index,supertrend,label='SUPERTREND')
        elif self.IndicatorBox2.currentText() == 'swma':
            swma = stock_data.ta.swma()
            plt.plot(stock_data.index,swma,label='SWMA')
            buy_signal = stock_data['Close'] > swma
            sell_signal = stock_data['Close'] < swma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 't3':
            t3 = stock_data.ta.t3()
            plt.plot(stock_data.index,t3,label='T3')
            buy_signal = stock_data['Close'] > t3
            sell_signal = stock_data['Close'] < t3
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'tema':
            tema = stock_data.ta.tema()
            plt.plot(stock_data.index,tema,label='TEMA')
            buy_signal = stock_data['Close'] > tema
            sell_signal = stock_data['Close'] < tema
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'trima':
            trima = stock_data.ta.trima()
            plt.plot(stock_data.index,trima,label='TRIMA')
            buy_signal = stock_data['Close'] > trima
            sell_signal = stock_data['Close'] < trima
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        #elif self.IndicatorBox2.currentText() == 'vidya':
         #   vidya = stock_data.ta.vidya()
          #  plt.plot(stock_data.index,vidya,label='VIDYA')
        elif self.IndicatorBox2.currentText() == 'vwap':
            vwap=stock_data.ta.vwap()
            plt.plot(stock_data.index,vwap,label='VWAP')
            buy_signal = stock_data['Close'] > vwap
            sell_signal = stock_data['Close'] < vwap
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'vwma':
            vwma=stock_data.ta.vwma()
            plt.plot(stock_data.index,vwma,label='VWMA')
            buy_signal = stock_data['Close'] > vwma
            sell_signal = stock_data['Close'] < vwma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'wcp':
            wcp=stock_data.ta.wcp()
            plt.plot(stock_data.index,wcp,label='WCP')
            buy_signal = stock_data['Close'] > wcp
            sell_signal = stock_data['Close'] < wcp
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'wma':
            wma=stock_data.ta.wma()
            plt.plot(stock_data.index,wma,label='WMA')
            buy_signal = stock_data['Close'] > wma
            sell_signal = stock_data['Close'] < wma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        elif self.IndicatorBox2.currentText() == 'zlma':
            zlma=stock_data.ta.zlma()
            plt.plot(stock_data.index,zlma,label='ZLMA')
            buy_signal = stock_data['Close'] > zlma
            sell_signal = stock_data['Close'] < zlma
            for index, signal in buy_signal[buy_signal].items():
                plt.text(index, stock_data['Close'][index], 'Buy', color='green', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='green', boxstyle='round,pad=0.3'))
            for index, signal in sell_signal[sell_signal].items():
                plt.text(index, stock_data['Close'][index], 'Sell', color='red', fontsize=8, va='center',
                         bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
        # Customize the graph
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(stock_Symbol)
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

