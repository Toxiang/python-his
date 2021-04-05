import json
from urllib import request
import re
import pkginfo
def data(url):
    headers = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Language':'zh-CN,zh;q=0.3',
            'Referer':'https://item.taobao.com/item.htm',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Connection':'keep-alive',
        }
    # url = 'https://item.taobao.com/item.htm?spm=a219r.lm895.14.16.78e06359x1sZSn&id=574793692960&ns=1&abbucket=7'
    url=url
    goods_id = re.findall('id=(\d+)', url)[0]
    print(goods_id)
    html = request.Request(url,headers=headers)
    reponse=request.urlopen(html).read().decode('gbk','ignore')
    # print(reponse)
    title=re.findall('<h3 class="tb-main-title" data-title="(.*?)">',reponse)
    # print(title[0])

    befor_price = re.findall('<em class="tb-rmb-num">(.*?)</em>', reponse)[0]
    # print(befor_price)
    price_url = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={}&modules=price,xmpPromotion".format(goods_id)

    price_req = request.Request(url=price_url, headers=headers)
    price_res = request.urlopen(price_req).read().decode('gbk')

    price_data = list(set(re.findall('"price":"(.*?)"', price_res)))
    # print(price_data)
    real_price = ""
    for t in price_data:
        if '-' in t:
            real_price = t
            break
    if not real_price:
        real_price = sorted(map(float,price_data))[0]
    print('商品名:',title[0])
    print('价格:', befor_price)
    print('淘宝价:', real_price)
    # 爬取图片











if __name__ == '__main__':
    # url=str(input("链接："))
    url='https://item.taobao.com/item.htm?spm=a219r.lm895.14.19.78e06359x1sZSn&id=575591616710&ns=1&abbucket=7'
    data(url)
# real_price = ""
# for t in data:
#     if '-' in t:
#         real_price = t
#         break
# if not real_price:
#     real_price = sorted(map(float, data))[0]





#爬取价格
# url='https://s.taobao.com/list?spm=a217m.8316598.313651-static.12.3c6633d54S6LiD&q=%E5%8D%AB%E8%A1%A3&cat=50344007&style=grid&seller_type=taobao'
# price_html=request.Request(url)
# price_response=request.urlopen(price_html).read().decode('utf-8','ignore')
#
#         #分析网页源码解析出价格
# price = re.findall(r'\"view_price\":\"\d+\.\d+?"',price_response)
# title = re.findall(r'\"raw_title\":\".+?\"',price_response)
#         # test this re
# print(price)
# print(title)
#         # for i in range(len(price)):
#         #     _price = eval(price[i].split(':')[1])
#         #     _title = eval(title[i].split(':')[1])
#         #     # infoList.append([_price, _title])
#
# print()
# # content = re.findall(r'g_page_config = (.*?) g_srp_loadCss',reponse,re.S)[0].strip()[:-1]
# # #格式化
# # content = json.loads(content)
