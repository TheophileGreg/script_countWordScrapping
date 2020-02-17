import requests
from collections import Counter


# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

from bs4 import BeautifulSoup

url = "https://viago.ca/top-10-des-meilleures-villes-d-europe-pour-faire-la-fete/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

word_counts = Counter(word for words in soup.text for word in words)

print(word_counts)


print(soup.word)

