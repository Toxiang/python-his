# from selenium import webdriver
# import requests
# import re
# if __name__ == "__main__":
#     browser = webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
#     # 打开百度文库的首界面
#     browser.get("https://wenku.baidu.com/")
#     # 通过ID找网页的标签，找到搜索框的标签
#     seek_input = browser.find_element_by_id("kw")
#
#     # # 设置搜索的内容
#     seek_input.send_keys("饮料")
#     # # 找到搜索文档按钮
#     seek_but = browser.find_element_by_id("sb")
#     # 并点击搜索文档按钮
#     seek_but.click()
#     url=browser.current_url
#     html=requests.get(url)
#     html.encoding='gb2312'
#     content_list=re.findall('a href="(.*?)"',html.text)
#     for i in content_list:
#         print(i)
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import re
# if __name__ == '__main__':
#     options=webdriver.ChromeOptions()
#     options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
#     brower=webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe",chrome_options=options)
#     brower.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
#     seek_continue=brower.find_element_by_xpath("//div[@class='foldpagewg-text']")
#     seek_continue.click()
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(executable_path='D:\py\chromedriver.exe',chrome_options = options)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
# page = driver.find_element_by_xpath("//div[@class='foldpagewg-text']")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
#driver.execute_script('arguments[0].scrollIntoView();', page) #拖动到可见的元素去
nextpage = driver.find_element_by_xpath("//div[@class='foldpagewg-text']")
nextpage.click()
page = driver.find_element_by_xpath("//div[@class='pagerwg-schedule']")
driver.execute_script('arguments[0].scrollIntoView();', page)
nextpage = driver.find_element_by_xpath("//div[@class='pagerwg-button']")
nextpage.click()
page = driver.find_element_by_xpath("//div[@class='pagerwg-schedule']")
driver.execute_script('arguments[0].scrollIntoView();', page)
nextpage = driver.find_element_by_xpath("//div[@class='pagerwg-button']")
nextpage.click()

html_=driver.page_source
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
text_list=soup.find_all('div',class_='content singlePage wk-container')
for i in text_list:

    soup_i=BeautifulSoup(str(i),'lxml')
    p_text=soup_i.find_all('p',class_='txt')
    for j in p_text:

        #print(j)
        soup_j=BeautifulSoup(str(j),'lxml')
        print(soup_j.get_text.string)
       # break
 #   print(soup_i.prettify())
#     page=BeautifulSoup(i,'lxml')
#     print(page.prettify())
