import yfinance as yf
import sqlite3
import json

# Connect to SQLite database
conn = sqlite3.connect('stock_data.db')
cursor = conn.cursor()

# Create a table to store stock data
cursor.execute('''CREATE TABLE IF NOT EXISTS stock_data
                (ticker TEXT, stock_name TEXT, date TEXT, open REAL, high REAL, low REAL, close REAL, volume INTEGER)''')

# Read stock tickers and names from JSON file
with open('stock_data.json', 'r') as json_file:
    stock_data = json.load(json_file)

# Fetch and insert stock data into the table
for ticker, stock_name in stock_data.items():
    # Fetch the stock data using yfinance
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d')

    # Insert data into the table, checking for duplicates
    for index, row in data.iterrows():
        cursor.execute("SELECT * FROM stock_data WHERE ticker=? AND date=?", (ticker, index.strftime('%Y-%m-%d')))
        existing_data = cursor.fetchone()
        if not existing_data:
            cursor.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (ticker, stock_name, index.strftime('%Y-%m-%d'), row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))

# Commit the changes and close the connection
conn.commit()
conn.close()