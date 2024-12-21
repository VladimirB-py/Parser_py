import requests

def fetch(url, params):
    headers = params['headers']
    body = params['body']
    method = params['method']
    if method == "POST":
        return requests.post(url, headers=headers, data=body)
    elif method == "GET":
        return requests.get(url, headers=headers)


dollar = fetch("https://siteapi.vtb.ru/api/currencyrates/convert", {
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/91.0.4472.124"
                      " Safari/537.36",
        "content-type": "application/json"
    },
    "body": "{\"categoryId\":1,\"categoryTypeId\":1,\"currencyFrom\":\"USD\",\"currencyTo\":\"RUB\""
            ",\"fromSumma\":1,\"toSumma\":0}",
    "method": "POST",
})

news = fetch("https://dzen.ru/news/rubric/chronologic?ajax=1&neo_parent_id=1734712586939226-5320455843965885028-2."
      "news-dzen-pginx.l7-news.pc.idzn.ru-BAL-9376-NEWS-NEWS_RUBRIC", {
  "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "content-type": "application/json",
        "cookie": ("news_lang=ru; nc=opertopTooltipWasShown=true; zencookie=9410766211726569713; "
                   "yandex_login=; yandexuid=1769214361726569712; _ym_uid=1726569695860891355; _ym_d=1726569695; "
                   "zen_gid=39; zen_vk_gid=5557; rec-tech=true; tmr_lvid=554a7fba4b5c35b4aba5924693318f56; "
                   "tmr_lvidTS=1726569696723; vid=b67e255801f9de54; stable_city=2; news-fullscreen-current-position=1; "
                   "is-news-fullscreen-waterfall-ended=false; has_stable_city=true; zen_ms_socdem_pixels=3212788; "
                   "is_auth_through_phone=true; news-fullscreen-showings-period-start-date=2024-12-19T05:50:51.190Z;"
                   " zen_sso_checked=1; Session_id=noauth:1734678935; "
                   "sessar=1.1197.CiDqLSSlM2ZEvuvZ0ucRYgbvVGVyJ14moV5ft36jpHSoKg.eoQQ5t6V77j9x3ExfirN9wyvYbowIdEKqc"
                   "dUpiol-U0; ys=c_chck.941036529; mda2_beacon=1734678935778; zen_vk_sso_checked=1; _ym_isad=2; "
                   "story-last-date-count=2024-12-20T07:17:34.304Z; _yasc=Zo/ZRon0SvonwIzFcsAFAGHWEjl7uiqrLU5oOoMcmhI7r"
                   "jp8yRGJ+cE6DbMWX0sXHzs=; front_fpid=uh5Cm2cJBfF1CLMA-_y1r; one_day_socdem=+; is_online_cached=false;"
                   " tmr_detect=0%7C1734712409564; skip_dzen_pro=true; domain_sid=uh5Cm2cJBfF1CLMA-_y1r%3A1734712583478;"
                   " Zen-User-Data={%22zen-theme%22:%22light%22}; is_online_stat=false"),

},
  "body": None,
  "method": "GET"
})
news_list=[]
for el in news.json()['data']['stories']:
    news_list.append(el['title']+" ---> "+el['source'])
    news_list.append(el['url'])
