import PySimpleGUI as sg

sg.theme('Dark')   # Add a touch of color

layout = [
    [sg.Text("Algum texto on 1"),sg.Text("Algum texto on 1"),sg.Text("Algum texto on 1")],
    [sg.Text("Entre com algo na linha 2"), sg.InputText(key="qualuer-coisa")],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window("Window Title", layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values)

window.close()