from pyppeteer import launch


async def take_screenshot(url, path):
    browser = await launch(
        executablePath="c:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        headless=True,
    )

    clip = {
        'x': 0,
        'y': 250,
        'width': 670,
        'height': 400,
    }

    page=await  browser.newPage()
    await page.goto(url, {'timeout': 60000})  # Wait until the page is fully loaded
    #await page.waitForSelector('body > main > div:nth-child(1)')  # Replace with the selector you want to wait for
    await page.screenshot({
        "path": path,
        "clip": clip,
    })
    await browser.close()


async def screenshot_func(string):
    url_str = {
        'weather': 'https://www.gismeteo.ru/weather-rostov-na-donu-5110/10-days/',
        'rubus': 'https://yandex.ru/search/?text=%D0%BF%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D1%80%D1%83%D0%B1%D0%BB%D1%8C&lr=39&clid=2233626&src=suggest_B',
        'news': 'https://dzen.ru/',
    }

    await take_screenshot(url=url_str[string], path=f"{string}.png")