import requests
import re
url='https://www.zhihu.com/people/shen-yu-bao/following'
user={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
html=requests.get(url,headers=user)
num=re.findall('<strong class="NumberBoard-itemValue" title=".*?" data-reactid=".*?">(.*?)</strong></div></a><a class',html.text)
print(int(num[0]))
if int(num[0])//20==0:
    n=int(num[0])//20
else:
    n=int(num[0])//20+1
print(n)
for i in range(1,n+1):
    print(i)
    url_i='https://www.zhihu.com/people/shen-yu-bao/following?page='+str(i)
    html_i=requests.get(url_i,headers=user)
    people=re.findall('urlToken&quot;:&quot;(.*?)&quot;', html_i.text)
    print(people)
    with open('D:\\sp_data\\zhihurenming.txt','a') as ff:
        for j in people:
            ff.write(j+'\n')