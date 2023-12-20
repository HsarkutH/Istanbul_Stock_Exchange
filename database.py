import yfinance as yf
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('stock_data.db')
cursor = conn.cursor()

# Create a table to store stock data
cursor.execute('''CREATE TABLE IF NOT EXISTS stock_data
                (ticker TEXT, date TEXT, open REAL, high REAL, low REAL, close REAL, volume INTEGER)''')

# List of stock tickers for Istanbul Stock
stock_tickers = ['ACSEL.IS', 'ADEL.IS', 'ADESE.IS']

# Iterate through each stock ticker
for ticker in stock_tickers:
    # Fetch the stock data using yfinance
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')

    # Insert data into the table
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (ticker, index.strftime('%Y-%m-%d'), row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))

# Commit the changes and close the connection
conn.commit()
conn.close()