from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import re, getpass, time, subprocess
user  = getpass.getuser()
#print(user)
subprocess.run("taskkill /f /im chrome.exe 2> nul && taskkill /f /im chromedriver.exe 2> nul", shell=True)
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("user-data-dir=C:\\Users\\"+user+"\\AppData\\Local\\Google\\Chrome\\User Data")
browser = webdriver.Chrome(executable_path="C:\\Users\\Farouk\\Desktop\\python projects\\chromedriver.exe", options=options)
browser.get("https://web.whatsapp.com/")
delay = 500
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[1]')))
    time.sleep(5)
except TimeoutException:
    print ("Loading took too much time!")
time.sleep(20)
hh = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[1]")
hh.click()
contacts = []
count = 0
while count < 20:
    lk = browser.find_elements_by_css_selector("span[dir='auto'][class='_19RFN _F7Vk']")
    for i in lk:
        #print(i.text)
        if i.text not in contacts:
            contacts.append(i.text)
    #ActionChains(browser).move_to_element(lk[0]).perform()    
    browser.execute_script("arguments[0].scrollIntoView();", lk[0])
    count+=1
k = open("C:\\Users\\"+user+"\\Desktop\\contacts that can view my status.txt","w+")
for contact in contacts:
    k.write(contact+"\n")
k.close()
print(contacts)
browser.quit()
