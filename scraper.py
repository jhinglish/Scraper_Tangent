from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from notifypy import Notify
import mechanicalsoup as ms
import time
import re


m = 0
url = f'https://utopiaclivias.co.za/products/category/mature_plants?page={m}'
base_link = 'https://utopiaclivias.co.za'
html = urlopen(url).read().decode("utf-8")
browser = (ms.Browser()).get(url)
name_pattern = r'<div class="field field--name-title field--type-string field--label-hidden field--item">.*?</div>'
price_pattern = r'<div class="product--variation-field--variation_price.*?</div>'
filename = 'clivia.txt'

def open_txt(filename):
    with open(filename, 'a+') as filehandle:
        old = [current_clivia.rstrip() for current_clivia in filehandle.readlines()]
    return old
old = open_txt(filename)
clivia = []
num_pages = int(((browser.soup.select('nav')[1]).select('a')[-1]['href']).replace('?page=', ''))

for m in range(num_pages + 1):
    count = len(re.findall('<article', html))
    n = 0
    while n < count:
        article_root = browser.soup.select('article')[n]
        article = article_root.decode(eventual_encoding = "utf-8")
        name_results = re.search(name_pattern, article)
        names = re.sub("<.*?>", "", name_results.group())
        price_results = re.search(price_pattern, article)
        prices = re.sub("<.*?>", "", price_results.group())
        link = base_link + (browser.soup.select('article')[n]).select('a')[-1]['href']
        out = [(names + ' : ' + prices + '; ' + link)]
        # print(out)
        clivia = clivia + out
        n += 1
    m += 1
    url = f'https://utopiaclivias.co.za/products/category/mature_plants?page={m}'
    html = urlopen(url).read().decode("utf-8")

def write_txt(filename):
    with open(filename, 'w') as filehandle:
        for listitem in clivia:
            filehandle.write('%s\n' % listitem)
write_txt(filename)

new_compare = [' '.join(x.split(' ')[:1]) for x in clivia]
old_compare = [' '.join(y.split(' ')[:1]) for y in old]
old_compare = ['MAT2132']

comparison = lambda a, b: list((set(a)- set(b))) + list((set(b)- set(a)))
new_clivia = comparison(old_compare, new_compare)
# new_clivia


# this is unnecessary... combine this into the one txt
# with open('new_clivia.txt', 'w') as filehandle:
#     for listitem in new_clivia:
#         filehandle.write('%s\n' % listitem)


# notifications system

notification = Notify()
notification.title = "New Clivias!"
notification.message = "New clivias are on sale."
notification.send()


# BONUS #
# tests

# cron job