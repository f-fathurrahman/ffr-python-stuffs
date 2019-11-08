import PySimpleGUI as sg

layout = [
    [sg.Text("Some text of Row 1")],
    [sg.Text("Enter something on Row 2"), sg.InputText()],
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