from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys

class CharSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Character Sheet")

        main_layout = QVBoxLayout(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CharSheet()
    win.show()
    app.exec()