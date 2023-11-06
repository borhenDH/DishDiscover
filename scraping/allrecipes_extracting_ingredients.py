from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import time
from unidecode import unidecode
from dotenv import load_dotenv



PATH = r"C:\Program Files (x86)\msedgedriver"
service = Service(PATH)
driver = webdriver.Edge(service=service)
recipes_links = []
recipe=[]
ingredients=[]
direction=[]
links  = pd.read_excel("recipes_links_sheet.xlsx")
links_list = links['recipes_Links'].tolist()
for i,link in enumerate(links_list) :

    driver.get(link)
    time.sleep(4)
    # ingredients_container= driver.find_element(By.ID,"mntl-lrs-ingredients_1-0")
    recipe.append(driver.find_element(By.ID,"article-heading_1-0").text)
    ingredients.append(driver.find_element(By.ID,"mntl-structured-ingredients_1-0").text) 
    direction.append(driver.find_element(By.ID,"recipe__steps_1-0").text)

df = pd.DataFrame({'recipes': recipe, 'ingredients': ingredients, 'direction': direction})
df.to_excel("recipes_ingredients_sheet.xlsx", index=False)
