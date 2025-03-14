import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        #
        self.button_is_checked = True
        # title
        self.setWindowTitle("My Awesome App")
        # button
        self.button = QPushButton("Press Me")
        self.button.setCheckable(True) # True: can be toggled
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)
        #
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("self.button_is_checked", self.button_is_checked)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

