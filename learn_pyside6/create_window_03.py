import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv) # only one instantce of app
window = QMainWindow()
window.show()
app.exec()