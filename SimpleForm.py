from PySide6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout, QVBoxLayout
    )
import sys, json, os

# Subclass QWidget to define our own window
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        # self.showMaximized()
        self.resize(500, 0)

        # Create layouts for our widgets
        main_layout = QVBoxLayout(self)

        name_layout = QHBoxLayout()
        main_layout.addLayout(name_layout)

        email_layout = QHBoxLayout()
        main_layout.addLayout(email_layout)

        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)

        # create name label and field
        name_lbl = QLabel("Name:")
        name_lbl.setMinimumWidth(120)
        self.name_field = QLineEdit()

        # add them to their layout
        name_layout.addWidget(name_lbl)
        name_layout.addWidget(self.name_field)


        # create email label and field
        email_lbl = QLabel("Email:")
        email_lbl.setMinimumWidth(120)
        self.email_field = QLineEdit()

        # add them to their layout
        email_layout.addWidget(email_lbl)
        email_layout.addWidget(self.email_field)

        # create email label and field
        address_lbl = QLabel("Address:")
        address_lbl.setMinimumWidth(120)
        self.address_field = QLineEdit()

        # add them to their layout
        address_layout.addWidget(address_lbl)
        address_layout.addWidget(self.address_field)

        save_bttn = QPushButton("Save Data")
        main_layout.addWidget(save_bttn)

        # connect signals
        save_bttn.clicked.connect( self.save_data )

        # Try to load user data
        self.load_data()

    def load_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json") as f:
                user_data = json.load(f)
                self.name_field.setText(user_data["name"])
                self.email_field.setText(user_data["email"])
                self.address_field.setText(user_data["address"])


    def save_data(self):
        user_data = {
            "name": self.name_field.text(),
            "email": self.email_field.text(),
            "address": self.address_field.text()
        }

        with open("user_data.json", "w") as f:
            json.dump(user_data, f)

        # Clear all fields
        self.name_field.clear()
        self.email_field.clear()
        self.address_field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    app.exec()