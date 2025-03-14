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
        self.button.clicked.connect(self.the_button_was_clicked)
        #
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already cliked me")
        self.button.setEnabled(False)
        self.setWindowTitle("My Oneshot App")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

