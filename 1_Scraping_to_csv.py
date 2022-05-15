#scrape static page list of elements to csv

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

cols = ['title', 'company', 'location']
lst = []

i = 1
for job_element in job_elements:

    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    print('Element number ' + str(i))
    e1 = title_element.text.strip()
    e2 = company_element.text.strip()
    e3 = location_element.text.strip()
    lst.append([e1, e2, e3])    
    i += 1

print('da da datastrata')

df1 = pd.DataFrame(lst, columns=cols)
print(df1)
df1.to_csv('aa1aa.csv')
