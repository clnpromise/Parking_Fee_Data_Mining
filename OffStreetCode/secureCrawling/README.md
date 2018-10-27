### Scrapy Crawling Secureparking Fee

1. run crawlURLs.py to get all URLs of each parking lot (change the URL if you want to crwal other cities)
2. install scrapy: pip install scrapy
3. run scrapy: scrapy crawl secureparking
Then the data will be stored in MySQL (change the database details in pipelines.py if you want to do some verification and should create table in MySQL first)
4. findSecureLocation.py: calling Google Place API to get the latitude and longitude of each parking lot and store the data in MySQL