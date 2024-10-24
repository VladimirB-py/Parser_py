import fake_useragent
import requests
from bs4 import BeautifulSoup

user=fake_useragent.UserAgent().random
header={'user-agent': user}
link = "https://3.python-requests.org/user/quickstart/"

res = requests.get(link, headers=header).text
soup=BeautifulSoup(res, 'lxml')
block=soup.find('div', id='binary-response-content')
h2_find=block.find('h2')
#print(block)
print(f'text - {h2_find}')