#-*-coding:gbk-*-
from random import randint
num = randint(1,100)
count = 0
print('������')
while True:
    answer = int(input())
    count += 1
    if num > answer:
        print('%d̫С�ˣ�'%answer)
    elif num < answer:
        print('%d̫���ˣ�'%answer)
    else:
        print('��ȷ������%d�Ǵ�'%num)
        break
print('һ������%d�Ρ�'%count)
