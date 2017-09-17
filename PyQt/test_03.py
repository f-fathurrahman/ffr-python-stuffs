import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('kucing.jpg'))
        #
        self.show()

class Example02(QWidget):
    def __init__(self,title='This is a title'):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle(title)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex02 = Example02('Made by ffr')
    sys.exit(app.exec_())
