from PySide6.QtWidgets import QApplication, QWidget
import sys

class CharSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Character Sheet")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CharSheet()
    win.show()
    app.exec()