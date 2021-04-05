from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
def geturl():
    url='https://www.taobao.com/'

    driver.get(url)
    driver.maximize_window()
    login_url=driver.find_element_by_xpath('//div[@class="member-ft"]//div[@data-spm-ab="2"]//a[1]').get_attribute('href')
    return login_url
def login():
    login_url=geturl()
    driver.get(login_url)
    driver.find_element_by_xpath('//div[@class="quick-form"]//div[@class="login-links"]//a[1]').click()
    driver.find_element_by_id('TPL_username_1').send_keys(u'15261204923')
    time.sleep(2)
    driver.find_element_by_id('TPL_password_1').send_keys(u'wzx@658')
    # span_background=driver.find_element_by_id('nc_1__scale_text')
    # span_background_size=span_background.size
    span_background = driver.find_element_by_class_name('nc-lang-cnt')
    span_background_size = span_background.size
    print(span_background_size)
    button=driver.find_element_by_id('nc_1_n1z')
    button_location=button.location
    x_location = button_location["x"] +290
    y_location = button_location["y"]
    ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()
if __name__ == '__main__':
    login()


