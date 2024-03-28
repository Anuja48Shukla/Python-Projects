from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from getpass import getpass

usr = input('Enter Email Id:')
pwd = getpass('Enter Password:')

from selenium.webdriver.chrome.service import Service
#service = Service(executable_path = "C:\\Users\\ashukla\\PycharmProjects\\chromedriver-win64\\chromedriver.exe")
service = Service(executable_path = "./chromedriver.exe")
driver = webdriver.Chrome(service=service)

#var = driver.implicitly_wait()


driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
print ("Password entered")
sleep(1)


login_button = driver.find_element(By.NAME, 'login')
login_button.click()
sleep(1)
print("Done")

print(driver.title)


driver.quit()
print("Finished")
