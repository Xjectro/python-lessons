import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QGridLayout,
)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New PyQt5 GUI")
        self.setGeometry(550, 250, 800, 600)
        self.setWindowIcon(QIcon("Assets/PyQt5.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label6 = QLabel("#6", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: purple;")
        label6.setStyleSheet("background-color: orange;")

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 0)
        grid.addWidget(label6, 2, 1)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
