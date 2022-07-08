import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/search?q=real%20me%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)
soup = BeautifulSoup(response.content,'html.parser')

                                                                                         
names = soup.find_all('div',class_='_4rR01T')
name = []
for i in names:
    t=i.get_text()
    name.append(t)


prices = soup.find_all('div',class_="_30jeq3 _1_WHN1")
rates=[]
for i in prices:
    s = i.get_text()
    rates.append(s)



images= soup.find_all('img',class_='_396cs4 _3exPp9')
image=[]
for i in images:
    m = i['src']
    image.append(m)


links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in links:
    l="https://www.flipkart.com"+i['href']
    link.append(l)


df=pd.DataFrame()
df['Name'] = name
df['Price'] = rates
df['Images'] = image
df['Links'] = link
print(df)
df.to_csv("mobiles.csv")
