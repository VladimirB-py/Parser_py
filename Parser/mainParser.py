import asyncio

import requests
#import teleg_bot


headers = {
    "accept": "*/* accept-encoding:gzip, deflate, br, zstdaccept-language:ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 \
    Safari/537.36 Edg/130.0.0.0"
}

def get_page(url):
    s=requests.Session()
    responses=s.post(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(responses.text)
        print(file)


#https://www.ozon.ru/category/nasosy-dlya-gsm-30312/?sorting=price
def mainParse():
    get_page(url="https://salomonrussia.ru/product-category/obuv/?orderby=price&filter_tselevaya-gruppa=men-unisex")


if __name__ == "__main__":
    mainParse()
    #teleg_bot.asyncio.run(teleg_bot.main())
