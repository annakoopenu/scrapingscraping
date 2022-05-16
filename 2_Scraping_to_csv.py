#scrape static page list of elements to csv - real site https://il.indeed.com/

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://il.indeed.com/jobs?q=excel'
page = requests.get(URL)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_ = "jobsearch-ResultsList")

job_elements = results.find_all("li")

l = len(job_elements)

result = []
cols = ['title', 'company', 'location']
lst = []

for job in job_elements:
    job_title = job.find(class_ = 'jcs-JobTitle')
    job_location = job.find(class_ = 'companyLocation')
    job_companyName = job.find(class_ = 'companyName')

    print('--------' + str(l) + '---------------')
    l -= 1

    if job_title is None:
        e1 = '-'
    else:
        e1 = job_title.text.strip()

    if job_companyName is None:
        e2 = '-'
    else:
        e2 = job_companyName.text.strip()    

    if job_location is None:
        e3 = '-'
    else:
        e3 = job_location.text.strip()
  
    lst.append([e1, e2, e3])    
    
print(len(job_elements))

df1 = pd.DataFrame(lst, columns=cols)
print(df1)
df1.to_csv('aa2aa.csv')

# task1 - find errors (why empty data)
# task2 - how to go to the next page
