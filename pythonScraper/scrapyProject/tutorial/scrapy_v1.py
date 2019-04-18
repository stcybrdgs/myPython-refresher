# scrapy_v1.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class QuotesSpider(scrapy.Spider):
    # identify the spider
    name = "quotes"

    # rem: 
    # spider can crawl a list of requests
    # starting from static list or generator function
    def start_requests(self):
        # use static list of urls for the spider to crawl
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


# main     =========================================
def main():
	print('Done.')

if __name__ == '__main__': main()