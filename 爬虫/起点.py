import requests
from bs4 import BeautifulSoup
import urllib.request
url='http://www.dytt8.net/'
user={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
html=urllib.request.urlopen(url)
html.encoding='utf-8'
soup=BeautifulSoup(html.read())
for i in soup.find_all('a'):
    if 'href' in i.attrs:
        print(i.attrs['href'])
