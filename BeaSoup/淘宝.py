from selenium import webdriver
import re
import time
from selenium.webdriver.common.action_chains import ActionChains


def search_word(key_word):
    # 使用id定位输入框的位置 并输入
    driver.maximize_window()
    driver.find_element_by_id("q").send_keys(key_word)
    driver.find_element_by_class_name("btn-search").click()
    # 填写账号密码
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="login-password"]/form[@id="login-form"]/div[@class="fm-field"]').find_element_by_id("fm-login-id").send_keys(15261204923)
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="login-password"]/form[@id="login-form"]/div[@class="fm-field"]').find_element_by_xpath('//input[@name="fm-login-password"]').send_keys('wzx@658')
    # 模拟鼠标拉动滑块
    time.sleep(1)
    kick = driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
    ActionChains(driver).click_and_hold(kick).move_to_element_with_offset(kick,305,1).perform()
    ActionChains(driver).release().perform()
    # 登录
    time.sleep(1)
    driver.find_element_by_class_name("fm-btn").click()

    # print(kick)
    # driver.find_element_by_class_name("fm-login-id").send_keys(17315392737)
    # driver.find_element_by_class_name("fm-login-password").send_keys('wzxwzx658')
    # driver.find_element_by_id("fm-button").click()
    # time.sleep(15)
    time.sleep(8)
    page_info = driver.find_element_by_xpath('//div[@class="total"]').text
    # print(page_info)
    page = re.findall("(\d+)",page_info)
    # print(page)
    return page

def get_data():
    items = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for item in items:
        # 基本信息
        pro_info = item.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        print(pro_info)
        # 价格信息
        pro_price = item.find_element_by_xpath('.//strong').text
        print(pro_price)
        pro_people = item.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        print(pro_people)
    # print(items)


if __name__ == '__main__':
    key_word = '粽子'
    driver = webdriver.Chrome(executable_path="D:\py\chromedriver.exe")
    driver.get('https://www.taobao.com/')
    pages = search_word(key_word)
    # for i in range(1,int(pages[0])):
    get_data()



