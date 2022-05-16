#scrape static page list of elements to csv - fake job site

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

for job_element in job_elements:

    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    e1 = title_element.text.strip()
    e2 = company_element.text.strip()
    e3 = location_element.text.strip()
    lst.append([e1, e2, e3])    

df1 = pd.DataFrame(lst, columns=cols)
#print(df1)
df1.to_csv('aa1aa.csv')

# task2 - add link as column
# task3 - try on other site, like il.indeed.com / https://www.drushim.co.il/
