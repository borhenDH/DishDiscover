from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
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


PATH = r"C:\Program Files (x86)\msedgedriver"
service = Service(PATH)
driver = webdriver.Edge(service=service)


driver.get("https://www.allrecipes.com/ingredients-a-z-6740416")
time.sleep(5)
links=[]
try:    
    container = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.ID,'alphabetical-list_1-0')))
    
    alphabets = container.find_elements(By.CLASS_NAME,'alphabetical-list__group')
    print(alphabets)
except:
    print('error in getting links')

for k,alphabet in enumerate(alphabets) :
    list_of_ingredients = alphabet.find_element(By.TAG_NAME, 'ul')
    ingredient=list_of_ingredients.find_elements(By.TAG_NAME,"li")
    for i,element in enumerate(ingredient):
        
        link_container = element.find_element(By.TAG_NAME,"a")
        link = link_container.get_attribute("href")
        links.append(link)


