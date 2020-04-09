ls = ['中国','美国','日本']
w = open('ss.txt','w+',encoding='utf-8')        #统一编码utf-8避免错误
w.write(' '.join(ls))
print(w)
w.seek(0)
print(w.read())