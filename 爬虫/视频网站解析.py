import requests,re, json, sys
from bs4 import BeautifulSoup
from urllib import request

class video_downloader():
    def __init__(self, url):
        #*****这些url是从抓包软件中获得的*****
        self.server = 'http://api.xfsub.com'        #解析网站域名
        self.api = 'http://api.xfsub.com/xfsub_api/?url='
        self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'#post信息发往的服务器
        self.url = url.split('#')[0]     #去掉多余的字符串
        self.target = self.api + url
        self.s = requests.session()      #身份证，用来持续访问服务器

    """
    函数说明:获取key、time、url等参数（POST给服务器）

    """
    def get_key(self):
        req = self.s.get(url=self.target)   #获得解析网站发送的key等信息
        req.encoding = 'utf-8'              #编码
        print(req.text)
        self.info = json.loads(re.findall('"url.php",\ (.+),', req.text)[0])   #json.loads用于将json格式数据转换为python格式，是个字典

    """
    函数说明:获取视频地址

    """
    def get_url(self):
        data = {'time':self.info['time'],
            'key':self.info['key'],
            'url':self.info['url'],
            'type':''}
        req = self.s.post(url=self.get_url_api,data=data)   #将key等发送给另外一个服务器
        url = self.server + json.loads(req.text)['url']     #服务器返回一个json文件
        req = self.s.get(url)                               #再对新网址发送请求命令
        bf = BeautifulSoup(req.text,'xml')                  #返回xml文件                     #因为文件是xml格式的，所以要进行xml解析。
        video_url = bf.find('file').string                  #获得视频地址                        #匹配到视频地址
        return video_url

    #**********以上两步相当于把解析网址申请视频的过程用代码进行了一遍********

    """
    函数说明:回调函数，打印下载进度

    """
    def Schedule(self, a, b, c):
        per = 100.0*a*b/c
        if per > 100 :
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per,a*b,c) + '\r')
        sys.stdout.flush()

    """
    函数说明:视频下载

    """
    def video_download(self, url, filename):
        request.urlretrieve(url=url,filename=filename,reporthook=self.Schedule)


if __name__ == '__main__':
    url = 'http://www.iqiyi.com/v_19rrnqzc4g.html#vfrm=19-9-0-1'
    filename = '王牌特工：特工学院'
    vd = video_downloader(url)
    print('%s下载中:' % filename)
    vd.get_key()
    # video_url = vd.get_url()
    # print('  获取地址成功:%s' % video_url)
    # vd.video_download(video_url, filename+'.mp4')
    # print('\n下载完成！')