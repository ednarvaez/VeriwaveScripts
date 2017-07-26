from bs4 import BeautifulSoup
import requests

url = ('https://ctlabs.verizon.net/vztracking/browse/FQG-2808')

print ()
print (url)

r = requests.get (url)

data = r.text

soup = BeautifulSoup (data, "lxml")

print (soup)
