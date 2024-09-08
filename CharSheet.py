from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
import sys
from char_sheet_lib.PlayerAttributes import PlayerAttributes
from char_sheet_lib.PlayerDeatails import PlayerDetails
from char_sheet_lib.Proficiencies import Proficiencies

class CharSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Character Sheet")

        main_layout = QVBoxLayout(self)

        player_details = PlayerDetails()
        main_layout.addWidget(player_details)

        player_attributes = PlayerAttributes()
        main_layout.addWidget(player_attributes)

        proficiencies = Proficiencies()
        main_layout.addWidget(proficiencies)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CharSheet()
    win.show()
    app.exec()