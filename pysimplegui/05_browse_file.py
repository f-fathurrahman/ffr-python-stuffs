import PySimpleGUI as sg

ret_values = sg.Window("Get filename example").Layout(
    [
        [ sg.Text("Filename") ],
        [ sg.Input(), sg.FileBrowse() ],
        [ sg.OK(), sg.Cancel() ]
    ]
).Read()


print(type(ret_values))
print(ret_values)