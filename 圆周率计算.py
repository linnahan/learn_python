#蒙特卡洛方法
from random import random
from progress_bar import progress_bar

num = 1000000
hits = 0
for i in range(num):
    x,y = random(),random()
    if pow(x**2+y**2, 0.5) <= 1:
        hits += 1
    progress_bar(num)
print((hits/num)*4)

#公式法
pi = 0
for i in range(10):
    pi += 1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print(pi)