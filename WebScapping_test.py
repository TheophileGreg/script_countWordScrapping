import requests
from collections import Counter


# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

from bs4 import BeautifulSoup

url = "https://viago.ca/top-10-des-meilleures-villes-d-europe-pour-faire-la-fete/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

huge_list = []  

for line in soup.text:
    huge_list = soup.text.split()


villes = ['Barcelone', 'Londres']


for ville in villes:
    print(ville) 
    print(huge_list.count(ville))
#word_counts = Counter(words in huge_list)

#print(word_counts)

#print(huge_list) 


