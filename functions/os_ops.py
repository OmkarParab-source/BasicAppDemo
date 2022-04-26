import os
import subprocess as sp

paths = {
    'notepad': "C:\\WINDOWS\\system32\\notepad.exe",
    'discord': "C:\\Users\\Omkar\\AppData\\Local\\Discord\\Update.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
