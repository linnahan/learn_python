#1
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A'<=c<='Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)

#2
inp=input()

l=len(inp)
#主要用到的就是chr和ord
#chr把ascii转为str
#ord把str转为ascii
for i in range(l):
    if ord('A') <=ord(inp[i])<=ord('Z'):
        onew=ord('A')+((ord(inp[i])-ord('A'))+3)%26
    elif ord('a') <=ord(inp[i])<=ord('z'):
        onew=ord('a')+((ord(inp[i])-ord('a')) + 3 )%26
    else:
        onew = ord(inp[i])
    new=chr(onew)
    print(new,end='')
