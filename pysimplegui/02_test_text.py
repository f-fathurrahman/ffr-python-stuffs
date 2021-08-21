import PySimpleGUI as sg

layout = [
    [sg.Text("Some text of Row 1", font="Courier 18",
        text_color="blue", background_color="white")],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.Read()
    print("event = ", event)
    print("values = ", values)
    if event in (None, "Cancel"):
        print("Cancel is pressed.")
        print("I will break now.")
        break

window.Close()