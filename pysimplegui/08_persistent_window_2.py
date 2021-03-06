import PySimpleGUI as sg

layout = [
    [ sg.Text("Your text appears here"), sg.Text("", key="_OUTPUT_") ],
    [ sg.Input(do_not_clear=True, key="_IN_") ],
    [ sg.Button("Show"), sg.Button("Exit") ],
]

window = sg.Window("Window Title").Layout(layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == "Exit":
        break
    if event == "Show":
        window.FindElement("_OUTPUT_").Update(values["_IN_"])

window.Close()
