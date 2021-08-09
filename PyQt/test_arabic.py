import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from buck2uni import *

class MyWindow(QWidget):

    def __init__(self, btn_label="Hello"):
        
        QWidget.__init__(self)
        
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo windows')
        
        quit = QPushButton(btn_label, self)
        quit.setGeometry(100, 100, 100, 400)
        
        font = quit.font()

        font.setPointSize(16)
        quit.setFont(font)
        quit.clicked.connect(app.quit)


app = QApplication(sys.argv)

window = MyWindow(btn_label=transliterateString("bisomi"))
window.show()

window2 = MyWindow(btn_label="Hello World")
window2.show()

sys.exit(app.exec_())
