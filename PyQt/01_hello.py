import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

print("PyQt version = ", QtCore.PYQT_VERSION_STR)


class MyWindow( QWidget ):

    def __init__(self, title="Hello PyQt5"):
        
        QWidget.__init__(self)

        self.setWindowTitle(title)
        self.resize(300,100)

        label = QLabel("<center>Hello World!</center>")
        btnQuit = QPushButton("Quit")

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(btnQuit)

        self.setLayout(vbox)
        btnQuit.clicked.connect(app.quit)

app = QApplication(sys.argv)

window = MyWindow()
window.show()

sys.exit( app.exec_() )


sys.exit(app.exec_())