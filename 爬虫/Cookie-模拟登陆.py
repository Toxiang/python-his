from urllib import request
from http import cookiejar
if __name__ == '__main__':
    cookie=cookiejar.CookieJar()
    #声明一个CookieJar对象实例来保存cookie
    cookiename='D:\\py\\cookie.txt'
    cookie=cookiejar.MozillaCookieJar()#声明一个MozillacookieJar对象来保存cookie
    cookie.load(cookiename,ignore_expires=True,ignore_discard=True)
    handler=request.HTTPCookieProcessor(cookie)
    #利用request的HTTPcookieprocessor来创建cookie处理器，也就是cookiehandler
    opener=request.build_opener(handler)#通过cookiehandler创建opener
    response=opener.open('https://www.baidu.com/')#用open的方式打开url
    #cookie.save(ignore_discard=True,ignore_expires=True)
    #print("保存成功")
    print(response.read())
    for item in cookie:
        print('name=%s'%item.name)
        print('value=%s'%item.value)