import remi.gui as gui
from remi import start, App

class MyApp( App ):

    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        # VBox container
        wid = gui.VBox(width=500, height=500) #, style={"align-items" : "center"})

        # text label
        # We will access lbl later in on_button_pressed, so we made it a member of MyApp
        self.lbl = gui.Label("Hello\n Test",
            width="80%", height="50%", style={"white-space" : "pre"})
        wid.append(self.lbl)

        # Button
        btn = gui.Button("Press me!", width=200, height=30)

        # set up listener
        btn.onclick.do(self.on_button_pressed)

        wid.append(btn)

        return wid

    def on_button_pressed(self, emitter):
        self.lbl.set_text("Hello World!")


if __name__ == "__main__":

    start(MyApp, debug=True, port=8001)