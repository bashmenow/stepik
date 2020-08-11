import requests
import re
from urllib.parse import urlparse
URL = str(input())
pattern = r'<a.+href=[\'"]([^./][^\'"]*)[\'"]'
response = requests.get(URL).text
lst = re.findall(pattern, response)
pattern = '(\w[\w-]+)\.(\w[\w-]+)(\.\w\w+)?'
urls = []
def parse_link(link):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]

for link in lst:
    urls.append(parse_link(link))
#    if re.search(pattern, link):
#          urls.append(re.search(pattern, link).group())
urls = set(urls)
for url in sorted(list(urls)):
    print(url)

