import PySimpleGUI as sg
import utils as ut
sg.theme('Topanga')


def image_converter_layout():
    image_path = [
        sg.Column([
            [sg.Text('Image -'), sg.Text(key='-IMAGE_NAME-'), sg.Input(
                key='-IMAGE_PATH-', visible=False, enable_events=True), sg.FileBrowse()],
            [sg.Text('Folder -'), sg.Text(key='-FOLDER_NAME-'), sg.Input(
                key='-FOLDER_PATH-', visible=False, enable_events=True), sg.FolderBrowse()]
        ])
    ]
    format_dropdown = [
        sg.Column([
            [sg.Text('Save as:'),
             sg.DropDown(['PNG', 'JPG', 'JPEG', 'PPM', 'GIF', 'TIFF',
                         'BMP'], readonly=True, key='-FORMAT_COMBO-'),
             ]
        ])
    ]
    convert_button = [sg.Button('Convert', key='-CONVERT_IMAGE-')]

    layout = image_path, format_dropdown, convert_button
    return layout


def units_converter_layout():
    font = ('Arial', 12)
    selected_unit = ''
    units = ['Length', 'Temperature', 'Weight', 'Time',
             'Bytes', 'Speed', 'Volume', 'Area', 'Energy']

    inputfields = sg.Column([
        [sg.Text('', size=(0, 2))],
        [sg.Text('From', font=font)],
        [sg.DropDown(values=ut.get_conversionlist(selected_unit), readonly=True, key='-SOURCE_UNIT-',
                     size=(13)), sg.Input('', size=(25), key='-CONVERSION_INPUT-', enable_events=True)],
        [sg.Text('To', font=font)],
        [sg.DropDown(values=ut.get_conversionlist(selected_unit), readonly=True, key='-TARGET_UNIT-',
                     size=(13)), sg.Text('='), sg.Text('', size=(25), key='-CONVERSION_RESULT-')],
        [sg.Text('Formula:', key='-CONVERSION_FORMULA-', font=font)]
    ])

    convert_column = sg.Column([
        [sg.Text('Converter', key='-TITLE-', font=('Arial', 25))],
        [sg.Text('', key='-CONVERSION_ERROR-', font=font)],
        [inputfields]
    ], vertical_alignment='top')

    units_buttons_column = sg.Column([
        [sg.Button(f'{unit}', size=(12), key=f'-{unit.upper()}-', font=font)] for unit in units
    ])

    layout = [
        [units_buttons_column, convert_column]
    ]
    return layout


layout = [[sg.TabGroup([[sg.Tab('Units', units_converter_layout(), key='-UNITS_TAB-'),
                         sg.Tab('Images', image_converter_layout(), key='-IMAGES_TAB-')]], enable_events=True, key='-TABS-')]]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if values['-TABS-'] == '-UNITS_TAB-':
        ut.manage_unit_converter(event, values, window)
    if values['-TABS-'] == '-IMAGES_TAB-':
        ut.manage_tab_converter(event, values, window)

window.close()
