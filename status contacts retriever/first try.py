import pyautogui
import subprocess
import re, getpass
user  = getpass.getuser()
print(user)
wh = pyautogui.size()
print(wh)
app = subprocess.Popen("C:\\Users\\" + str(user) +"\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
print("WhatsApp opened")

