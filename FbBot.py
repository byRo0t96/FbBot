import os
from selenium import webdriver
from time import sleep
from userpass import passw
from userpass import user

def pause():
    programPause = raw_input("Press the ENTER key to Exit...")
    print("Goodbye!...")

def clear():
    os.remove("userpass.pyc")


class FbBot_login:
    def __init__(self, user, passw):
        self.driver = webdriver.Chrome()
        print("\033[05m loading... \033[25m ")
        self.driver.get("https://facebook.com")
        sleep(2)

        try:
          self.driver.find_element_by_xpath("//input[@name=\"email\"]")
        except:
          print("ERROR: i can not login.")
          x = "F"
          sleep(2)
        else:
          self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
              .send_keys(user)
          print("puting username")
          self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
              .send_keys(passw)
          print("puting password")
          try:
            self.driver.find_element_by_xpath('//input[@type="submit"]')
          except:
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"
          else:
            self.driver.find_element_by_xpath('//input[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"

        try:
          self.driver.find_element_by_xpath("//input[@name=\"email\"]")
        except:
          if x == "F":
            print("")
            sleep(2)
          else:
            print("Password correct.")
            sleep(2)
        else:
          print("Try to login again...")
          self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
              .send_keys(passw)
          print("puting password")
          try:
            self.driver.find_element_by_xpath('//input[@type="submit"]')
          except:
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"
          else:
            self.driver.find_element_by_xpath('//input[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"

        try:
          self.driver.find_element_by_xpath("//input[@name=\"email\"]")
        except:
          if x == "F":
            print("")
            sleep(2)
          else:
            print("Password correct.")
            sleep(2)
        else:
          npassw = raw_input("\nEnter other password: ")
          self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
              .send_keys(npassw)
          print("puting new password")
          try:
            self.driver.find_element_by_xpath('//input[@type="submit"]')
          except:
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"
          else:
            self.driver.find_element_by_xpath('//input[@type="submit"]')\
                .click()
            sleep(2)
            x = "T"

        try:
          self.driver.find_element_by_xpath("//input[@name=\"approvals_code\"]")
        except:
          if x == "F":
            print("")
            sleep(2)
          else:
            print("Two-Factor Authentication not Required.")
            sleep(2)

        else:
          print("Two-Factor Authentication Required: ")
          sleep(2)
          tf = raw_input("\nWhen you receive your 6-digit code, enter it to continue: ")
          self.driver.find_element_by_xpath("//input[@name=\"approvals_code\"]")\
              .send_keys(tf)
          print("puting 6-digit code")
          self.driver.find_element_by_xpath('//button[@type="submit"]')\
              .click()
          sleep(2)





FbBot_login(user, passw)
pause()


clear()












