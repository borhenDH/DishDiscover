from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import psycopg2
import json
import re
from unidecode import unidecode
from dotenv import load_dotenv
import os
from selenium import webdriver


from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service = Service() # this is the important line of code!

PATH = r"C:\Program Files (x86)\msedgedriver"
service = Service(PATH)

driver = webdriver.Edge(service=service)



driver.get("https://www.allrecipes.com/ingredients-a-z-6740416")

links=[]
try:    
    container = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID,'alphabetical-list_1-0')))
    time.sleep(5)
    alphabets = container.find_elements(By.CLASS_NAME,'alphabetical-list__group')
except:
    print('error in getting links')

for k,alphabet in enumerate(alphabets) :
    ingredients = alphabet.find_elements(By.CLASS_NAME, 'link-list__item')
    time.sleep(5)
    for i,ingredient in enumerate(ingredients):
        link = ingredient.get_attribute("href")
        if i>3 :
            break
        links.append(link)
print(links)