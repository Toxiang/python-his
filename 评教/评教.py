import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.binary_location = r'D:\py\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(chrome_options=chrome_options)
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(executable_path='D:\py\chromedriver_win32\chromedriver.exe',chrome_options = options)
driver.get('http://202.195.102.33/')


def wait_items_by_class_name(class_name):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
    )


def wait_item_by_id(id_):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, id_))
    )


def accept_alert():
    t = 0
    while t < 25:
        try:
            driver.switch_to.alert.accept()
        except:
            time.sleep(0.2)
            t += 1


# page 1 - 登录
driver.find_element_by_id('UserName').send_keys('16441129')
driver.find_element_by_id('Password').send_keys('300918')
wait_item_by_id('getpassword').click()

# page 2 - 选择学生选课
# btn = driver.find_element_by_id('ImageButton1')
wait_item_by_id('ImageButton1').click()

# page 3 - 进入评教
# driver.execute_script('__doPostBack("GVxmxz", "Select$1")')
for item in wait_items_by_class_name('dg1-item'):
    assert isinstance(item, WebElement)
    if '学生评教' in item.text:
        item.find_element_by_css_selector('input[type=button]').click()
        break

# page 4 - 点击图片
wait_item_by_id('ImageButton1').click()

# page 5 - 评教页面
for i in range(len(wait_items_by_class_name('dg1-item'))):
    driver.execute_script('__doPostBack("GVpjkc", "CmdPj$%s")' % i)

    items = wait_items_by_class_name('dg1-item')
    for item in items:
        item.find_element_by_css_selector('input[value="100"]').click()
    random.choice(items).find_element_by_css_selector('input[value="80"]').click()

    elem = wait_item_by_id('DDztpj')
    elem.find_element_by_css_selector('option[value="很好"]').click()

    wait_item_by_id('BTjc').click()
    accept_alert()

    try:
        wait_item_by_id('BTbc').click()
        accept_alert()
    except:
        driver.back()

driver.close()