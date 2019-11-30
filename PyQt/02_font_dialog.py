import sys
from PyQt5.QtWidgets import QFontDialog, QApplication

class MyFontDialog( QFontDialog ):

    def __init__(self):
        QFontDialog.__init__(self)

        self.fontSelected.connect( self.on_font_selected )


    def on_font_selected(self):

        font = self.currentFont()
        print("Name:   %s" % (font.family()))

    def run(self):
        self.show()


app = QApplication(sys.argv)

screen = MyFontDialog()
screen.run()


sys.exit(app.exec_())
