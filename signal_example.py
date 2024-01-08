import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta

# Hisse senedi verilerini çekme
hisse_kodu = 'THYAO.IS'
veriler = yf.download(hisse_kodu, start='2023-01-01', end='2024-01-01')

# StochRSI (Stochastic RSI) hesaplama
stochrsi = veriler.ta.stochrsi(close='Close', high='High', low='Low', k_period=14, d_period=3, d_ma_type='SMA', cumulative=False, append=False)

# StochRSI değerlerini DataFrame'e ekleme
veriler['StochRSI_14_3_3'] = stochrsi['StochRSI_14_3_3']

# Al-sat sinyalleri (sadece indikatör kesişimleri)
veriler['Al_Sinyali'] = (veriler['StochRSI_14_3_3'] > 80) & (veriler['StochRSI_14_3_3'].shift(1) <= 80)
veriler['Sat_Sinyali'] = (veriler['StochRSI_14_3_3'] < 20) & (veriler['StochRSI_14_3_3'].shift(1) >= 20)

# Grafiği çizin
plt.figure(figsize=(12, 8))

# Fiyatları çizin
plt.plot(veriler['Close'], label='Fiyatlar', linewidth=2)

# StochRSI indikatörlerini çizin
plt.plot(veriler['StochRSI_14_3_3'], label='StochRSI_14_3_3', linestyle='--', linewidth=2)

# Al-sat sinyallerini göster
plt.plot(veriler[veriler['Al_Sinyali']].index, veriler['Close'][veriler['Al_Sinyali']], '^', markersize=10, color='g', label='Al Sinyali')
plt.plot(veriler[veriler['Sat_Sinyali']].index, veriler['Close'][veriler['Sat_Sinyali']], 'v', markersize=10, color='r', label='Sat Sinyali')

plt.title(f'{hisse_kodu} Hisse Senedi Analizi')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.grid(True)
plt.show()
