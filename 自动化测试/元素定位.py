from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
url='http://www.baidu.com'
driver.get(url)
driver.maximize_window()

#   id定位
# driver.find_element_by_id('kw').send_keys("jj")
# driver.find_element_by_id('su').click()


#  name定位
# driver.find_element_by_name('wd').send_keys("jkj")
# driver.find_element_by_id('su').click()

#class name 定位
# driver.find_element_by_class_name('mnav').click()

#link_text
# news=driver.find_element_by_link_text("新闻")
# news.click()

# css_selector
# driver.find_element_by_css_selector('input[class="s_ipt"]').send_keys("网易云")
# driver.find_element_by_css_selector('#su').click()

#层级定位
# driver.find_element_by_css_selector('form>span:nth-child(1)>[class="s_ipt"]').send_keys("djjff")
driver.find_element_by_xpath('//form[@id="form"]//span[1]//input').send_keys("kkk")


# find_elements_by_id 
# find_elements_by_name
# find_elements_by_class_name
# find_elements_by_tag_name
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_css_selector
# find_elements_by_xpath

