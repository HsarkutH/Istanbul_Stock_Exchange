import pandas
import pandas_ta as ta
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime
import json
from MainMenu import Ui_mainWindow

class indicator_params:
    def callAO(self, stock_name):
        with open('day_value.json', 'r') as file:
            data = json.load(file)
        gun_sayisi = data.get('gunsayisi')
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=gun_sayisi)
        stock_data = yf.download(stock_name, start=start_date, end=end_date)
        ao = stock_data.ta.ao(high='High', low='Low', close='Close', append=True)

        fig, (ax1, ax2) = plt.subplots(2,1, figsize=(15,8))

        mpf.plot(
            stock_data,
            ax=ax1,
            type='candle',
            style='charles',
            #title='THYAO',
            ylabel='Price',
            xlabel='Date',
            #subplots=True
        )
        ax1.set_title(stock_name)

        ax2.plot(stock_data.index, ao, label='AO', color='green')
        ax2.axhline(y=0, color='gray', linestyle='--', label='Zero Line')
        #ax2.set_title(f"{ticker} AO Indicator")
        ax2.set_ylabel('AO')
        ax2.set_xlabel('Date')
        ax2.legend()

        plt.tight_layout()  # Adjust spacing between subplots
        plt.show()

    def callAPO(self, stock_name):
        with open('day_value.json', 'r') as file:
            data = json.load(file)
        gun_sayisi = data.get('gunsayisi')
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=gun_sayisi)
        stock_data = yf.download(stock_name, start=start_date, end=end_date)
        apo = stock_data.ta.apo(high='High', low='Low', close='Close', append=True)

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8))

        mpf.plot(
            stock_data,
            ax=ax1,
            type='candle',
            style='charles',
            #title='THYAO',
            ylabel='Price',
            xlabel='Date',
            # subplots=True
        )
        ax1.set_title(stock_name)

        ax2.plot(stock_data.index, apo, label='APO', color='green')
        ax2.axhline(y=0, color='gray', linestyle='--', label='Zero Line')
        # ax2.set_title(f"{ticker} AO Indicator")
        ax2.set_ylabel('APO')
        ax2.set_xlabel('Date')
        ax2.legend()

        plt.tight_layout()  # Adjust spacing between subplots
        plt.show()

params = indicator_params()
params.callAPO('THYAO.IS')