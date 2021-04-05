import requests
from bs4 import BeautifulSoup
headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }

total=[]
url='https://www.qidian.com/rank/yuepiao?chn=0&page=1'
res=requests.get(url,headers=headers)

soup=BeautifulSoup(res.text,'html.parser')
书名s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > h4 > a')
作者s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.author > a.name')
类型s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.author > a:nth-of-type(2)')
简介s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.intro')
最新章节s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > p.update > a')
链接s=soup.select('#rank-view-list > div > ul > li > div.book-mid-info > h4 > a')

print(作者s)
for 书名,作者,类型,简介,最新章节,链接 in zip(书名s,作者s,类型s,简介s,最新章节s,链接s):
    data={'书名':书名.get_text().strip(),\
    '作者':作者.get_text().strip(),\
    '类型':类型.get_text().strip(),\
    '简介':简介.get_text().strip(),\
    '最新章节':最新章节.get_text().strip(),\
    '链接':链接['href'].strip()}
    total.append(data)
for i in total:
    print(i)
import pandas
deal1=pandas.DataFrame(total)
print(deal1)
