import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
url='https://www.qisuu.la/soft/sort01/'
html=requests.get(url)
html.encoding='utf-8'
list=re.findall('<a style="font-weight: normal;" href="(.*?)">',html.text)

html_2=urlopen('https://www.qisuu.la'+list[2])
soup=BeautifulSoup(html_2,'lxml')
list=soup.find_all('div',class_='pc_list')
soup_2=BeautifulSoup(str(list),'lxml')
#print(soup_2)
list_2=soup_2.find_all('li')
for i in list_2:
    content_url='https://www.qisuu.la/du/36/36877/'+i.a.get('href')
    content_html=urlopen(content_url)
    content_soup=BeautifulSoup(content_html,'lxml')
    content_list=soup.findAll('div',class_ ='txt_cont')
    print(content_list)
    break
    # print(content_url)
    # content_html=requests.get(content_url)
    # content_html.encoding='utf-8'
    # contents=re.findall('(.*?)<br />',content_html.text)
    # print(contents)
    # for content in contents:
    #     with open('D:\\py\\龙王传说.txt','a') as f:
    #         f.write(content)
    # break
    # #print(i.a)

# from urllib import request
# from bs4 import BeautifulSoup
#
# if __name__ == "__main__":
#     target_url = 'http://www.biqukan.com/1_1094/'
#     head = {}
#     head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
#     target_req = request.Request(url = target_url, headers = head)
#     target_response = request.urlopen(target_req)
#     target_html = target_response.read().decode('gbk','ignore')
#     #创建BeautifulSoup对象
#     listmain_soup = BeautifulSoup(target_html,'lxml')
#     #搜索文档树,找出div标签中class为listmain的所有子标签
#     chapters = listmain_soup.find_all('div',class_ = 'listmain')
#     for i in chapters:
#         print(i)
    # #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    # download_soup = BeautifulSoup(str(chapters), 'lxml')
    # #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    # begin_flag = False
    # #遍历dl标签下所有子节点
    # for child in download_soup.dl.children:
    #     #滤除回车
    #     if child != '\n':
    #         #找到《一念永恒》正文卷,使能标志位
    #         if child.string == u"《一念永恒》正文卷":
    #             begin_flag = True
    #         #爬取链接
    #         if begin_flag == True and child.a != None:
    #             download_url = "http://www.biqukan.com" + child.a.get('href')
    #             download_name = child.string
    #             print(download_name + " : " + download_url)