import PySimpleGUIQt as sg

layout = [
    [sg.Text("Some text of Row 1", font="DejaVu Sans 18", text_color="blue", background_color="green")],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.Read()
    if event in (None, "Cancel"):
        print("Cancel is pressed.")
        print("I will break now.")
        break

window.Close()