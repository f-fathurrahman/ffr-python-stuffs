#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 150)
w.move(100, 300)
w.setWindowTitle("Simple Window Example")
w.show()

# why use sys.exit ?
# sys.exit ensures a clean exit
# The environment will be informed how the application ended.
sys.exit( app.exec_() )

