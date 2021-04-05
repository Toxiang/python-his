from selenium import webdriver
from urllib import request
import pandas as pd
import time
import requests
def gethtml(url):
    loginurl='https://www.douban.com/'
    browser = webdriver.Chrome(executable_path="D:\py\chromedriver.exe")
    browser.maximize_window()
    browser.get(loginurl)
    browser.find_element_by_name('form_email').clear()
    browser.find_element_by_name('form_email').send_keys(u'17315392737')
    browser.find_element_by_name('form_password').clear()
    browser.find_element_by_name('form_password').send_keys(u'wzxwzx658')
    #手动输入验证码
    captcha_link=browser.find_element_by_id('captcha_image').get_attribute('src')
    request.urlretrieve(captcha_link,'captcha.jpg')
    captcha_code = input("pls input captcha code : ")
    browser.find_element_by_id('captcha_field').send_keys(captcha_code)

    # browser.find_element_by_css_selector('input[class="bn-submit"]').click()##lzform > fieldset > div.item.item-submit > input
    browser.find_elements_by_xpath("//div[@class='item item-submit']")
    browser.get(url)
    browser.implicitly_wait(10)
    return browser


def getcontent(url):
    i=1
    AllArticle = pd.DataFrame()
    brower=gethtml(url)
    while True:
        s=brower.find_elements_by_class_name('comment-item')
        articles=pd.DataFrame(s,columns=['web'])
        articles['user']=articles.web.apply(lambda x:x.find_element_by_tag_name('a').get_attribute('title'))
        articles['comment'] = articles.web.apply(lambda x: x.find_element_by_class_name('short').text)
        articles['star'] = articles.web.apply(lambda x: x.find_element_by_xpath("//*[@id='comments']/div[1]/div[2]/h3/span[2]/span[2]").get_attribute( 'title'))
        articles['date'] = articles.web.apply(lambda x: x.find_element_by_class_name('comment-time').get_attribute('title'))
        # articles['vote'] = articles.web.apply(lambda x: np.int(x.find_element_by_class_name('votes').text))
        del articles['web']
        AllArticle = pd.concat([AllArticle,articles],axis=0)
        print("第"+str(i)+"页完成")
        try:
            if i == 1:
                brower.find_element_by_xpath("//*[@id='paginator']/a").click()
            else:
                brower.find_element_by_xpath("//*[@id='paginator']/a[3]").click()
            brower.implicitly_wait(10)
            # time.sleep(3)  # 暂停3秒
            i = i + 1
        except:
            # AllArticle = AllArticle.reset_index(drop=True)
            return AllArticle

        # AllArticle = AllArticle.reset_index(drop=True)

        return AllArticle





if __name__ == '__main__':
    a=getcontent('https://movie.douban.com/subject/26882446/comments?sort=new_score&status=P')
    print(a)