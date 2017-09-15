import sys
from PyQt4 import QtGui, QtCore

from buck2uni import *
import arabic_reshaper
from bidi.algorithm import get_display

#str1 = get_display( arabic_reshaper.reshape( transliterateString('bisomi')) )

str1 = transliterateString('bisomi')

class DemoWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo windows')
        quit = QtGui.QPushButton(str1, self)
        quit.setGeometry(10, 10, 70, 40)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

app = QtGui.QApplication(sys.argv)
dw = DemoWindow()
dw.show()
sys.exit(app.exec_())
