from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)
print(page.text)
soup = BeautifulSoup(page.text,"html.parser")
star_table=soup.find_all("table")
temp_list=[]
table_rows=star_table[7].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    print(row)
names=[]
distance=[]
mass=[]
radius=[]
for i in range (1,len(temp_list)):
    names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
df=pd.DataFrame(list(zip(names,distance,mass,radius)),columns=["name","distance","mass","radius"])
df.to_csv("star.csv")
