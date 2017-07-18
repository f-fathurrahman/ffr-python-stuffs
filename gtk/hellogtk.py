from __future__ import print_function
import pygtk
pygtk.require20
import gtk

class HelloWorld:
    #
    def __init__(self):

        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # When the window is given the "delete_event" signal
        # we ask it to call the delete_event() function defined below.
        # The data passed to the callback function is null and is ignored
        self.window.connect('delete_event', self.delete_event)

        self.window.connect('destroy', self.destroy)

        self.window.set_border_width(10)

        # Add a button
        self.button = gtk.Button('Say Hello')
        self.button.connect('clicked', self.hello, None)
        self.button.connect_object('clicked', gtk.Widget.destroy, self.window)

        self.window.add(self.button)

        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

    def hello(self, widget, data=None):
        print('Hello World from ffr')

    def delete_event(self, widget, event, data=None):
        # useful for 'are you sure you want to quit?' dialogs
        print('delete_event occured')
        # change False to True and the main window will not be destroyed
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

if __name__ == '__main__':
    hello = HelloWorld()
    hello.main()
