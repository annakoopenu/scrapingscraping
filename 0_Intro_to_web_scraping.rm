#https://realpython.com/python-web-scraping-practical-introduction/

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# STEP1 - scrape 
url = "https://en.wikipedia.org/wiki/Federico_Fellini"
page = urlopen(url)
print("STEP1 - scrape")
print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

# STEP2 - extract with regular expression 
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags
print("STEP2 - extract with regular expression")
print(title)

# STEP3 - extract with HTML Parser for Web Scrapping  
soup = BeautifulSoup(html, "html.parser")
print("STEP3 - extract with HTML Parser")
title_s = soup.title
print(title_s.string)
