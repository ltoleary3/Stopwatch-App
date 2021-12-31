import time, re
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

if __name__ == "__main__":
    # Initialize threads, vars, and window
    elapsedTime = 0
    paused = True
    started = False
    displayTime = 0
    startTime = 0

    # Define Settings window
    menuDefTitlebarOff = ['', ['File', ['Load Time', 'Save Time', 'Exit'],
                     'Edit', ['Title Bar On'],
                     'Help']]
    menuDefTitlebarOn = ['', ['File', ['Load Time', 'Save Time', 'Exit'],
                     'Edit', ['Title Bar Off'],
                     'Help']]

    # Define main window and elements
    sg.theme('Dark Gray 10')
    layout = [[sg.pin(sg.Titlebar('Stop Watch', key='-TITLEBAR-'), expand_x=True)],
              [sg.Text(text='Enter previous time in format: HHH:MM:SS', key='-TEXT-', justification= 'center', font='default')],
              [sg.pin(sg.Input(key='-INPUT-'))],
              [sg.Button(button_text='Start', button_color='#1f523a', key='-USE-'), sg.Button(button_text='Reset', button_color='#9e2626', key='-RESET-'),
               sg.ButtonMenu('Settings', menuDefTitlebarOn, key='-SETTINGS-')]]
    window = sg.Window('Stop Watch', layout, element_justification='center')

    # Main function
    while (True):
        # Read and update window
        event, values = window.read(timeout=10)

        # Close window
        if event == sg.WINDOW_CLOSED or (event == '-SETTINGS-' and values['-SETTINGS-'] == 'Exit'):
            break

        # Start Timer
        if event == '-USE-' and started == False:
            # Get start time
            startTime = int(round(time.time() * 100))
            started = True
            # Parse input text
            elapsedTimes = re.sub('[^0-9:]','',values['-INPUT-']).split(':')
            if len(elapsedTimes) == 3:
                print(elapsedTimes[2])
                if len(elapsedTimes[2]) > 2:
                    elapsedTime = ((int(elapsedTimes[0]) * 3600) + (int(elapsedTimes[1]) * 60)) * 100 + int(elapsedTimes[2])
                else:
                    elapsedTime = ((int(elapsedTimes[0]) * 3600) + (int(elapsedTimes[1]) * 60) + int(elapsedTimes[2])) * 100
            paused = False
            window['-USE-'].update(text='Pause', button_color='gray')
            window['-INPUT-'].update(visible=False)
        # Pause Timer
        elif event == '-USE-' and paused == False:
            paused = True
            # Update total elapsed time
            elapsedTime = displayTime
            window['-USE-'].update(text='Resume', button_color='green')
        # Resume Timer
        elif event == '-USE-' and paused == True:
            paused = False
            # Set time of restart
            startTime = int(round(time.time() * 100))
            window['-USE-'].update(text='Pause', button_color='gray')

        # Completely Reset Timer
        if event == '-RESET-':
            paused = True
            started = False
            elapsedTime = 0
            window['-INPUT-'].update(value='')
            # Reset to original setup
            startTime = int(round(time.time() * 100))
            window['-USE-'].update(text='Start', button_color='green')
            window['-INPUT-'].update(visible=True)
            window['-TEXT-'].update(font='default', value='Enter previous time in format: HHH:MM:SS')
        
        if event == '-SETTINGS-' and values['-SETTINGS-'] == 'Save Time':
            try:
                file = open('stopWatchSave.txt', 'w')
                file.write(str(displayTime))
                file.close()
            except:
                sg.popup_error(title='Could not save time')
        elif event == '-SETTINGS-' and values['-SETTINGS-'] == 'Load Time':
            try:
                file = open('stopWatchSave.txt', 'r')
                loadedTime = int(file.read())
                file.close()
            except:
                sg.popup_error(title='Could not load previous time')
            
            if started == False:
                window['-INPUT-'].update(value='{}:{:02d}:{:02d}.{:02d}'.format((loadedTime // 100) // 3600,
                                                                    ((loadedTime // 100) % 3600) // 60,
                                                                    ((loadedTime // 100) % 3600) % 60,
                                                                    loadedTime % 100))
        
        if event == '-SETTINGS-' and values['-SETTINGS-'] == 'Title Bar On':
            window['-SETTINGS-'].update(menu_definition=menuDefTitlebarOn)
            window['-TITLEBAR-'].update(visible=True)
            window.grab_any_where_off()
        elif event == '-SETTINGS-' and values['-SETTINGS-'] == 'Title Bar Off':
            window['-SETTINGS-'].update(menu_definition=menuDefTitlebarOff)
            window['-TITLEBAR-'].update(visible=False)
            window.grab_any_where_on()


        if paused == False:
            # Display timer in window
            displayTime = (int(round(time.time() * 100)) - startTime) + elapsedTime
            window['-TEXT-'].update(font=('Helvetica', 40), value='{}:{:02d}:{:02d}.{:02d}'.format((displayTime // 100) // 3600,
                                                                    ((displayTime // 100) % 3600) // 60,
                                                                    ((displayTime // 100) % 3600) % 60,
                                                                    displayTime % 100))

    window.close()