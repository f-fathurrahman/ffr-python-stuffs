import sys
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        pos_x = 100
        pos_y = 100
        width = 400
        height = 300
        self.setGeometry(pos_x, pos_y, width, height)
        self.setWindowTitle('Empty Window in PyQt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())

