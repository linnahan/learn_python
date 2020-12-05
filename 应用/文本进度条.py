import time


def progress_bar(i):
    print('开始执行'.center(i+5,'='))
    for j in range(i+1):
        ok,no = chr(9608)*j,' '*(i-j)
        print('\r{:^4.2%}|{}{}|'.format(j/i,ok,no),end='')
        time.sleep(0.3)
    print('\n'+'结束执行'.center(i+5,'='))

if __name__ == '__main__':
    progress_bar(20)

