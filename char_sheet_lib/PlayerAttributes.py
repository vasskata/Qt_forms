from PySide6.QtWidgets import QGroupBox, QVBoxLayout

class PlayerAttributes(QGroupBox):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)
        self.setTitle("Player Attributes")
        self.setMaximumWidth(250)