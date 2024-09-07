from PySide6.QtWidgets import (
    QWidget, QApplication, QLabel, 
    QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
    )
import sys

# subclass QWidget to define our own window
class MyForm(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        # self.showMaximized()
        self.resize(500, 0)

# ceate layouts for our window
        main_layout = QVBoxLayout(self)

        name_layout = QHBoxLayout()
        main_layout.addLayout(name_layout)

        email_layout = QHBoxLayout()
        main_layout.addLayout(email_layout)

        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)

        #create name label and field
        name_lbl = QLabel("Name:")
        name_field = QLineEdit()

        #add theme to thier layout
        name_layout.addWidget(name_lbl)
        name_layout.addWidget(name_field)

         #create email label and field
        email_lbl = QLabel("Email:")
        email_field = QLineEdit()
        
        #add theme to thier layout
        email_layout.addWidget(email_lbl)
        email_layout.addWidget(email_field)

        #create address label and field
        address_lbl = QLabel("Name:")
        address_field = QLineEdit()
        
        #add theme to thier layout
        address_layout.addWidget(address_lbl)
        address_layout.addWidget(address_field)

        button = QPushButton("Save")
        main_layout.addWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    app.exec()