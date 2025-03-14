import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv) # only one instantce of app
window = QPushButton("Push Me")
window.show()
app.exec()