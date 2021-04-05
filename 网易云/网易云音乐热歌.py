from selenium import webdriver


# def get_page():
    # driver = webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
    # url='https://music.163.com/'
    # driver.get(url)
    # driver.maximize_window()
    # driver.find_element_by_xpath('//div[@id="g_nav2"]//div[@class="wrap f-pr"]//ul//li[2]')
    # html=driver.page_source
    # print(html)
# html=get_page()
driver = webdriver.Chrome(executable_path="D:\py\chromedriver_win32\chromedriver.exe")
def get_mation(url):
    driver.get(url)
    driver.maximize_window()
    driver.switch_to_frame('g_iframe')
    try:
        song_name=driver.find_element_by_xpath('//div[@class="cnt"]//div[@class="hd"]//div').text
        singer_name=driver.find_element_by_xpath('//div[@class="cnt"]//p[1]//span').get_attribute('title')
        zhuanji=driver.find_element_by_xpath('//div[@class="cnt"]//p[2]//a').text
        with open('C:\\Users\\wangz\\Desktop\\song.txt','a') as f:
            f.write("歌名："+song_name+"  ")
            f.write("歌手："+singer_name+"  ")
            f.write("专辑："+zhuanji+'\n')
            f.write('\n')
    except:
        return



url='https://music.163.com/'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//div[@id="g_nav2"]//div[@class="wrap f-pr"]//ul//li[2]').click()
driver.switch_to_frame('g_iframe')
url_list=[]
for i in range(1,100):
    try:
        url_list.append(driver.find_element_by_xpath('//div[@class="j-flag"]//table//tbody//tr['+str(i)+']//td[2]//div//div//a').get_attribute('href'))

    except:
        continue
# print(url_list[2])
for i in range(1,100):
    get_mation(url_list[i])

