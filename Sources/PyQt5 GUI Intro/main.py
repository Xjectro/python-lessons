import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New PyQt5 GUI")
        self.setGeometry(550, 250, 800, 600)
        self.setWindowIcon(QIcon("Assets/PyQt5.png"))
        self.setStyleSheet("background-color: yellow;")

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 800, 600)
        label.setStyleSheet(
            "color: blue;" "font-weight: bold;" "text-decoration: underline;"
        )

        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVTop) # CENTER & CENTER

        label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
