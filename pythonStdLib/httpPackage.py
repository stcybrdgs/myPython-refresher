# python HTTP package
# http, urlib, json, textwrap
#
# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
#
# rem use google books api--> give it an isbn number and let api return data on the book

import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
	text = f.read() # read everything returned by the request
	decodedtext = text.decode('utf-8') # decode so you can print to user
	print(textwrap.fill(decodedtext, width=50))

# once you have the json object returned, you can use the json module to pull out the
# specific data you want

print()

obj = json.loads(decodedtext) # load json data into json object
print(obj['kind'])

print(obj['items'][0]['searchInfo']['textSnippet'])
print(obj['items'][0]['accessInfo']['webReaderLink'])