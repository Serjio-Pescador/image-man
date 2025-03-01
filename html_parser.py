import requests
from bs4 import BeautifulSoup
import ssl
import cloudscraper ,socket
from http import cookies
import json
from urllib.parse import urlparse
from urllib import parse



c = cookies.SimpleCookie()

s = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0'})

domain = 'https://okko.sport/'
routes = ['tournament/jupiler-pro-league-24-25', 'tournament/ligue-2-bkt-24-25', 'sport_collection/cybersport', 'sport_collection/5d658271-1736-3215-a420-0cc3e2b75a20']

# url = "tournament/jupiler-pro-league-24-25"
route = "tournament/isu-world-championships-2024"
# url = "https://okko.sport/tournament/ligue-2-bkt-24-25"
# url = "https://okko.sport/sport_collection/cybersport"

url = domain + route
print(url)

with open('okko.sport.json') as f:
    d = json.load(f)
    # print(d)

cookie = [d]

headers = {
    "accept": "text/css,*/*;q=0.1",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7",
    "if-modified-since": "Wed, 28 February 2025 22:14:37 GMT",
    "referer": "*.okko.sport",
    "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "style",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ]"
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "x-client-data": "CJC2yQEIorbJAQipncoBCOfaygEIlqHLAQiFoM0BCIunzQEIx6rNAQ==",
    "Origin": "*.okko.sport",
    # "cookie": {cookie}
}


r = s.get(url, headers=headers)
print(r.status_code)

bs = BeautifulSoup(r.text, 'lxml')
data = bs.select("picture", {"class": "NCBBdh36 rfa0EE5_"}.get('source'))
# print(data)

found_data1 = []
found_data2 = []

urlparse("scheme://netloc/path;parameters?query=fragment")
urls = []

for elem in data:
    el = str(elem).replace("amp;", '').split(' ')
    for i in el:
        if i.startswith("https://static.okko.tv"):
            o = url.split('?')[0].split('&')
            if i not in urls:
                urls.append(i)
                parsed = urlparse(i)
                captured_uuid = parsed.path.split('/')[3]
                found_data1.append(captured_uuid)
                found_data2.append(dict(parse.parse_qsl(parse.urlsplit(i).query)))

for i in range(len(found_data1)):
    print(found_data1[i], '=', found_data2[i])


list_uuid_used_preset = []
for j, element in enumerate(found_data2):
    for k, v in element.items():
        if k == 'presetId':
            list_uuid_used_preset.append((found_data1[j], element['presetId'], element['width']))

print(*list_uuid_used_preset, sep='\n')
print([*set([x[0] for x in list_uuid_used_preset])], sep=',\n')
