import requests
import re
url='https://www.qisuu.la/soft/sort01/'
html=requests.get(url).text
#print(html)
novel=re.findall('<a href="(.*?)"><img src=".*?" onerror=.*?>《天醒之路》全集</a>',html)
novel_url='https://www.qisuu.la'+novel[0]
print(novel_url)
novel_html=requests.get(novel_url).text
novel_title=re.findall('<a class="downButton" href=\'(.*?)\' title=.*?',novel_html)
print(novel_title[0])
novel_text_url='https://www.qisuu.la'+novel_title[0]
novel_text_html=requests.get(novel_text_url)
novel_text_html.encoding='utf-8'
novel_list=re.findall('<li><a href=".*?.html">(.*?)</a></li>',novel_text_html.text)
for i in novel_list[12:]:
    print(i)
    with open('D:\\sp_data\\novel.txt','a') as ff:
        ff.write(i+'\n')
