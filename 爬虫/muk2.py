import requests
import re
url='https://www.zhihu.com/people/shen-yu-bao/following?page=3'
user={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
html=requests.get(url,headers=user)
names = re.findall('urlToken&quot;:&quot;(.*?)&quot;', html.text)
print(names)
