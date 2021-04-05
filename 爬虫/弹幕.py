import requests
import re
url='https://api.live.bilibili.com/ajax/msg'
form={
    'roomid':' 30493',
    'csrf_token': '2ea7f36d9ccab0f1b04482388772f6c9',
    'visit_id': '40qt7lo208o0'
}
cookie={'Cookie': 'fts=1513943533; UM_distinctid=1607e1110e9321-00619bfdc5f8b9-3f63450e-1fa400-1607e1110eb58; sid=9se3bsm7; buvid3=4F0D5BEA-F555-44CC-9B2C-4FD2D0B0F2E18007infoc; rpdid=olimslxiiwdosoklpksiw; pgv_pvi=27276288; CURRENT_QUALITY=80; finger=edc6ecda; LIVE_BUVID=49dd22e4ea6b0af75705ec84523592af; LIVE_BUVID__ckMd5=25c50ebefdee5873; DedeUserID=20333652; DedeUserID__ckMd5=4711e6ba5a014c6d; SESSDATA=8bf817fb%2C1529160794%2C82bb3b32; bili_jct=2ea7f36d9ccab0f1b04482388772f6c9; _dfcaptcha=6db49ca22233804ad2f1bda25fd8a91a; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526912891,1526912960,1526913140,1526913171; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1526913263'}
html=requests.post(url,data=form)
danmu = list(map(lambda x:html.json()['data']['room'][x]['text'], range(10)))
#print(danmu)
message=danmu[0]
print(message)
url2='https://api.live.bilibili.com/msg/send'
form2 = {  'color':'16777215',
                        'csrf_token':'476a087c35bded09ec0caa9e10a3c7c9',
                        'fontsize':'25',
                        'mode':'1',
                        'msg':message,
                        'rnd':'1524919101',
                        'roomid':'30493'  }
        # 发送
for i in range(1,100):
 html = requests.post(url2, data=form2, cookies=cookie)

