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
    huge_list = (soup.text.split())

# for h2 in soup.find_all('h2'):
#     huge_list.append(h2)

# for h1 in soup.find_all('h1'):
#     huge_list.append(h1)


# for h3 in soup.find_all('h3'):
#     huge_list.append(h3)

# for h4 in soup.find_all('h4'):
#     huge_list.append(h4)


# for h5 in soup.find_all('h5'):
#     huge_list.append(h5)




villes = ['Barcelone', 'Barcelone,' , 'Londres']

# print(huge_list)


for ville in villes:
    print(ville) 
    
    print(huge_list.count(ville))
#word_counts = Counter(words in huge_list)

#print(word_counts)

#print(huge_list) 


