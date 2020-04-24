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
#文章出现最多的词
#自己
'''import jieba

wz = []
a = open('沉默的羔羊.txt',encoding='utf-8')
for i in a.read():
    if i >= u'\u4e00' and i <= u'\u9fa5':
        wz.append(i)
file = ''.join(wz)

fen = jieba.lcut(file)
dic = {}
for i in fen:
    dic[i] = dic.get(i,0) + 1
lis = sorted(dic.items(),key=lambda x:x[1],reverse=True)
for i in lis:
    if len(i[0]) > 2:
        print(i[0])
        break'''
#网上
'''import jieba

f=open('沉默的羔羊.txt','r',encoding='utf-8')
sp=f.read()
words=jieba.lcut(sp)
lis={}
for word in words:
    if(len(word)>=2):
        lis[word]=lis.get(word,0)+1
count=list(lis.items())
count.sort(key=lambda x:x[1],reverse=True)
print(count[0][0])'''