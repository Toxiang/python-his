import numpy as np
a = np.array([1,2,3,4,5])
print(a)

import time
a=np.random.rand(1000000)
b=np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print("向量化:"+str(1000*(toc-tic)))

tic = time.time()
for i in range(1000000):
    c += a[i]+b[i]
toc = time.time()
print("for循环:"+str(1000*(toc-tic)))