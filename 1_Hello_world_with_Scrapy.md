# scraping a web page - Note 1 : Hello world with Scrapy

run at the terminal 

1. to install run : - pip install Scrapy
    
2. to check installation run :     scrapy --help
    
3. to start scarping project run : scrapy startproject <project name>
                                   scrapy startproject ietf_scraper

    THIS WILL CREATE A TEMPLATE with files
        - scrapy.CFG holds configuration information
        - items.py defines the objects or the entities that we're scraping
        - etc
        - the !! spider DIRECTORY 
        - 

4.navigate to ietf spiders directory to set spider  :   cd ietf_scraper/ietf_scraper/spiders
                                                        cd ietf_scraper/ietf_scraper/spiders

5.to create spider run  :   crapy genspider ietf pythonscraping.com
    
     THIS WILL CREATE A TEMPLATE a spider --> ietf.py

6.overview the spider file  :   go to ietf.py 
    
7.inside <spider-file>
    
    7.1 modify the start URL
        inside spiders/ietf.py/ 
        change
        start_urls = ['http://pythonscraping.com/']
        to 
        start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    7.2 inside spiders/ietf.py/parsel() function add
        title = response.css('span.title::text').get()
        or
        title = response.xpath('//span[@class="title"]/text()').get()    
    

    7.3 inside spiders/ietf.py/parsel() function delete pass and add
        return {"title": title}
        or in one line 
        return {'title': response.xpath('//span[@class="title"]/text()').get()}

8. run spider to see the results    :   scrapy runspider ietf.py    

from
    https://www.linkedin.com/learning/web-scraping-with-python/hello-world-with-scrapy?autoSkip=true&autoplay=true&resume=false
https://github.com/LinkedInLearning/web-scraping-with-python-2848331
    
