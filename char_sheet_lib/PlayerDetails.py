from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QLineEdit

class PlayerDetails(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setTitle("Player Details")
        self.setMaximumHeight(100)

        main_layout = QHBoxLayout(self)

        self.player_name = QLineEdit()
        self.player_name.setPlaceholderText("Player Name")
        main_layout.addWidget(self.player_name)

        player_data_layout = QVBoxLayout()
        main_layout.addLayout(player_data_layout)

        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        player_data_layout.addLayout(h_layout_1)
        player_data_layout.addLayout(h_layout_2)

        self.race_field = QLineEdit()
        self.race_field.setPlaceholderText("Race")

        self.age_field = QLineEdit()
        self.age_field.setPlaceholderText("Age")

        self.height_field = QLineEdit()
        self.height_field.setPlaceholderText("Height")

        h_layout_1.addWidget(self.race_field)
        h_layout_1.addWidget(self.age_field)
        h_layout_1.addWidget(self.height_field)

        self.background_field = QLineEdit()
        self.background_field.setPlaceholderText("Background")

        self.eyes_field = QLineEdit()
        self.eyes_field.setPlaceholderText("Eyes")

        self.hair_field = QLineEdit()
        self.hair_field.setPlaceholderText("Hair")

        h_layout_2.addWidget(self.background_field)
        h_layout_2.addWidget(self.eyes_field)
        h_layout_2.addWidget(self.hair_field)