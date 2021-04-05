import requests
import json
import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
def gethtml():
    url='https://music.163.com/#/song?id=486814412'
    driver.get(url)
    driver.maximize_window()
    ele=driver.find_element_by_class_name('g-iframe')
    driver.switch_to.frame(ele)
    cmts = driver.find_element_by_xpath("//div[@class='cnt f-brk']/a[@class='s-fc7']").text
    print(cmts)
    # driver.find_element_by_xpath('//div[@class="auto-1539673884593 u-page"]//div[@class="zpgi zpg2 js-i-1539673884591"]').click()
    # print(driver.page_source)
    time.sleep(1)

url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_486814412?csrf_token='
gethtml()
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Origin': 'http://music.163.com',
    'Referer': 'http://music.163.com/song?id=551816010',
    'Host': 'music.163.com'
}
#加密数据
user_data={
    'params': 'VnigabB3RWh3YjHYjeI8lQkwjeI0/IHpRxkU3D+2pm4V1B+HS8lShoovF3OVKUyoRZVg3I1SDH0j3FkY3EXTbGMaQeIPS95/neTpb9Cu5uDvhWXhFwT1Ame/2a2LlNetVaFS0+tVbpMheg8kpaj1hKMtJHS+jxfPAmO8T7FGtDQZOABHXrkXu2ZpQTdsZRh8',
    'encSecKey': 'a2233ce6e72bf2bb8492412067b63fd895037234d806288c6b908a827168386421cea69503afbc745197aa64a4b50f719f1e52c2719f9d41a3b2fb6c4e4ba83c17c1caf224391045ba3ad0161c292cb3ce9b12c85de5ad313d01aa06cb709f959aa6385e0eb989602969e364cf6c306b1c85d709e1716f3d5cc67faa13a717f5'
}
response=requests.post(url,headers=header,data=user_data)
data=json.loads(response.text)
#print(data)
for hotcomment in data['comments']:
    print(hotcomment['content'])
    # f + SZvV2z38PTY9uNhY20ijVCYtrneQR04 / ah9cCIKsjjF7ke + n5g7oe9b7NBdkYOUxN9uT4gxTC8lquRmS3XTcHRoj2wphGfLmfap / jLCkjMLU0N4J0te4TFnwvsenwMBag
    # IzbcABY9WqirJMp4m + mdBbwuCsfDIJm6UqzBhZxavFauvspUe6FM0NpfMlD9 + nutz8LPMUrKF6sFxYtJYBgc5iLOspYHkLn2TU3i8WOQ =
    # pepVUJcs3jBlXt1q4LkDDZKaVweqwc + ulFMJVG / vb + hyOMDDBob1dwhXjKqxS6fUn0rGIbKZ0vw8EuBclIDU92apkzQwfDCmw6hYSQo0B9YU1 / 1
    # y2M5N8UM3Ty8McsIl9oFBp3jbEsRDVDpoiVQ6hm8dBtVI7j4EECkrsI4V8Z8SUgcdgyp8WYM91mX0E0H0GDA8bQpXdSuUI9uagLhWtuFALj1s / ADe71hDZJRGwi8 =
# import re
# from selenium import webdriver
# import requests
# import urllib.request
# import json
# from bs4 import BeautifulSoup
# def get_all_hotSong():     #获取热歌榜所有歌曲名称和id
#     url='http://music.163.com/discover/toplist?id=3778678'    #网易云云音乐热歌榜url
#     header={    #请求头部
#         'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
#     }
#     request=urllib.request.Request(url=url, headers=header)
#     html=urllib.request.urlopen(request).read().decode('utf8')   #打开url
#     soup=BeautifulSoup(html,'lxml')
#     list=soup.find_all('ul',class_='f-hide')
#     soup_1=BeautifulSoup(str(list[0]))
#     name_list=soup_1.find_all('a')
#     for name in name_list:
#         print(name.string)
    #html=str(html)     #转换成str
    # pat1=r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>'  #进行第一次筛选的正则表达式
    # result=re.compile(pat1).findall(html)     #用正则表达式进行筛选
    # result=result[0]     #获取tuple的第一个元素
    #
    # pat2=r'<li><a href="/song\?id=\d*?">(.*?)</a></li>' #进行歌名筛选的正则表达式
    # pat3=r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'  #进行歌ID筛选的正则表达式
    # hot_song_name=re.compile(pat2).findall(result)    #获取所有热门歌曲名称
    # hot_song_id=re.compile(pat3).findall(result)    #获取所有热门歌曲对应的Id
    #
    # return hot_song_name,hot_song_id
# get_all_hotSong()
#hot_song,hot_song_id=get_all_hotSong()
# for i in range(0,51):
#     print(hot_song[i])
#     print(hot_song_id[i])
# driver =webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
# driver.get('http://music.163.com/#/discover/toplist?id=3778678')
# html=driver.page_source
# soup=BeautifulSoup(html,'lxml')
# #print(soup.prettify())
# list=soup.find_all('span',class_='txt')
# print(list)