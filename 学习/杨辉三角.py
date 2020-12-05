def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]
        #return 'done'   错误
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)

#星号三角形
N = int(input())
for i in range((N+1)//2):
    print(('*'*((i+1)*2-1)).center(N))