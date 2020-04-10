import os
import sys
from functions.login import login

def pause():
    programPause = input("Press the ENTER key to Exit...")
    print("Goodbye!...")

def clear():
    os.popen('sh functions/clear.sh')

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

Banner = """\033[37m
╔═╗┌┐ ╔╗ ┌─┐┌┬┐
╠╣ ├┴┐╠╩╗│ │ │ 
╚  └─┘╚═╝└─┘ ┴ Beta2
\033[91mhttps://github.com/byRo0t96\033[37m\n"""

cls()

print (Banner)

try:
    user = sys.argv[1]
    passw = sys.argv[2]

except:
    print('Usage: python start.py username password\n')
    clear()
    sys.exit()

login(user, passw)
pause()
clear()












