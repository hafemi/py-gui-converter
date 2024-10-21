import PySimpleGUI as pg

pg.theme('DarkBlue') # Sets a theme for the window.
sumtext = '' # Makes sure the sumtext variable starts blank.
numpad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

layout = [  # Creates the layout for the window.
    [pg.InputText(sumtext, key='output', size=(12,2))],
    [[pg.Button(f'{number}', size=(2,1), key=f'{number}') for number in row] for row in numpad],
    [pg.Button('0', key=0, size=(2,1)), pg.Button('=', key='=', size=(2,1)), pg.Button('+', key='+', size=(2,1))],
    [pg.Button('Close', key='close')]
]

window = pg.Window('Calculator', layout) # Creates the window.

while True:

    event, values = window.read()  # Reads events and values in the 'window' at the current time and prints them.
    print(event, values)

    if event in (pg.WINDOW_CLOSED, 'close'): # Creates a way to close the window without error.import PySi
        break
    elif str(event) in '0123456789+': # Checks if the string is one in the variable.
        sumtext += str(event)
        window['output'].update(sumtext) # Updates the input text.
    elif event == '=':
        try:
            result = eval(sumtext) # Evaluates the variable 'sumtext' as Python code and executes it.
            print(result)
        except SyntaxError: # Handles syntax errors with a pop-up error message.
            pg.popup_error('Syntax Error: Enter a real sum idiot.')
        

window.close() # Closes the window.