import fake_useragent
import requests
from bs4 import BeautifulSoup

link = "https://httpbin.org/"

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

with requests.Session() as s:
    res=s.get(link, headers=header).text

    soup = BeautifulSoup(res, 'lxml')
    block = soup.find('span', id='//*[@id="swagger-ui"]/div/div[2]/div[3]/section/div/div[7]')
    #span_find = block.find('span')
    print(soup, block)
    #print(f'text - {h2_find}')
