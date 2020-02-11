import requests, re
from bs4 import BeautifulSoup

url = 'http://www.google.com/search'
query = raw_input('Enter your search parameter: ')
payload = { 'q' : query }

my_headers = { 'User-agent' : 'Mozilla/11.0' }
r = requests.get( url, params = payload, headers = my_headers )

print(r.text.count('toto'))
