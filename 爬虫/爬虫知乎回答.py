from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
import re
import requests
import html.parser
import time
if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="D:\py\chromedriver.exe")
    driver.get('https://www.zhihu.com/question/267460120')


    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            # try:
            #     driver.find_element_by_css_selector('button.QuestionMainAction').click()
            #     print("page" + str(i))
            #     time.sleep(10)
            # except:
            #     break


    execute_times(50)
    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    # soup_=soup.prettify()
    # print(soup_)
    class_list=soup.find_all('span',class_='RichText CopyrightRichText-richText')
    k=1
    for i in class_list:
        soup_i=BeautifulSoup(str(i),'lxml')
        print(soup_i)
        noscript_list=soup.find_all('noscript')
        for j in noscript_list:
        #    print(j.string)
            soup_j=BeautifulSoup(str(j.string),'lxml')
            img_list=soup_j.find_all('img')
            for img in img_list:
                print("正在爬取第"+str(k)+"张:",img.get('src'))
                jpg_html=requests.get(img.get('src'))
                with open('D:\\py\\知乎图片\\'+str(k)+'.jpg','wb')as f:
                    f.write(jpg_html.content)
                    k=k+1