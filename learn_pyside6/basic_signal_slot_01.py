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
        # title
        self.setWindowTitle("My Awesome App")
        # button
        self.button = QPushButton("Press Me")
        self.button.setCheckable(True) # can be toggled
        self.button.clicked.connect(self.the_button_was_clicked)
        #
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Button is clicked")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

