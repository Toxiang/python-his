import requests
import re
from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
def pandata(url):

    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath("//div[@class='Download']//div[@class='dl_url']//a[2]").click()
def get_down(url):
    html=requests.get(url)
    html.encoding='utf-8'
    url=re.findall('<a target="_blank" href="(.*?)"> <img src=".*?"  width="',html.text)
    # print(url)
    pandata(url[0])
    # html_downpage=requests.get(url[0])
    # html_downpage.encoding='utf-8'
    # down_url=re.findall('<a class="down2  baidu countHit" data-itemid="1110966" data-hot="true" href="(.*?)"',html_downpage.text)
    #
def get_html(url):
    html=requests.get(url)
    html.encoding='utf-8'
    # print(html.text)
    name_list=re.findall(r'<div class="t2"><a target="_blank" href=".*?">(.*?)</a></div>',html.text)
    url_list=re.findall(r'<div class="t2"><a target="_blank" href="(.*?)">.*?</a></div>',html.text)
    get_down(url_list[3])
    # print(len(name_list))
    # print(len(url_list))
if __name__ == '__main__':
    url='https://www.gamersky.com/'
    get_html(url)