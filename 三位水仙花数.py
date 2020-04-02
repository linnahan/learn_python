#1
s = ''
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            S = i*100+j*10+k
            if i**3+j**3+k**3 == S:
                s += '{},'.format(S)
print(s[:-1])

#2
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])