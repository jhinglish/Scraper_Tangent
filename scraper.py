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

name_pattern = r'<div class="field field--name-title field--type-string field--label-hidden field--item">.*?</div>'
price_pattern = r'<div class="product--variation-field--variation_price__670 field field--name-price field--type-commerce-price field--label-hidden field--item">.*?</div>'

browser = ms.Browser()
x = (browser.get(url).soup.select('article')[1]).decode(eventual_encoding = "utf-8")
print(x)
y = re.search(name_pattern, x)
print(y)
y_sub = re.sub("<.*?>", "", y.group())
y_sub

n = 0
while n < 11:
    article = (browser.get(url).soup.select('article')[n]).decode(eventual_encoding = "utf-8")
    results = re.search(name_pattern, article)
    clivia = re.sub("<.*?>", "", results.group())
    print(clivia)
    n += 1
    

match_results = re.search(name_pattern, html)
name = re.sub("<.*?>", "", match_results.group())
print(name)


# read specific information
# name/price/url


# create/update list and save to file system
# print out new plants


# BONUS #
# tests

# cron job

# notifcations system