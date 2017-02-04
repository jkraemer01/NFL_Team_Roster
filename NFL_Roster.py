from bs4 import BeautifulSoup
import requests
import pandas as pd
base = requests.get("http://m.espn.com/nfl/teamroster?teamId=1")
soup=BeautifulSoup(base.content,'html.parser')
column=soup.find(id="left-column")
name= [row.get_text() for row in column.find_all("a")]
head=[x.get_text() for x in column.find_all("th")]
pos=[y.get_text() for y in column.find_all("td")[2::3]]
numb=[z.get_text() for z in column.find_all("td")[0::3]]
table=pd.DataFrame({
    head[0]:numb,
    head[1]: name,
    head[2]:pos
})
print(table.to_string(index=False))