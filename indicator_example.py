import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import yfinance as yf

class FinanceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Finance App')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.canvas = PlotCanvas(self, width=5, height=4)
        self.layout.addWidget(self.canvas)

        self.load_data_button = QPushButton('Load Data', self)
        self.layout.addWidget(self.load_data_button)
        self.load_data_button.clicked.connect(self.load_data)

    def load_data(self):
        symbol = "THYAO.IS"
        start_date = "2022-01-01"
        end_date = "2023-01-01"
        data = yf.download(symbol, start=start_date, end=end_date)

        self.canvas.plot_data(data)

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)

    def plot_data(self, data):
        self.ax.clear()

        # Buraya finansal göstergelerinizi çizme kodlarını ekleyin
        self.ax.plot(data['Close'], label='Close Price', alpha=0.5)
        # Örnek olarak SMA eklendi
        self.ax.plot(data['Close'].rolling(window=50).mean(), label='SMA 50', linestyle='--', alpha=0.7)

        self.ax.set_title('Finance Indicators')
        self.ax.legend()
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinanceApp()
    window.show()
    sys.exit(app.exec())