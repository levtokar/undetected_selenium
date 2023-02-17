#The code is a Python script that automates logging into a website and performs some actions using the undetected Selenium web driver library. 
#It's needed to aovid firewall, and download required zip file
#It's done through emulating user's interactions

#importing needed libraries
import subprocess
import sys
import time
import shutil
import ctypes
from pynput.keyboard import Key, Controller
from threading import Timer
from os.path import isfile, join, abspath
from inspect import getsourcefile
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc


# Define a function to handle exceptions
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    sys.exit(-1)

# Set the exception handler
sys.excepthook = show_exception_and_exit

# Define a function to automate the login process
def login_cms():
    # Navigate to the login page
    driver.get("https://www.parfum.kz/admin/login")#?locale=ru

    # Wait for the page to load
    time.sleep(15)

    # Navigate to the login page again (just in case)
    driver.get("https://www.parfum.kz/admin/login")#?locale=ru

    # Wait for the page to load
    time.sleep(15)

    # Fill in the login form
    driver.execute_script('document.getElementById("phone_or_email").value="email"')  
    time.sleep(1) 
    driver.execute_script('document.getElementById("password").value="password"') 
    time.sleep(1) 

    # Submit the login form
    driver.execute_script('document.getElementsByClassName("login_form-submit").item(0).click()') 

    # Wait for the page to load
    time.sleep(5)

    # Navigate to the category management page
    driver.get("https://www.parfum.kz/admin2/categories/-1#") #driver.get("https://www.parfum.kz/admin2/categories/-1#")#?locale=ru
    time.sleep(5)

    # Open the context menu for the root category
    driver.execute_script('document.getElementsByClassName("ctxmenu-toggle glyphicon").item(0).click()')
    time.sleep(2)

    # Click on the "Export" option in the context menu
    driver.execute_script('document.getElementsByClassName("treeicon-context-menu-export").item(0).click()')
    
    # Wait for the export to complete (10 minutes) downloading zip file. External programm will intercept it, when it's done.
    time.sleep(600)
    
    
#This code removes a specific directory using the shutil library, waits for 5 seconds, and then sets the path to the directory where the Chrome browser is located.
#it is needed to clean up chromedriver which is downloaded on every execution. Path was hardcoded, but of course it could be made dynamic
try: 
  shutil.rmtree("C:\\Users\\Администратор\\AppData\\Roaming\\undetected_chromedriver")
except:
  pass
time.sleep(5)

dir_path ='C:/Release'

#Initializes undetected Chrome web driver and waits for 10 seconds.
driver = uc.Chrome()
time.sleep(10)

#The login_cms() function is called in a try-except block. If it fails, nothing happens and the code moves on to close the driver and exit the program.
try: 
   login_cms()  
   driver.close()
except:
    pass    #Reverse1 



driver.close()
time.sleep(5)
exit()


#The last line is a comment to instruct PyInstaller to package the code into a single executable file using CMD.
#pyinstaller test33.py --onefile    
