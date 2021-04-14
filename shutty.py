
import PySimpleGUI as sg
import webbrowser
from shutdown import *
from datetime import datetime, timedelta

sg.theme('Reddit')
font = ('Courier New', 12)
font_s = ('Courier New', 12)
font_title = ('Courier New', 15, "bold")
font_result = ('Courier New', 9)
font_about = ('Courier New', 12, "underline")

# , 'underline'
layout = [

    [sg.Text('Shutty', font=font_title)],
    [sg.Text('Set the timer to shutdown your pc', font=font)],
    [sg.Text('Hours', size=(10, 1), font=font), sg.InputText(
        key='-HOURS-', size=(9, 1), default_text="1", font=font)],
    [sg.Text('Minutes', size=(15, 1), font=font), sg.Combo(
        list(range(0, 61)), default_value=0, font=font, key='-MINUTES-')],
    [sg.Text('Seconds', size=(15, 1), font=font), sg.Combo(
        list(range(0, 61)), font=font, default_value=0, key='-SECONDS-')],
    [sg.Button('Set time', font=font),
     sg.Button("Abort shutdown", font=font, pad=(20, 0), button_color="red")],
    [sg.Text(size=(400, 1), key="-RESULT-", font=font_result)],
    [sg.Text("About", key="-LINK-", enable_events=True, font=font_about,
             pad=(0, 0), text_color="blue"), sg.Button("     Exit    ", font=font, pad=(80, 0),)]
]

window = sg.Window('Shutty', layout, size=(410, 260))


while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == '     Exit    ':
        break
    # Output a message to the window
    if event == "Set time":
        try:
            minutes = values['-MINUTES-']
            seconds = values['-SECONDS-']
            hours = int(values['-HOURS-'])
            shutdown_time = seconds + (minutes*60) + (hours*60*60)
            if shutdown_time == 0:
                shutdown_time = 1

            time = datetime.now() + timedelta(seconds=shutdown_time)
            shutdown(time=shutdown_time, force=False, warning_off=False)
            #os.system(f"shutdown /s /t {shutdown}")
            # os.system("exit")
            #print((f"shutdown /s /t {shutdown}"))
            window['-RESULT-'].update(
                f'Your computer will shutdown at {str(time)[:-7]}')

        except Exception:
            window['-RESULT-'].update('The hour is not a number')
    if event == "Abort shutdown":
        #os.system(f"shutdown /a")
        # os.system("exit")
        cancel()
        window['-RESULT-'].update(
            f'Shutdown aborted')

    if event == "-LINK-":
        webbrowser.open("www.google.com.ar")

# Finish up by removing from the screen
window.close()
