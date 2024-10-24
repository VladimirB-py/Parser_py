import requests
from bs4 import BeautifulSoup

link = "https://3.python-requests.org/user/quickstart/"

res = requests.get(link).text
soup=BeautifulSoup(res, 'lxml')
block=soup.find('div', id='binary-response-content')
h2_find=block.find('h2')
#print(block)
print(f'text - {h2_find}')