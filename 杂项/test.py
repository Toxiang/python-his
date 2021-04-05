import math
import numpy as np
import random
# 19.计算质数
def compute_prime(number):
    res = []
    for i in range(2,number+1):
        res.append(i)
        for j in range(2,int(math.sqrt(i))+1):
            # print("i:",i," ","j:",j)
            if(i%j==0):
                res.pop()
                break
    return res


# 18.筛选列表
def compute_list_prime(l):
    res = []
    if(l.count(1)==1): l.remove(1)
    for i in l:
        res.append(i)
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                res.pop()
                break
#     计算质数和
    count = 0
    res.sort()
    for i in range(0,len(res)-1):
        num1 = res[i]
        for j in range(i+1,len(res)):
            num2 = res[j]
            if (res.count(num1 + num2) == 1):
                # print(num1, num2, num1 + num2)
                count = count + 1
    print(count)
    return count
    #下面循环和上面效果一样 上面的更快
    # for num1 in res:
    #     for num2 in res:
    #         # print("num1:",num1,"num2:",num2)
    #         if(res.count(num1+num2)==1):
    #             print(num1,num2,num1+num2)
    #             count = count+1
    # return count/2

#22.矩阵
def create_matrix():
    mat = np.random.rand(4,4)
    np.matrix(mat)
    print(mat)
    mat = mat.T
    print(mat)






if __name__ == '__main__':
    #18.测试
    number = 500
    res = compute_prime(500)
    count = 0
    for i in res:
        print(i,end=" ")
        count = count + 1
        if(count==5):
            print(end='\n')
            count=0

    #19.测试
    #测试用 l为测试列表
    l = []
    for i in range(1,501):
        l.append(i)
    count_add = compute_list_prime(l)

    #22.测试
    create_matrix()

