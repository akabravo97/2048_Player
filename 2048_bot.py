import time
import os
import requests
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox(executable_path='D:\\geckodriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')
home=browser.find_element_by_tag_name('html')
time.sleep(10)
while(True):
    choice=random.randint(1,4)
    if(choice==1):
     home.send_keys(Keys.ARROW_UP)
    elif(choice==2):
        home.send_keys(Keys.ARROW_DOWN)
    elif(choice==3):
        home.send_keys(Keys.ARROW_LEFT)
    elif(choice==4):
        home.send_keys(Keys.ARROW_RIGHT)
