# imports 
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import mechanicalsoup as ms
import time
import re

# access website
url = 'https://utopiaclivias.co.za/products/category/mature_plants?page=1'
# page = urlopen(url)
html = urlopen(url).read().decode("utf-8")
# print(html)


# read specific information
# name/price/url

name_pattern = r'<div class="field field--name-title field--type-string field--label-hidden field--item">.*?</div>'
price_pattern = r'<div class="product--variation-field--variation_price.*?</div>'

browser = ms.Browser()
x = (browser.get(url).soup.select('article')[1]).decode(eventual_encoding = "utf-8")
print(x)
y = re.search(price_pattern, x)
print(y)
y_sub = re.sub("<.*?>", "", y.group())
print(y_sub)
z = urlopen(url)
# links = [a['href'] for a in re.findall('a', x)]
link_text = ''
for link in re.findall('a', x):
    link_text = link['href']
    print(link_text)


count = len(re.findall('<article', html))
n = 0
while n < count:
    article = (browser.get(url).soup.select('article')[n]).decode(eventual_encoding = "utf-8")
    name_results = re.search(name_pattern, article)
    names = re.sub("<.*?>", "", name_results.group())
    price_results = re.search(price_pattern, article)
    prices = re.sub("<.*?>", "", price_results.group())
    print(names + ' : ' + prices)
    n += 1
    

# create/update list and save to file system
# print out new plants


# BONUS #
# tests

# cron job

# notifcations system