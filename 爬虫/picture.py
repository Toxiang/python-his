import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
def get_next_url(url):
    html=requests.get(url)
    html.encoding='gb2312'
    next_url=re.findall('<div class="r">下一篇：<a href=\'(.*?)\'',html.text)
    print(next_url[0])
    return next_url[0]
def getsrc(url,i):
    html=requests.get(url)
    html.encoding='gb2312'
    src=re.findall(' src="(.*?)" /></a><a href=\'.*?\' class="rightFix" id="rightFix"></a>',html.text)
    name=re.findall('<img alt="(.*?)"  src=".*?" />',html.text)
    print(src[0])
    getcontent(src[0],i,name[0])
def getcontent(src,i,name):
    html=requests.get(src)
    with open('D:\\py\\content\\'+str(name)+str(i)+'.jpg','wb')as f:
        f.write(html.content)

def st(url):
    for i in range(1, 7):
        url_src = str(url)[0:48] + '_' + str(i) + '.html'
        getsrc(url_src, i)
url='http://www.27270.com/ent/meinvtupian/2018/272701.html'
for i in range(1,5):
    st(url)
    url=get_next_url(url)


