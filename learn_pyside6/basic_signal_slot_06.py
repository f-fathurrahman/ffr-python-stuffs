import sys
from random import choice

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "My App 1",
    "My App 2",
    "Still My App 1",
    "Still My App 2",
    "What on earth 1",
    "What on earth 2",
    "This is surprising 1",
    "This is surprising 2",
    "Something went wrong",
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0
        
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title to %s" % new_window_title)
        self.setWindowTitle(new_window_title)
    
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()