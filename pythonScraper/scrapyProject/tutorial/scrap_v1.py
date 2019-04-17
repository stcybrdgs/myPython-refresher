# scrapy_v1.py
# getting started with a scrapy web scraper


# imports  =========================================
import scrapy

# classes  =========================================
class QuotesSpider():
	name = "quotes"

	def start_requests(self):
		urls = [
		    'http://quotes.toscrape.com/page/1/',
		    'http://quotes.toscrape.com/page/1/'
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