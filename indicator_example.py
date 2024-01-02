import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox
import pyqtgraph as pg
import yfinance as yf
import pandas_ta as ta

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

        # PyQtGraph PlotWidget for displaying the stock chart
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        # Connect the combobox signal to the slot for indicator selection
        self.indicator_combobox.currentIndexChanged.connect(self.update_chart)

        # Initial symbol and data
        self.symbol = "AAPL"
        self.data = yf.download(self.symbol, start="2022-01-01", end="2023-01-01")

        # Initial plot
        self.plot_stock_chart()

    def plot_stock_chart(self):
        self.plot_widget.clear()

        # Plot stock closing prices as a line
        self.plot_widget.plot(self.data.index, self.data["Close"], name="Close", pen=pg.mkPen(color="b"))

    def plot_indicator(self, indicator_values, name):
        self.plot_widget.plot(self.data.index, indicator_values, name=name)

    def update_chart(self):
        selected_indicator = self.indicator_combobox.currentText()

        # Clear previous indicator plot
        self.plot_widget.clearPlots()

        # Plot stock price
        self.plot_stock_chart()

        # Plot selected indicator
        if selected_indicator == "SMA":
            sma_values = self.data.ta.sma(length=20)
            self.plot_indicator(sma_values, "SMA")
        elif selected_indicator == "RSI":
            rsi_values = self.data.ta.rsi(length=14)
            self.plot_indicator(rsi_values, "RSI")

def main():
    app = QApplication(sys.argv)
    window = StockChartApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
