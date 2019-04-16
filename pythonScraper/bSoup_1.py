# bSoup_1.py
# testing a python/beautifulSoup screen scraper

from bs4 import BeautifulSoup
import urllib
import urllib.request
import re # regular expression library

# point to html markup doc
htmlDoc = open('DSFD_Listing.html', 'rt')

# make a BeautifulSoup object, and then let it turn the 
# html markup from htmldoc into a parse tree
soup = BeautifulSoup(htmlDoc, 'html.parser')
htmlDoc.close()

# print some stuff from the markup
print(soup.prettify()[0:200])
print('\n\n')
print(soup.p.attrs)
print(soup.body.p)

# point to web page
myPage = 'https://analytics.usa.gov'

# make a BeautifulSoup object, and then let it turn the
# html from the page into a parse tree
p = urllib.request.urlopen(myPage)
# urllib.request.urlopen('https://analytics.usa.gov').read()
soup = BeautifulSoup(p, 'html.parser')

# print some stuff from the url
print('\n\n')
print(soup.prettify()[0:200])



