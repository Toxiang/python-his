import requests
from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
    #创建txt文件
    file = open('全职法师.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/0_66/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #计算章节个数
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
    index = 1
    #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    begin_flag = False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        if child != '\n':
            #找到《一念永恒》正文卷,使能标志位
            if child.string == u"《全职法师》正文卷":
                begin_flag = True
            #爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_req = request.Request(url = download_url, headers = head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id = 'content', class_ = 'showtxt')
                print(texts)
                break
