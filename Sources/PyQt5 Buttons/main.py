import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
   QPushButton,QLabel
)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New PyQt5 GUI")
        self.setGeometry(550, 250, 800, 600)
        self.setWindowIcon(QIcon("Assets/PyQt5.png"))
        self.initUI()

    def initUI(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
