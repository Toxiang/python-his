import requests
import re
from openpyxl import workbook
from openpyxl import load_workbook
import os
os.chdir("C:\\Users\\wangz\\Desktop")
def get_info(url):
    global ws
    html=requests.get(url)
    user_name=re.findall('<a class="leader-board__nickname" data-link="leaderboard-link" href=".*?">(.*?)</a>',html.text)
    RP=re.findall('<div class="leader-board__table-content ">(.*?)</div></td>',html.text)
    total=re.findall('<div class="leader-board__table-content">(.*?)</div></td>',html.text)
    win_per=re.findall('<span class="leader-board__grades-value">(.*?)</span>',html.text)
    top_ten=re.findall('<div class="leader-board__grades-value">(.*?)</div>',html.text)
    data=re.findall('<div class="leader-board__table-content">([\s\S]*?)</div>',html.text)
    hate=re.findall('<div class="leader-board__grades-value">(.*?)</div>',html.text)
    KDA=[]
    ave_grade=[]
    for i in range(0,len(data)+1):
        if((i-1)%3==0):
           KDA.append(data[i].replace(" ",'').replace("\n",''))
        if((i+1)%3==0):
            ave_grade.append(data[i].replace(" ",'').replace("\n",''))
    for j in range(0,497):
        try:
            ws.append([str(j+4),user_name[j],RP[j],total[j],win_per[j],top_ten[j],KDA[j],hate[j],ave_grade[j]])
        except:
            continue
if __name__ == '__main__':
    url='https://pubg.op.gg/leaderboard'
    wb=workbook.Workbook()
    ws=wb.active
    ws.append(['排名','用户名', 'RP', '游戏场数', '胜%', 'Top10%', 'K/D', '伤害', '平均排名'])
    get_info(url=url)
    wb.save('pubg.xlsx')
