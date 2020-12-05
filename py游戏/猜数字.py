#-*-coding:gbk-*-
from random import randint
num = randint(1,100)
count = 0
print('猜数字')
while True:
    answer = int(input())
    count += 1
    if num > answer:
        print('%d太小了！'%answer)
    elif num < answer:
        print('%d太大了！'%answer)
    else:
        print('正确！！！%d是答案'%num)
        break
print('一共答了%d次。'%count)
