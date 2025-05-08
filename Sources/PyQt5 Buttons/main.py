import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New PyQt5 GUI")
        self.setGeometry(550, 250, 800, 600)
        self.label = QLabel("Hello", self)
        self.button = QPushButton("Click Me", self)
        self.setWindowIcon(QIcon("Assets/PyQt5.png"))
        self.initUI()

    def initUI(self):
        self.button.setGeometry(
            ((self.width() - 200) // 2), ((self.height() - 100) // 2), 200, 100
        )
        self.button.setStyleSheet("font-size: 20px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(
            ((self.width() - 200) // 2), ((self.height() - 200) // 2), 200, 50
        )
        self.label.setStyleSheet("font-size: 20px;")

    def on_click(self):
        print("Button clicked!")
        self.label.setText("Goodbye")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
