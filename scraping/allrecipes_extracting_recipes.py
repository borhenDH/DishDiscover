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
recipes_links = []
links  = pd.read_excel("links_sheet.xlsx")
links_list = links['Links'].tolist()
for link in links_list :
    driver.get(link)
    time.sleep(4)
    container = driver.find_element(By.ID,"mntl-taxonomysc-article-list-group_1-0")
    cards = container.find_elements(By.CLASS_NAME,"mntl-card-list-items")
    for i,card in enumerate(cards) :
        recipe_link = card.get_attribute("href")
        recipes_links.append(recipe_link)
df = pd.DataFrame({'recipes_Links': recipes_links})
df.to_excel("recipes_links_sheet.xlsx", index=False)
