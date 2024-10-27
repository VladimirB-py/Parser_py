import fake_useragent
import requests
from bs4 import BeautifulSoup

link = "https://httpbin.org/"

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
data = {
    'login':'123',
    'pass':'123',
    }

with requests.Session() as s:
    res=s.get(link, data=data, headers=header).text
    #print(f'res - {res}')
    soup = BeautifulSoup(res, 'lxml')
    block = soup.find('div', id='swagger-ui')
    #span_find = block.find('span')
    #print(f'soup - {soup}')
    print(f'blk - {block}')
