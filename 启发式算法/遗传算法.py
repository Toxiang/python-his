import random
import numpy as np
import math

num_city = 30 # 城市数目
num_total = 100 #随机生成随机解的数目
copy_num = 50 # 保留解的数目
cross_num = 40 #交叉解的数目
var_num = 10 # 变异数目

location = np.loadtxt('city.txt')
location = location.T
# 随机生成初始解

def generate_initial():
    initial = []
    city = list(range(num_city))
    for i in range(num_total):
        random.shuffle(city)
        p = city.copy()
        while(p in initial):
            random.shuffle(city)
            p=city.copy()
        initial.append(p)
    return initial

def distance_to_cities():
    dis = []
    for i in range(num_city):
        dis_city = []
        for j in range(num_city):
            d = math.sqrt(pow(location[i][0]-location[j][0],2)+pow(location[i][1]-location[j][1],2))
            dis_city.append(d)
        dis.append(dis_city)

    return dis

# 适应度函数计算
def compute_adp(dis,initial):
    dis_adp = []
    for i in range(num_total):
        d = 0
        for j in range(num_city-1):
            d = dis[initial[i][j]][initial[i][j+1]] + d
        d = dis[initial[i][num_city-1]][initial[i][0]] + d
        dis_adp_city = 10000.0/d
        dis_adp.append(dis_adp_city)
    return dis_adp

# 中间计算
def choose_from_last(dis_adp,answer_source):
    mid_adp = []
    mid_adp_city = 0
    for i in range(num_total):
        mid_adp_each = dis_adp[i] + mid_adp_city
        mid_adp.append(mid_adp_each)
        # print(mid_adp)
        # 产生0-mid_adp[num_total-1]之间的随机数
        # 选择n-1<随机数<n的那个n的解,保留
    copy_ans = []
    for p in range(copy_num):
        rand = random.uniform(0, mid_adp[num_total - 1])  # 产生随机数
        # print(rand)
        # print(p)
        for j in range(num_total):
            if (rand < mid_adp[j]):  # 查找位置
                copy_ans.append(answer_source[j])
                break
            else:
                continue
    return copy_ans

# 交叉函数
def cross_pronew(copy_ans):
    for i in range(cross_num):
        choice = random.randint(0,copy_num-1)
        cross_list = copy_ans[choice].copy()
        while(cross_list in copy_ans):
            p = random.randint(0,num_city-1)
            q = random.randint(0,num_city-1)
            cross_list[p],cross_list[q] = cross_list[q],cross_list[p]
            m = random.randint(0,num_city-1)
            n = random.randint(0,num_city-1)
            cross_list[m],cross_list[n] = cross_list[n],cross_list[m]
        copy_ans.append(cross_list)
    cross_ans = copy_ans.copy()
    return cross_ans

#随机选择那95中的5个进行变异
def var_pronew(cross_ans):
    for i in range(var_num):
        which=random.randint(0,copy_num+cross_num-1)#选择对那个解交叉
        var_list=cross_ans[which].copy()
        while (var_list in cross_ans):
            p=random.randint(0,num_city-1)
            q=random.randint(0,num_city-1)
            var_list[p],var_list[q]=var_list[q],var_list[p]#交换位置
        cross_ans.append(var_list)
    var_ans=cross_ans.copy()
    return var_ans


answer_source = generate_initial()
dis = distance_to_cities()
print(dis)
# print(dis)
dis_adp = compute_adp(dis,answer_source)
Max_adp = max(dis_adp)
# print(dis_adp)
# copy_answer = choose_from_last(dis_adp,answer_source)
# cross_answer = cross_pronew(copy_answer)
# var_answer = var_pronew(cross_answer)
if (max(dis_adp)>10000/550):
    print('找到的最近距离是：',10000/max(dis_adp))

else:
    print('哎呀没找到，我再找找~')
    answer_new=answer_source
    dis_adp_new=dis_adp
    times = 1
    while(Max_adp<=10000/550):
        times = times + 1
        copy_answer=choose_from_last(dis_adp_new,answer_new)
        cross_answer=cross_pronew(copy_answer)
        var_answer=var_pronew(cross_answer)
        answer_new=var_answer.copy()
        # print(len(answer_new))
        dis_adp_new=compute_adp(dis,answer_new)
        Max_adp=max(dis_adp_new)
#        dis_min=10000/adp_max_new
#        print('这次是：',dis_min)


    dis_min=10000/Max_adp
    print('终于找到你啦：',dis_min)
    print(times)
