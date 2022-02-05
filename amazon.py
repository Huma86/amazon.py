from email import header
from encodings import utf_8
from itertools import product
from math import prod
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.ae/s?k=galaxy+ultra&rh=n%3A15415001031&ref=nb_sb_noss'

headers = {'user-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36' }

page = requests.get(url, headers=headers)

bs = BeautifulSoup(page.content, 'html.parser')

#print(bs.prettify().encode("utf-8"))

product_title = bs.find(id = "producttitle")

print(product_title)
