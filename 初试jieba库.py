import jieba


a = open('xiaohua.txt',encoding='utf-8').read()
print(type(a))
for i in '，,。/；‘、=-·~！@#￥%……&*（） ：“$《》？”^\n1234567890':
    a = a.replace(i , '')

b = jieba.lcut(a)
#print(b)
dic = {}
for i in b:
    dic[i] = dic.get(i,0) + 1
lis = sorted(dic.items(),key=lambda x:x[1],reverse=True)
for i in range(100):
    print('{}:{}'.format(lis[i][0],lis[i][1]))