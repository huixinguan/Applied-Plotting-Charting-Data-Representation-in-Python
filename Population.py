import requests
from bs4 import BeautifulSoup
import ast
import csv

url = 'http://www.worldometers.info/world-population/population-by-country/'

page=requests.get(url).text

soup=BeautifulSoup(page,'html.parser')

# table = soup.find('tbody')

countries=soup.find_all('a')
countries_list=[]
for c in countries:
    countries_list.append(c.text.strip())
country=countries_list[8:-14]

populations=soup.find_all('td', attrs={'style':'font-weight: bold;'})
population = []
for p in populations:
    population.append(p.text.strip())

    # population.append(float(p.text.strip().split(',')))
# print(table)
# print(country)
# pop=[]
# j=[]
# z=0
# for s in population:
#     z="".join(s.split(","))
#     pop.append(int(z))
pop=[int("".join(s.split(","))) for s in population]

with open("population.csv",'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['country','population'])
    for a,b in zip(country,pop):
        writer.writerow([a,b])