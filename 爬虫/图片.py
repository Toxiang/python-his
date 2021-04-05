import requests
import re
def get_jpg(url,n):
    jpg_html=requests.get(url)
    jpg_html.encoding='gbk'
    jpg_url=re.findall('<a href="(.*?)" title=".*?" target="_blank"><i class="iconfont">&#xe75d;',jpg_html.text)
    print(jpg_url)
    jpg=requests.get(jpg_url[0])
    print(jpg)
    with open('D:\\py\\content\\'+str(n)+'.jpg','wb')as f:
        f.write(jpg.content)
if __name__ == '__main__':
    for i in range(6,10):
        url='http://www.xiazaizhijia.com/bizhi/4724'+str(i)+'.html'
        get_jpg(url,i)

