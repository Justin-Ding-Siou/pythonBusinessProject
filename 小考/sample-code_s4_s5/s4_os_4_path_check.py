# Check Path validility

import os

os.path.exists('C:\\Windows')

os.path.exists('C:\\some_made_up_folder')

os.path.isdir('C:\\Windows\\System32')

os.path.isfile('C:\\Windows\\System32')

os.path.isdir('C:\\Windows\\System32\\calc.exe')

os.path.isfile('C:\\Windows\\System32\\calc.exe')