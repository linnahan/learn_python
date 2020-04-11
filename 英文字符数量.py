f = open('latex.log')
dic = {}
count = 0
for i in f.read():
    if i in 'qwertyuiopasdfghjklzxcvbnm':
        dic[i] = dic.get(i,0)+1
    #if i != ' ' and i != '\n':
    count += 1
ls = sorted(dic.items(),key=lambda x:x[0])
print('共{}字符'.format(count),end='')
for i in ls:
    print(',{}:{}'.format(i[0],i[1]),end='')
