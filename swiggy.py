import pandas as pd
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.swiggy.com/restaurants/v-grand-family-restaurant-janardhan-nagar-guntur-road-ongole-491857")
print(response)

soup = BeautifulSoup(response.content,'html.parser')

names = soup.find_all('div',class_="OEfxz")
name = []
for i in names:
    n =i.get_text()
    name.append(n)
print(name)