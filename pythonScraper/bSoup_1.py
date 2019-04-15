# bSoup_1.py
# testing a python/beautifulSoup screen scraper

from bs4 import BeautifulSoup

'''
result = requests.get('https://wrangleworks.com')
page = result.text
print(page)
driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/')
page = driver.page_source
'''
# htmldoc = ('DSFD_Listing.html')

html_doc = open('DSFD_Listing.html', 'rt')
# make a BeautifulSoup object, and let it turn the 
# html markup from htmldoc into a parse tree
soup = BeautifulSoup(html_doc, 'html.parser')
print(html_doc, 'HELLO', '\n\n', soup)
html_doc.close()



