import time, re
import PySimpleGUI as sg

if __name__ == "__main__":
    # Initialize threads, vars, and window
    elapsedTime = 0
    paused = True
    started = False
    displayTime = 0

    # Define window and elements
    layout = [[sg.Text(text="Enter previous time in format: HHH:MM:SS", key='-TEXT-', justification= 'center', auto_size_text=True, background_color='#121212', text_color='#c3beb6')],
              [sg.Input(key='-INPUT-', background_color='#222222', text_color='#c3beb6')],
              [sg.Button(button_color="#1f523a", button_text="Start", key="-USE-"), sg.Button(button_text="Reset", button_color="#9e2626", key='-RESET-')]]
    window = sg.Window("Stop Watch", layout, element_justification='center', background_color='#121212')

    # Main function
    while (True):
        # Read and update window
        event, values = window.read(timeout=10)

        # Close window
        if event == sg.WINDOW_CLOSED:
            break

        # Start Timer
        if event == '-USE-' and started == False:
            # Get start time
            startTime = int(round(time.time() * 100))
            started = True
            # Parse input text
            elapsedTimes = re.sub("[^0-9:]","",values['-INPUT-']).split(':')
            if len(elapsedTimes) == 3:
                elapsedTime = ((int(elapsedTimes[0]) * 3600) + (int(elapsedTimes[1]) * 60) + int(elapsedTimes[2])) * 100
            else:
                elapsedTime = 0
            paused = False
            window['-USE-'].update(text='Pause', button_color="gray")
            window['-INPUT-'].hide_row()
        # Pause Timer
        elif event == '-USE-' and paused == False:
            paused = True
            # Update total elapsed time
            elapsedTime = displayTime
            window['-USE-'].update(text='Resume', button_color="green")
        # Resume Timer
        elif event == '-USE-' and paused == True:
            paused = False
            # Set time of restart
            startTime = int(round(time.time() * 100))
            window['-USE-'].update(text='Pause', button_color="gray")

        # Completely Reset Timer
        elif event == '-RESET-':
            paused = True
            started = False
            # Reset to original setup
            startTime = int(round(time.time() * 100))
            window['-USE-'].update(text='Start', button_color="green")
            window['-INPUT-'].unhide_row()
            window['-TEXT-'].update(font='default', value='Enter previous elapsed time in the format: HHH:MM:SS')
            window['-USE-'].hide_row()
            window['-USE-'].unhide_row()

        if paused == False:
            # Display timer in window
            displayTime = (int(round(time.time() * 100)) - startTime) + elapsedTime
            window['-TEXT-'].update(font=('Helvetica', 40), value='{}:{:02d}:{:02d}.{:02d}'.format((displayTime // 100) // 3600,
                                                                    ((displayTime // 100) % 3600) // 60,
                                                                    ((displayTime // 100) % 3600) % 60,
                                                                    displayTime % 100))

    window.close()