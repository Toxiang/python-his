# import itchat
# itchat.auto_login()
# for friend in itchat.get_friends(update=True)[0:]:
#     print(friend['NickName'],friend['RemarkName'],friend['Sex'],friend['Province'],friend['Signature'])
#     img=itchat.get_head_img(userName=friend['UserName'])
#     path="D:/py/img/"+friend['NickName']+"("+friend['RemarkName']+").jpg"
#     try:
#         with open(path,'wb')as f:
#             f.write(img)
#     except Exception as e:
#         print(repr(e))
# itchat.run()
import os

from math import sqrt
from PIL import Image
path='D:/py/img/'
pathlist=[]

for item in os.listdir(path):
    imgpath=os.path.join(path,item)
    pathlist.append(imgpath)
total=1600
line=int(sqrt(total))
NewImage=Image.new('RGB',(128*line,128*line))
x=y=0
for item in pathlist:
    try:
        img=Image.open(item)
        img=img.resize((128,128),Image.ANTIALIAS)
        NewImage.paste(img,(x*128,y*128))
        x+=1
    except IOError:
        print("第%d行,%d列文件读取失败")
        x-=1
    if x==line:
        x=0
        y+=1
    if(x+line*y)==line*line:
        break
NewImage.save(path+"final.jpg")
