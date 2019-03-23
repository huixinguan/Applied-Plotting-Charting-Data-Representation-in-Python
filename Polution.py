import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.numbeo.com/pollution/rankings_by_country.jsp'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')

countries = soup.find_all('td', attrs={'class' : 'cityOrCountryInIndicesTable'})
country=[]
for c in countries:
    country.append(c.text.strip())


indexes=soup.find_all('td', attrs={'style' : 'text-align: right'})
index=[]
for p in indexes:
    index.append(p.text.strip())
pollution_index = [float(index[i]) for i in range(len(index)) if i%2==0 ]
exp_pollution_index = [float(index[i]) for i in range(len(index)) if i%2!=0 ]

with open('pollutionIndex.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['country','pollution index','exp pollution index'])
    for a,b,c in zip(country, pollution_index, exp_pollution_index):
        writer.writerow([a,b,c])






