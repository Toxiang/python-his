import requests
import re
url='https://www.bilibili.com/ranking?spm_id_from=333.5.banner_link.2'
html=requests.get(url).text
#print(html)
list=re.findall('<div class="info"><a href="//(.*?)" target="_blank" class="title">(.*?)</a><!----><!----><div class="detail">',html)
j=1
for i in list:
    print(i[0]+i[1])
