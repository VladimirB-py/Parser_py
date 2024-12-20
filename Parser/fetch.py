import requests

def fetch(url, params):
  headers=params['headers']
  body=params['body']
  method=params['method']
  if method=="POST":
    return requests.post(url, headers=headers, data=body)
  elif method=="GET":
    return requests.get(url, headers=headers)

lada=fetch("https://auto.ru/-/ajax/desktop-search/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "279.0.15513387",
    "x-client-date": "1734348237106",
    "x-csrf-token": "d42144d8f5cb41615211dea13a5b2cdaee3ce68be9d3c65f",
    "x-page-request-id": "89029999751d9f586aa19dc1fa0ec2ff",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/rostov-na-donu/cars/chery/amulet/used/",
    "x-yafp": "{\"a1\":\"8Pohaj1vziN/eA==;0\",\"a2\":\"SUPF+dYb1yqxhF8VRureV1MF0F4DeA==;1\",\"a3\":\"hDLCoyZYtaeNOWfxSsp3Aw==;2\",\"a4\":\"4VV1HtGyGrKns7WHoJB6BF1HXDEev6g3p8+XZRGOXR5ufw==;3\",\"a5\":\"BlYesPqYeVWH+Q==;4\",\"a6\":\"t84=;5\",\"a7\":\"hqbzAoodc4WF1A==;6\",\"a8\":\"xcLW1LmGAKQ=;7\",\"a9\":\"Tu6+EQn2U2YY2g==;8\",\"b1\":\"A1/Wof2puA4=;9\",\"b2\":\"YGe01fuRS+tuoA==;10\",\"b3\":\"41YNEp7WcbROHg==;11\",\"b4\":\"LnmoUac4Obk=;12\",\"b5\":\"7iw+AsUa9KTF0w==;13\",\"b6\":\"OQPKMfEXylSh3w==;14\",\"b7\":\"uh/H0xQk1qBOFQ==;15\",\"b8\":\"IP2PDQV8HcunMQ==;16\",\"b9\":\"F7eSZauPw0BqxQ==;17\",\"c1\":\"LJAEwg==;18\",\"c2\":\"UzsMmwiXKbWj1jxSzlgIvQ==;19\",\"c3\":\"dXyuJ9Tkz1k2a86aLg/axw==;20\",\"c4\":\"FXmZcbw062A=;21\",\"c5\":\"T+WzBdPECE0=;22\",\"c6\":\"zySEBg==;23\",\"c7\":\"KdL313E47pQ=;24\",\"c8\":\"y6M=;25\",\"c9\":\"2uaqHhONDRw=;26\",\"d1\":\"4Gugp682CCo=;27\",\"d2\":\"WSA=;28\",\"d3\":\"xKyFz2m/X07tlQ==;29\",\"d4\":\"uIJ8n8MLvPc=;30\",\"d5\":\"DdL9z727hI26IQ==;31\",\"d7\":\"b322yfODHBc=;32\",\"d8\":\"VjzxifJF3WzwXTeFk72BRRgAyMHPf+OpBUA=;33\",\"d9\":\"RXiKxrDtCKU=;34\",\"e1\":\"b+VaC9mDyYHj6Q==;35\",\"e2\":\"Etj2sKn+3r0=;36\",\"e3\":\"XpnPnFYxQOM=;37\",\"e4\":\"3g5vRtbK3Zg=;38\",\"e5\":\"EPqT1zZ4bz7PbA==;39\",\"e6\":\"HalUAe/6q8A=;40\",\"e7\":\"c1GR8weVwk6hYw==;41\",\"e8\":\"K3IbkW7sPtk=;42\",\"e9\":\"+bcORpyNnkk=;43\",\"f1\":\"RI/H73hpizZpzg==;44\",\"f2\":\"8cEchtsYAz4=;45\",\"f3\":\"iR4EVJNmzynekA==;46\",\"f4\":\"ZGrU8LAuDnI=;47\",\"f5\":\"K3NTzYw7KcFEfg==;48\",\"f6\":\"XvYeY1wp7GlIyg==;49\",\"f7\":\"5+iFSpr7EJQ35g==;50\",\"f8\":\"Fervn8B2iEnEOQ==;51\",\"f9\":\"2kmbvu1JUGk=;52\",\"g1\":\"KpBN9M9xNe5q6A==;53\",\"g2\":\"trXccfP0SqbU3w==;54\",\"g3\":\"dPqDSuwROlM=;55\",\"g4\":\"DdOLVUQ0m5s8pw==;56\",\"g5\":\"fHu7/gSN60Q=;57\",\"g6\":\"ee62k7OzI18=;58\",\"g7\":\"jacgRFLmG/s=;59\",\"g8\":\"EHJydquEZPQ=;60\",\"g9\":\"DgLBCpOX0e0=;61\",\"h1\":\"bJaBYIUBxwXARw==;62\",\"h2\":\"a346DVHj4RRyBw==;63\",\"h3\":\"gceI2L/sV7TIfw==;64\",\"h4\":\"1sHEryvMw4p+tw==;65\",\"h5\":\"UKNNAVo1hpU=;66\",\"h6\":\"35IsCuWCkWwgbw==;67\",\"h7\":\"A+/4T74EGNe6XD+iPcU123taz+0eJeU1d+L+IfVx6Cvn+UM2;68\",\"h8\":\"qPtUljJN1civKA==;69\",\"h9\":\"vVkJoetKBz9mtw==;70\",\"i1\":\"50ISvNArzys=;71\",\"i2\":\"3JrAm23M28xYLA==;72\",\"i3\":\"LsEn+KQ+yD8H2Q==;73\",\"i4\":\"/O7GmWy26+a5nA==;74\",\"i5\":\"AnBeuHQKxCT0Wg==;75\",\"z1\":\"WvKxJjklJaJvpdw7PqfSmVGjkH02cSosJ1gUSK+xyYpPH3+kyHLqSzP+RQrZQXnmEFhzhRly6+yLuOxC7EIseQ==;76\",\"z2\":\"XPuNqbF2hrn2I52YvVEOKfuDMR1fKVvuyH1LekI4hAZPGJIpCNnp5PpLcEPW2cI+tcFK+hlkIFOzVEC7ANAFxA==;77\",\"y2\":\"7BWuNjGKYfHQRg==;78\",\"y3\":\"dVtj6Xt5IAKjNQ==;79\",\"y6\":\"iiJwe1E6ypztJA==;80\",\"y8\":\"IREQHiQlldzlgQ==;81\",\"x4\":\"cgHT88ppN47o6w==;82\",\"z4\":\"4d7ZdB6/co+RyA==;83\",\"z5\":\"f47s9XT6mZ4=;84\",\"z6\":\"IXiE2sinpJB9FGdg;85\",\"z7\":\"bpAZcICrZMV6/iPF;86\",\"z8\":\"aw9z9q4127dPt4o4;87\",\"z9\":\"eMWvkF6oonCHIB7X;88\",\"y1\":\"qi3AQT5K3MmiadbQ;89\",\"y4\":\"rM3MjtndmKeOxZCr;90\",\"y5\":\"bCO56uq9nSmjR8d4jsY=;91\",\"y7\":\"u+fJLetXXMdlXM8Z;92\",\"y9\":\"nMJclwQuAJ69vjbQbGA=;93\",\"y10\":\"K9qD5whBxUWPVq7JPgQ=;94\",\"x1\":\"O8z+xEd2bCfR8FLM;95\",\"x2\":\"93d9Zk7TsHFu7pAmKiM=;96\",\"x3\":\"sKsfRj8x1gJmfs1K;97\",\"x5\":\"QejxZvu6qds2hFox;98\",\"z3\":\"aTewAt3H51fLRMjgoyc=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"NEERBtjAm8J41VZ76E8AEDe++a0=;100\",\"pgrd\":\"sIPZ6KL00w92lciahEghw/OySHXD96JJQDTpbnjXkslrAt1Bxxp99U0sH2idnInSSNH6no/ad8B10EAepIfN2YmkIKGdNefKmcVimdvOsE8DDMceAgsnm5Jy/9BGalxyfLoE/GmauUWSZ9wtsl7N3GOaL5jxBK8y0RXPyoKz0Dp8esPoIUyCT/U1YTfD41QEQYMT+P+Av6/Gy3kl6SvEZscfuGk=\"}",
    "cookie": "suid=4d92c3d2815be2fb790f0f8f9e342916.ca46fbb06983b5d9b71f4db952f67876; autoru_sid=a%3Ag675e704826mk3dmn5uiqe4l7khc11e4.f8ee4106512015729f2a332f29239324%7C1734242376802.604800.s1XUUE7BblAiy3ducmFU2w.EcnSvH4h7po2fnTXS8c68jDVpilevntB3lU_T3o4_IE; autoruuid=g675e704826mk3dmn5uiqe4l7khc11e4.f8ee4106512015729f2a332f29239324; yandex_login=; i=ZpS7G9/ykVjF0oIs/08Ly/XQy2V52bdObQKOXP0lQ0g91PRibMvHz5LwiNoBZxfbmHJ76VXsLLAwSlUU1d/zoJqCPn0=; yandexuid=5561055731734242377; crookie=x3uzOVm5e2fAj4pQhRYbw3UsNMsuND7aa70QGtFe5RV+0PYnFl+20R9Uj6HYxZLE3GDpTC0tf0jBhj8Fuhoi1i5FTq4=; cmtchd=MTczNDI0MjM3NDAwMA==; _ym_uid=1734242388174691123; autoru-visits-count=2; _ym_isad=2; fp=079e3c6fc7c9b7a67ac35ccbd0788dd9%7C1734338344901; yaPassportTryAutologin=1; _csrf_token=d42144d8f5cb41615211dea13a5b2cdaee3ce68be9d3c65f; from=direct; gids=39; gradius=100; layout-config={\"screen_height\":768,\"screen_width\":1366,\"win_width\":563,\"win_height\":641}; gdpr=0; _ym_visorc=b; spravka=dD0xNzM0MzQ2NDQ3O2k9NDYuMTQ3LjIyMi41MDtEPTEwQkQ1OTk0OTlFMkJEMDhBMzBFNzA1QjhDNDVFNkQ4MURFNkZDRjJDQjcxQkU1QjM2RTIxQTVGM0ZCMkVBNTQ5RkZCQzgwRkZBNjAzNDhEODkyNTg2NDc3Q0U4QjlCM0ZCODU5NEQxMzQ1QTgxOTYwMzRDMDYzNzAzOTBBRDRERUMxRkYxRTY1NTgzQ0I5NTt1PTE3MzQzNDY0NDc0NjE1Mzg5NzA7aD01ZjY1YmJkNDUxODg0OTgwNTQ3Zjc0ZGI0ZGMxYTBmZQ==; autoru_sso_blocked=1; Session_id=noauth:1734346447; sessar=1.1197.CiCbuVLJlr0G-UDotTYwW-adG1LmXVwzayGpbdRjUsTsJg.APXzR9wuLQvUHiZUs2Fgpoume673lCI8bx83jCml6uo; ys=c_chck.3524456845; mda2_beacon=1734346447717; sso_status=sso.passport.yandex.ru:synchronized; autoru_sso_redirect_blocked=1; _yasc=LxUNoq94Kl2xf/2CPGXNDpseBgrBjsfQ7oadH3bZsUJ8gqEVrZDC1itk+3HyAae+zR8KPAWu0A==; cycada=TgC29ru5+/ms78zrZnT890dY0vP8GU2bWfdZzatojTU=; _ym_d=1734348187; count-visits=20; from_lifetime=1734348243888",
    "Referer": "https://auto.ru/rostov-na-donu/cars/chery/amulet/used/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"CHERY\",\"model\":\"AMULET\"}],\"section\":\"used\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_radius\":100,\"geo_id\":[39]}",
  "method": "POST"
})

offer=lada.json()["offers"]
print(offer)
for element in offer:
  print(element["price_info"]['RUR'])