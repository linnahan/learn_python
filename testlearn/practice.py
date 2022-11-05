import random


num = int(random.randrange(1,100))
try:
    guest = int(input("猜数字（1-100）："))
    i = 0
    while 1 :
        i += 1
        if guest == num:
            print('正确，结果是%d,一共猜了%d次'%(num,i))
            break
        if guest < num:
            print('小了')
        elif guest > num:
            print('大了')
        guest = int(input('请继续猜：'))
except ValueError:
    print('输入数字啊，沙鸟')
