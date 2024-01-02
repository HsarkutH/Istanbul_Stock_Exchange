import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import yfinance as yf
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from datetime import datetime

class StockChartApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stock Chart with Indicator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Combobox for selecting indicator
        self.indicator_combobox = QComboBox()
        self.indicator_combobox.addItem("None")
        self.indicator_combobox.addItems(["SMA", "RSI"])  # Add more indicators as needed
        self.layout.addWidget(self.indicator_combobox)

        # QLineEdit for entering stock symbol
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Enter stock symbol")
        self.layout.addWidget(self.symbol_input)

        # Button to update stock chart
        self.update_button = QPushButton("Update Chart")
        self.update_button.clicked.connect(self.update_chart)
        self.layout.addWidget(self.update_button)

        # Matplotlib FigureCanvas for displaying the stock chart
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Add NavigationToolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.addToolBar(self.toolbar)

        # Connect the combobox signal to the slot for indicator selection
        self.indicator_combobox.currentIndexChanged.connect(self.update_chart)

        # Initial symbol and data
        self.symbol = None
        self.data = None

    def plot_stock_chart(self):
        ax = self.figure.add_subplot(111)
        ax.clear()

        ohlc = self.getCandlestickData(self.data)
        candlestick_ohlc(ax, ohlc, width=0.6, colorup='g', colordown='r')

        # Format x-axis as dates
        ax.xaxis_date()

        # Enable zooming
        ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        self.figure.autofmt_xdate()

        # Apply tight layout
        self.figure.tight_layout()

        # Redraw canvas
        self.canvas.draw()

    def getCandlestickData(self, data):
        ohlc = []
        for date, row in data.iterrows():
            open, high, low, close = row["Open"], row["High"], row["Low"], row["Close"]
            ohlc.append((mdates.date2num(date), open, high, low, close))
        return ohlc

    def update_chart(self):
        selected_indicator = self.indicator_combobox.currentText()
        new_symbol = self.symbol_input.text().upper()  # Convert symbol to uppercase

        # Check if the symbol has changed
        if new_symbol != self.symbol:
            # Set new symbol and download new data
            self.symbol = new_symbol
            self.data = yf.download(self.symbol, start="2010-01-01", end=datetime.now().strftime('%Y-%m-%d'))

            # Set new title
            self.figure.suptitle(self.symbol)

            # Clear previous plot
            self.figure.clear()

            # Plot stock price
            self.plot_stock_chart()

            # Redraw canvas
            self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = StockChartApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
