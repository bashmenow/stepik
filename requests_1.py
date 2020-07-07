import requests
import re
url1 = str(input())
url2 = str(input())
tmp_url = []
pattern = r'(https://.+)"'
res = False
def getter(url):
    response = requests.get(url)
    return re.findall(pattern, response.text)
urls = getter(url1)
for url in urls:
    tmp_url.extend(getter(url))
for url in tmp_url:
    if url == url2:
        print('Yes')
        res = True
        break
if not res:
    print('No')
