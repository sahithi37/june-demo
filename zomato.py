
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
print(response)
#soup = BeautifulSoup(response.content,"html.parser")
#print(soup)

Name = soup.find_all("td",class_="titleColumn")
title = []
for i in Name:
    t = i.get_text()
    t=t.replace("\n","")
    t=t.replace("     ","")
    title.append(t)
#print(title)
s=len(title)
print(s)

rating = soup.find_all("td",class_="ratingColumn imdbRating")
ratings = []
for i in rating:
    r= i.get_text()
    r= r.replace("\n","")
    ratings.append(r)
#print(ratings)

poster = soup.find_all("img")
posters = []
for i in poster:
    p = i['src']
    posters.append(p)
#print(posters)

# link = soup.find_all("a",href = re.compile("^/title/tt00"))
# link_1 = soup.find_all("a",href = re.compile("^/title/tt01"))
# link_2 = soup.find_all("a",href = re.compile("^/title/tt8"))
# links = []
# for i in link:
#     l = "https://www.imdb.com/"+str(i.get('href'))
#     links.append(l)
# for i in link_1:
#     n="https://www.imdb.com/"+str(i.get('href'))
#     links.append(n)
# for i in link_2:
#     q="https://www.imdb.com/"+str(i.get('href'))
#     links.append(q)
# #print(links)

df = pd.DataFrame()
df['Title'] = title
df['Rating'] = ratings
df['Poster'] = posters
for i in range(10):
    print(df)


