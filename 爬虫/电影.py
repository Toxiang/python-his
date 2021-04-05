import requests
import re
def get_html(url):
    html=requests.get(url)
    movie_list=re.findall('<span class="title">(.*?)</span></a><p class="intro">',html.text)
    acter=re.findall('<p class="intro">(.*?)</p></li><li class="card s190x254 ">',html.text)
    link=re.findall('<a href="(.*?)" title=".*?" class="link">',html.text)
    image=re.findall('<img src="(.*?)"',html.text)
    for i in image:
        print(i)
    for i in range(1,31):
        print(image[i])
        imager=requests.get(image[i])
        print(image[i])
        with open('C:\\Users\\wangz\\Desktop\\img\\'+movie_list[i]+'.jpg','wb')as f:
            f.write(imager.content)



if __name__ == '__main__':
    for i in range(1,2):
        url='http://v.hao123.baidu.com/v/search?channel=movie&pn='+str(i)
        get_html(url)