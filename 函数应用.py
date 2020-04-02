def compare(num1,num2):
    if num1>num2:
        print('too big')
        return False
    elif num1<num2:
        print('too small')
        return False
    else:
        print('bingo')
        return True
from random import randint
num=randint(1,100)
print('guess number?')
bingo=False
while bingo==False:
    answer=int(input())
    bingo=compare(answer,num)
