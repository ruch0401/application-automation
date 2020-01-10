import requests
import html5lib
import bs4
from bs4 import BeautifulSoup

URL = "https://www.passiton.com/inspirational-quotes"
r = requests.get(URL, verify = False)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())

quotes = []
table = soup.find('div', attr = {'class':'container'})
print(table.prettify())

"""
for row in table.find_all('div', attrs = {'class':'product_price'}): 
	quote = {}
	quote['price'] = row.p.text
	quote['name'] = row.h3.title
	quotes.append(quote)
	print(quotes)
"""