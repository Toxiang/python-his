from numpy import array,exp,random,dot

x=array([[0,1,1],[1,1,1],[1,0,1],[0,1,1]])
y=array([[0,1,1,0]]).T

w = random.random((4,2))
print(w)

# 设置随机权重
random.seed(1)
weights = 2 * random.random((3,1))-1

for i in range(10000):
    z = dot(x,weights) #dot矩阵相乘

    yout = 1/(1+exp(-dot(x,weights)))

    e = 1/2*(y - yout)*(y-yout)
    # error*斜率
    slope = (y-yout) * (1-yout)#斜率
    delta = yout*slope

    # 更新权重
    weights += dot(x.T,delta)

print(weights)
test = [1,1,1]
print(1/(1+exp(-dot([test],weights))))
print(exp(2))

