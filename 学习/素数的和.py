#第一种，自己想的
sum = 0
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sum += i
print(sum)

#第二种，网上
def prime(n):
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False
    return True

s = 0
for i in range(2, 100):
    if prime(i):
        s += i
print(s)