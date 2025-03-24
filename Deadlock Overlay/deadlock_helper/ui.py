# PySimpleGUI window logic

import PySimpleGUI as sg
from .screen import get_secondary_monitor



def start_main_app():
    monitor = get_secondary_monitor()

    layout = [
        [sg.Text("Deadlock Helper", font=("Helvetica", 20))],
        [sg.Text("More features coming soon...")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Deadlock Helper", layout, finalize=True)
    window.move(monitor.x + 100, monitor.y + 100)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

    window.close()