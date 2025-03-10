import requests
from bs4 import BeautifulSoup
import cloudscraper
from http import cookies
import ssl
import urllib3
from urllib3 import PoolManager
from urllib.parse import urlparse
from urllib import parse
from requests.adapters import HTTPAdapter
from urllib.request import urlopen

urllib3.disable_warnings()
c = cookies.SimpleCookie()

s = cloudscraper.create_scraper(delay=20, browser={'custom': 'ScraperBot/1.0'})


class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.TLSVersion.TLSv1_3
        )


# sess = requests.session()
# # sess.proxies.update({
# #     'https': 'http://10.77.152.192',
# # })
#
# sess.mount("https://", MyAdapter())

# host = ''
host = 'pre.'

domain = f"https://{host}okko.sport/"
# domain = 'https://{host}okko.tv/'
routes = ['tournament/jupiler-pro-league-24-25', 'tournament/ligue-2-bkt-24-25', 'sport_collection/cybersport',
          'sport_collection/5d658271-1736-3215-a420-0cc3e2b75a20']

# url = "tournament/jupiler-pro-league-24-25"
# route = "tournament/isu-world-championships-2024"
# route = "sport_collection/editoral-programms-mma"
route = "sport_collection/608ce1be-1c92-3436-af9e-89f221421034"
# route = "tournament/cs-2-perfect-world-shanghai-major-2024"

# url = "https://okko.sport/tournament/ligue-2-bkt-24-25"
# url = "https://okko.sport/sport_collection/cybersport"

session_param = "?clientSessionId=19558dbf-3a14-7aaa-2236-96f4cbf89cb6&sso=false"

url = domain + route #+ session_param
print(url)

# with open('okko.sport.json') as f:
#     d = json.load(f)
# print(d)

cookie = ("isCrawler=false; _sa=SA1.cbe2d1d3-6cb0-41f1-8b0d-b119090de73d.1740569789; _ym_uid=1740569790987129875; "
          "_ym_d=1740569790; tmr_lvid=85149b1cc2bc0ba163f2ef7f115c6f84; tmr_lvidTS=1740569789959; "
          "_ga=GA1.2.971080776.1740569820; _gcl_au=1.1.1467005930.1740644554; "
          "adtech_uid=b4f0040c-10a0-411e-b644-599a4d0c9067%3Aokko.sport; "
          "top100_id=t1.7272139.145041680.1740644554247; pre_noAuth=false; pre_tagHash=; "
          "odid=1954bb48-0877-7aaa-dde1-3364088d1b5e; old-odid=195420b3-a7cd-7aaa-a05a-7fbeda1f51de; "
          "accessKey=45f5ca5a-7770-450a-bcbc-164780bfe297; "
          "sessionToken=00.UUqUimYr54JMwXC2nB6nJ4IaKtR3fV_v8Lup0YxuBftffxEdJkyR-KUhcsWgf41B9pU5NGI8bVc05U"
          "-Zb3kraWIqszzscU4XCMJTfWYDtec; "
          "persistentToken=ZEG3gN_2JJ7L-nCiddL_24IaKtR3fV_v8Lup0YxuBfuxgKIABljdePNYWleTGgEYpxAk7mvcAF6KyEfOiizYNw; "
          "noAuth=false; t3_sid_7272139=s1.943056969.1740825505537.1740825723063.11.27; "
          "pre_accessKey=9735a672-bdcc-40b0-806c-5a86c2a6906b; "
          "pre_sessionToken=00.iAZ7usJIIboHjUwVHX709pHy2WZAxRfgeCrxOirD2DtAXbj_9bd9CU9Rl3-Vm4mcOGUba9T5hMFdTIndE"
          "-cTCRqA3tnCCKjE1GvUY5x9wTI; "
          "pre_persistentToken=IXOF9qIKgECCA8RSeQB-H0gwXsgmbpTPKNtGv6dyEECLchKqIVVQL1V0rFQJ2JztDueqPfglQ98JWNEupbdLWw"
          "; _sp_ses.075f=*; _ym_isad=2; _ym_visorc=w; domain_sid=ZDSni63x9g4zbFxyRbXnk%3A1740947886488; "
          "_gid=GA1.2.397125670.1740947915; _sp_id.075f=5615e190-299a-4549-8af6-59d6a4cf5184.1738240357.87.1740948089"
          ".1740841811.9bb0e139-2267-40fe-b52c-b12f2848ed85.0be396eb-b478-4f8e-8ca5-78e3194cfa10.68f712f3-99cc-450b"
          "-b47f-ebc4aa66c279.1740947885357.9; tmr_detect=0%7C1740948091112; "
          "_ga_WWJP846PEF=GS1.2.1740947915.18.0.1740948119.60.0.0")

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "if-modified-since": "Wed, 02 March 2025 22:14:37 GMT",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "*.okko.sport",
    "sec-ch-ua": "\"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/133.0.0.0 Safari/537.36",
    # "x-client-data": "CJC2yQEIorbJAQipncoBCOfaygEIlqHLAQiFoM0BCIunzQEIx6rNAQ==",
    "upgrade-insecure-requests": "1",
    "Origin": "*.okko.sport",
    # "Referrer Policy": "strict-origin-when-cross-origin",
    "cookie": "odid=19558ebe-948c-7aaa-69ee-30ea77227318"
}



# короткая реализаация без requests
# with urlopen(url) as response:
#     response_status = response.status  # сохраняем статус запроса в переменную
#     html = response.read()  # вычитываем ответ в переменную
#
# print(response_status == 200)  # проверяем успешен ли запрос
# print(html.decode())  # выводим полученный ответ на экран

r = requests.get(url, headers=headers, allow_redirects=True, verify=False, stream=True, timeout=5)
if r.history:
    print("Request was redirected")
    for resp in r.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(r.status_code, r.url)
else:
    print("Request was not redirected")


print(r.status_code)

bs = BeautifulSoup(r.text, 'lxml')
# print(bs)
data = bs.select("picture", {"class": "NCBBdh36 rfa0EE5_"}.get('source'))
print(data)

found_data1 = []
found_data2 = []

urlparse("scheme://netloc/path;parameters?query=fragment")
urls = []

if host:
    stat_url = "https://pre-static.okko.tv"
else:
    stat_url = "https://static.okko.tv"

for elem in data:
    el = str(elem).replace("amp;", '').split(' ')
    for i in el:
        if i.startswith(stat_url):
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
