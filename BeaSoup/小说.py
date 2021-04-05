from bs4 import BeautifulSoup
import re
import requests
headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
url = "http://www.biquger.com/biquge/115076/46732745"

html = requests.get(url,headers=headers).text.encode('iso-8859-1').decode('utf-8')


soup = BeautifulSoup(html,'lxml')

title = soup.find('h1').text

print(title)