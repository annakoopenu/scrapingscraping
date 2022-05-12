# scrapingscraping

test script for scraper

1.run at the terminal to install 
    pip install Scrapy
2.run at the terminal to check installation 
    scrapy --help
3.run at the terminal to start scarping project 
    scrapy startproject ietf_scraper

    THIS WILL CREATE A TEMPLATE with files
        - scrapy.CFG holds configuration information
        - items.py defines the objects or the entities that we're scraping
        - etc
        - the !! spider DIRECTORY 
        - 

4.navigate to ietf spiders directory to set spider 
    cd ietf_scraper/ietf_scraper/spiders
    

5.create a spider --> ietf.py
        scrapy genspider ietf pythonscraping.com

6.go to ietf.py overview the template
    FIRST THING TO DO: modify the start URL
    inside spiders/ietf.py/ 
    change
    start_urls = ['http://pythonscraping.com/']
    to 
    start_urls = ['http://pythonscraping.com/about']?

7.inside spiders/ietf.py/parsel() function
    title = response.css('span.title::text').get()
    or
    title = response.xpath('//span[@class="title"]/text()').get()    
    pass

7.inside spiders/ietf.py/parsel() function delete pass and add
    return {"title": title}

    or in one line 
        return {'title': response.xpath('//span[@class="title"]/text()').get()}

8. run spider to see the results 
    scrapy runspider ietf.py    
