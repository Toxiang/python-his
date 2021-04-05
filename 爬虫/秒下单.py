import requests
import time
import smtplib
from email.mime.text import MIMEText
#     email用于构建邮件内容
from email.header import Header

#接收邮件
mail = [
        '2543820733@qq.com'

]

# 商品url
url = [
        'https://c0.3.cn/stock?skuId=100010172240&area=12_933_3407_56188&venderId=1000093247&buyNum=1&choseSuitSkuIds=&cat=1320,1583,1592&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1339782362&ch=1&callback=jQuery7108562'
        ,'https://c0.3.cn/stock?skuId=100002355147&area=12_933_3407_56188&venderId=1000003443&buyNum=1&choseSuitSkuIds=&cat=9987,653,655&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=1339782362&ch=1&callback=jQuery4814245'
    ]

def sendMail(url):


    # 用于构建邮件头

    # 发件方的信息：发信邮箱，qq 邮件授权码

    from_address = '1074450267@qq.com'
    psd = 'bhlboxjqijowgbaf'

    # 收信方
    for i in mail:
        # print(i)
        to_address = i
        print(to_address)
        # 发信服务器
        smtp_server = 'smtp.qq.com'
        # bhlboxjqijowgbaf
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式（plain 为纯文本）
        msg = MIMEText(url,'plain','utf-8')
        # msg = MIMEText('ssss','plain','utf-8')
        msg['From'] =  Header(from_address)
        msg['To'] = Header(to_address)
        msg['subject']  = Header('dd')

        # 开启发送服务，使用加密传输
        server = smtplib.SMTP_SSL(host=smtp_server)
        server.connect(smtp_server,465)
        # 登陆发信邮箱
        server.login(from_address,psd)
        # 发送邮件
        server.sendmail(from_address,to_address,msg.as_string())

        server.quit()

flag = 0
run = 1
# sendMail(11)
while(run):
    run=0
    try:

        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        print('第' + str(flag) + '次 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        flag += 1
        for i in url:
            # skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
            # print(skuidUrl)
        #商品url
            # print(i)
            skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
            response = session.get(i)
            # print(response.text)

            if (response.text.find('无货') > 0):
                print('无货 ： ' + skuidUrl)
            else:
                print('有货! 有货! 有货! ： ' + skuidUrl)
                # sendMail(skuidUrl)

        time.sleep(5)
    except Exception as e:
        import traceback

        print(traceback.format_exc())
        print('异常')
        time.sleep(10)
