import requests
import re
url='https://item.taobao.com/item.htm?spm=a219r.lm895.14.16.78e06359x1sZSn&id=574793692960&ns=1&abbucket=7'
html=requests.get(url)
infolist=re.findall('<li title=.*?>(.*?)</li>',html.text)
for i in infolist:
    print(i)