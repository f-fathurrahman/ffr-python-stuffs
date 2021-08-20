import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text("Some text of Row 1", font="Arial 15")],
    [sg.Text("Enter something on Row 2", font="Arial 15"), sg.InputText()],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        print("Cancel is pressed.")
        print("I will break now.")
        break
    print("You entered: ", values)

window.close()