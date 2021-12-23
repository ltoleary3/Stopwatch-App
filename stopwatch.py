import time, re
import PySimpleGUI as gui

if __name__ == "__main__":
    # Initialize threads, vars, and window
    elapsedTime = 0
    paused = True
    started = False
    displayTime = 0

    # Define gui window
    layout = [[gui.Text(key='text', justification= 'center', auto_size_text=True, text="Enter previous time in format: HHH:MM:SS", background_color='#121212', text_color='#c3beb6')],
              [gui.Input(key='inputTime', background_color='#222222', text_color='#c3beb6')],
              [gui.Button(auto_size_button=False, button_color="#1f523a", button_text="Start", key="Use"), gui.Button(auto_size_button=False, button_color="#9e2626", button_text="Reset", key="Reset")]]
    window = gui.Window("Stop Watch", layout, element_justification='center', background_color='#121212')

    # Main function
    while (True):
        # Read and update window
        event, values = window.read(timeout=10)

        # Close window
        if event == gui.WINDOW_CLOSED:
            break

        # Start Timer
        if event == 'Use' and started == False:
            # Get start time
            startTime = int(round(time.time() * 100))
            started = True
            # Parse input text
            elapsedTimes = re.sub("[^0-9:]","",values['inputTime']).split(':')
            if len(elapsedTimes) == 3:
                elapsedTime = ((int(elapsedTimes[0]) * 3600) + (int(elapsedTimes[1]) * 60) + int(elapsedTimes[2])) * 100
            else:
                elapsedTime = 0
            paused = False
            window['Use'].update(text='Pause', button_color="gray")
            window['inputTime'].hide_row()
        # Pause Timer
        elif event == 'Use' and paused == False:
            paused = True
            # Update total elapsed time
            elapsedTime = displayTime
            window['Use'].update(text='Resume', button_color="green")
        # Resume Timer
        elif event == 'Use' and paused == True:
            paused = False
            # Set time of restart
            startTime = int(round(time.time() * 100))
            window['Use'].update(text='Pause', button_color="gray")

        # Completely Reset Timer
        elif event == 'Reset':
            paused = True
            started = False
            # Reset to original setup
            startTime = int(round(time.time() * 100))
            window['Use'].update(text='Start', button_color="green")
            window['inputTime'].unhide_row()
            window['text'].update(font='default', value='Enter previous elapsed time in the format: HHH:MM:SS')
            window['Use'].hide_row()
            window['Use'].unhide_row()

        if paused == False:
            # Display timer in window
            displayTime = (int(round(time.time() * 100)) - startTime) + elapsedTime
            window['text'].update(font=('Helvetica', 40), value='{}:{:02d}:{:02d}.{:02d}'.format((displayTime // 100) // 3600,
                                                                    ((displayTime // 100) % 3600) // 60,
                                                                    ((displayTime // 100) % 3600) % 60,
                                                                    displayTime % 100))
