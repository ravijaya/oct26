from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('/home/ravijaya/Trainings/drivers/chromedriver_linux64/chromedriver')
browser.get('http://127.0.0.1:5000/add')

login, pwd, uid, gid, gecos, home, shell = 'eva', 'eva', '3434', '3434', 'a sample user', '/home/eva', '/bin/bash'

login_element = browser.find_element_by_id('login')
login_element.send_keys(login)

pwd_element = browser.find_element_by_id('pwd')
pwd_element.send_keys(pwd)

uid_element = browser.find_element_by_id('uid')
uid_element.send_keys(uid)


gid_element = browser.find_element_by_id('gid')
gid_element.send_keys(gid)

gecos_element = browser.find_element_by_id('gecos')
gecos_element.send_keys(gecos)

home_element = browser.find_element_by_id('home')
home_element.send_keys(home)

shell_element = browser.find_element_by_id('shell')
shell_element.send_keys(shell)

print(sleep(5))

browser.find_element_by_id('submit').click()