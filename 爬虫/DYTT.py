import requests
import re
a_url='http://www.dytt8.net/html/gndy/dyzz/list_23_2.html'
html=requests.get(a_url)
html.encoding='gb2312'
#print(html.text)
a_list=re.findall('<a href="(.*?)" class="ulink">',html.text)
#print(a_list)
for i in a_list:
    i='http://www.dytt8.net'+i
    html_i=requests.get(i)
#    print(html_i.text)
    html_i.encoding='gb2312'
    i_list=re.findall('<a href="(.*?)">.*?</a></td>',html_i.text)
    print(i_list)
    with open('D:\\py\\zhihu2.txt','a') as ff:
        for j in i_list:
             ff.write(j+'\n')