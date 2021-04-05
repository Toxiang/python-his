from bs4 import BeautifulSoup
from selenium import webdriver
import time
import xlwt


def Save(soup):
    list = soup.find(class_='grid-16-8 clearfix').find(class_='bd').find(class_='carousel').find(class_='slide-list').find_all('ul')
    # print(list)
    k=0
    for item in list:
        item.find_all('li')

        for i in item:
            k = k+1
            print("-----------------------------------------------------------------------------")
            print(i)
    # sel = list.find('select')
    #     print(item)
    #     break
    # print((sel))
    print(k)
def GetSource():
    time.sleep(1)
    # driver.switch_to.window(driver.window_handles[2])

    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')

    Save(soup)
    # print(html)
    driver.quit()

def readss(url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    GetSource()


# http://opac.nlc.cn/F/1Y19B49DX35J45GUPEHG36XVJ6KIYYTKFMB8F8RJFCYIDKDVUT-07758?func=find-b&find_code=ISB&request=9787108006721&local_base=NLC01&filter_code_1=WLN&filter_request_1=&filter_code_2=WYR&filter_request_2=&filter_code_3=WYR&filter_request_3=&filter_code_4=WFM&filter_request_4=&filter_code_5=WSL&filter_request_5=
if __name__ == '__main__':
    url = 'https://book.douban.com/'
    driver = webdriver.Chrome(executable_path="D:\py\chromedriver.exe")
    readss(url)