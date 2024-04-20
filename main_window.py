import PySimpleGUI as sg
import os
import libscrc

working_directory = os.getcwd()

layout = [
    [sg.Text("Choose your file: ")],
    [sg.InputText(key="-FILE_PATH-"),
     sg.FileBrowse(initial_folder=working_directory, file_types = [("BIN Files", "*.bin")])],
    [sg.Button("Submit"), sg.Exit()],
    [sg.Text("", key='-RESULT-', size=(50, 1), font=("Arial", 20, 'bold'))],
]

window = sg.Window("CRC32/MPEG2 Converter", layout)

def display_crc(file_address):
    f = open(file_address, mode="rb")

    # Reading file data with read() method
    data = f.read()

    # Printing our byte sequenced data
    print(data)

    # Closing the opened file
    f.close()

    crc32 = libscrc.mpeg2(data)
    return crc32

while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "Submit":
        file_address = value["-FILE_PATH-"]
        window['-RESULT-'].update("CRC/MPEG2 value: " + str(display_crc(file_address)))
        print(display_crc(file_address))

window.close()