import numpy as np
import math
import random
import time

# 经过多次实验 缺点 不够稳定
# 41 94 37 84 54 67 25 62  7 64  2 99 68 58 71 44 54 62 83 69 64 60 18 54 22 60 83 46 91 38
# 25 38 24 42 58 69 71 71 74 78 87 76 18 40 13 40 82  7 62 32 58 35 45 21 41 26 44 35  4 50

num_city = 30 #the number of city
T_Max = 120 # initial T
lowest_T = 0.01 # the lowest T
M = 150 # change the status
iteration = 5000 # the times of iteration

location = np.loadtxt('city.txt')
location = location.T

# matrix: the dic of two cities
def distance_two_cities():
    dis = [] # 距离矩阵
    for i in range(30):
        dis_city = [] # 第i个城市到其他城市的距离
        for j in range(30):
            d = math.sqrt(pow(location[i][0]-location[j][0],2)+pow(location[i][1]-location[j][1],2))
            dis_city.append(d)
        dis.append(dis_city)
    return dis

# compute the distance of all the paths
# def cal_newpath(dis_mat,path):
#     dis=0
#     for j in range(num_city-1):
#         dis=dis_mat[path[j]][path[j+1]]+dis
#     dis=dis_mat[path[29]][path[0]]+dis#回家
#     return dis
def compute_path(dis,path):
    d = 0
    for j in range(num_city-1):
        d = dis[path[j]][path[j+1]]+d
    d = dis[path[num_city-1]][path[0]]+d # 最后一条路返回起点
    return d

# 初始化
dis = distance_two_cities()
# 路径
path = list(range(30))
#初始第一条路
d = compute_path(dis,path)
# 初始温度
T = T_Max

def main2(T,path,d):
    while(T > lowest_T):
        count_m = 0
        count_iter = 0
        while(count_m < M and count_iter < iteration):
            i = 0
            j = 0
            while(i==j):
                i = random.randint(1,29)
                j = random.randint(1,29)
            path_new = path.copy
            path_new[i],path_new[j] = path_new[j],path_new[i]
            d_new = compute_path(dis,path_new)
            dela = d_new - d

def main(T,path,d):
    times = 0
    while(T > lowest_T ):
        count_m = 0
        count_iter = 0
        while(count_m < M and count_iter < iteration):
            i = 0
            j = 0
            while(i == j):#防止访问同一个城市
                i = random.randint(1,29)
                j = random.randint(1,29)
            path_new = path.copy()
            path_new[i],path_new[j] = path_new[j],path_new[i] #交换两个城市坐标
            d_new = compute_path(dis,path_new)
            delta = d_new - d # new path 和 preious path
            # get a random number
            rand = random.random()
            # compute the number of function
            exp_d = math.exp(-delta/T)

            if delta < 0:
                path = path_new
                d = d_new
            elif exp_d > rand:
                path = path_new
                d = d_new
            else:
                count_m = count_m + 1
            count_iter = count_iter + 1
        T = 0.99 * T   #指数式下降
        # T = T_Max/(1+T) #
    d_min = d
    path_min = path
    print("最短距离：",d_min)
    print("最短路径：",path_min)
    return  d_min


if __name__ == '__main__':
    x=0
    start = time.clock()
    for i in range(50):
        x = x + main(T,path,d)
    x = x/50
    print("平均最短距离：",x)
    print("运行时间为：",time.clock()-start)
# 最短距离： 473.36277286229597
# 最短路径： [0, 27, 20, 5, 7, 16, 9, 11, 18, 26, 3, 1, 28, 14, 12, 17, 23, 25, 19, 21, 13, 4, 6, 10, 8, 22, 24, 29, 15, 2]
# 最短距离： 465.95396236014443
# 最短路径： [0, 2, 23, 25, 12, 17, 14, 28, 1, 11, 18, 26, 3, 19, 21, 13, 29, 4, 20, 5, 7, 9, 16, 6, 10, 8, 22, 24, 15, 27]
# 最短距离： 477.0670346194311
# 最短路径： [0, 2, 27, 15, 13, 21, 19, 25, 23, 17, 12, 14, 28, 1, 3, 26, 18, 11, 9, 16, 10, 8, 6, 7, 5, 20, 4, 29, 22, 24]
# 最短距离： 456.4071692824513
# 最短路径： [0, 2, 24, 22, 8, 10, 6, 16, 9, 7, 5, 20, 4, 29, 15, 27, 13, 21, 25, 19, 3, 26, 18, 11, 1, 28, 14, 12, 17, 23]



