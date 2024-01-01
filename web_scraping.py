import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.bbc.com/'

#Pass url to fetch html content
r=requests.get(url)
htmlcontent=r.content

#Parse the html
soup=BeautifulSoup(htmlcontent,'html.parser')

#HTML Tree traversal
contents=soup.find_all('a',class_='media__link')

links_list=[]
category_list=[]
title_list=[]
for i in contents:
    links_list.append(i.get('href'))
    category_list.append(i.get('rev'))
    title_list.append(i.get_text().strip())


data={'Title':title,'Link':links,'Category':category}
df=pd.DataFrame(data)
df.to_csv('bbc_news_scraping.csv')

