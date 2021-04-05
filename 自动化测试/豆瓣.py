from selenium import webdriver
import re
def get_html():
    url='https://www.douban.com/'
    driver=webdriver.Chrome(executable_path='D:\py\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id('form_email').clear()
    driver.find_element_by_id('form_email').send_keys(u'17315392737')
    driver.find_element_by_id('form_password').send_keys(u'wzxwzx658')
    code=input("请输入验证码：")
    driver.find_element_by_id('captcha_field').send_keys(code)
    driver.find_element_by_class_name('bn-submit').click()
    driver.find_element_by_id('inp-query').send_keys("斗破苍穹")
    driver.find_element_by_xpath('//div[@class="inp-btn"]//input').click()
    driver.find_element_by_xpath('//div[@class="result-list"]//div[@class="result"]//div[2]//a').click()

    return driver

def get_content():
    driver=get_html()
    all=driver.window_handles
    # print(all)
    # print(driver.current_window_handle)
    driver.switch_to_window(all[2])
    # print(driver.current_window_handle)
    driver.find_element_by_xpath('//div[@id="comments-section"]//h2//a').click()
    # i=1
    # while(i<10):
    #     content=driver.find_element_by_class_name('short').text
    #     print(content)
    #     i=i+1
    # return driver
    content_html=driver.page_source
    content_list=re.findall('<span class="short">(.*?)</span>',content_html)
    for i in content_list:
        print(i)


if __name__ == '__main__':
    a=get_content()
