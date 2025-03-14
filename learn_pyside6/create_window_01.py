from PySide6.QtWidgets import QApplication, QWidget

import sys

# sys.argv can be used to allow command line args
app = QApplication(sys.argv)

# create window
window = QWidget()
window.show() # show it, because it is hidden by default

# Start event loop
app.exec()

print("Program is finished")
