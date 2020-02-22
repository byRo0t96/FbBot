import os

def create():
    newpath = r'temp' 
    if not os.path.exists(newpath):
      os.makedirs(newpath)
      f=open("temp/userpass.py", "a+")
      usern = input("Enter username: ")
      passw = input("Enter password: ")
      f.write("user = '{}'\n".format(usern))
      f.write("passw = '{}'\n".format(passw))

create()
