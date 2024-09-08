from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
import sys
from char_sheet_lib.PlayerAttributes import PlayerAttributes
from char_sheet_lib.PlayerDetails import PlayerDetails
from char_sheet_lib.Proficiencies import Proficiencies

class CharSheet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D&D Character Sheet")
        self.showMaximized()

        main_layout = QVBoxLayout(self)

        # Create top section for player details
        player_details = PlayerDetails()
        main_layout.addWidget(player_details)

        # Create a horizontal layout for the other two section
        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)

        # Create player attributes section and add this to h_layout
        player_attributes = PlayerAttributes()
        h_layout.addWidget(player_attributes)


        proficiencies = Proficiencies()
        h_layout.addWidget(proficiencies)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CharSheet()
    win.show()
    app.exec()