import time
block = 20
ok = chr(9608)
no = ' '

def __bar(n):
    for i in range(1,n+1):
        ok_n = round(round(i/n,2) / 0.05)
        no_n = block - ok_n
        print('\r'+'{:^6.1%}|{}{}|'.format(next(_prop),ok*ok_n,no*no_n),end='')
        if i == n:
            print('\n'+'循环结束'.center(25,'='))
        yield

def __proportion(n):
    for i in range(1,n+1):
        scale = i/n
        yield scale

def __ti():
    a = 1
    while True:
        yield a
        a += 1

_c = __ti()

def progress_bar(num):
    global _prop
    global _a
    if next(_c) == 1:
        _a = __bar(num)
        _prop = __proportion(num)
    return next(_a)


if __name__ == '__main__':
    for i in range(99):
        progress_bar(99)
        time.sleep(0.2)