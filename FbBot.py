import os
from temp.userpass import passw
from temp.userpass import user
from functions.login import login

def pause():
    programPause = input("Press the ENTER key to Exit...")
    print("Goodbye!...")

def clear():
    os.popen('sh functions/clear.sh')



login(user, passw)
pause()


clear()












