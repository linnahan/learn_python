def prime(m):
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False
    return True


n = eval(input())
if n != int(n):
    n = int(n) + 1
else:
    n = int(n)
i = 5
while i > 0:
    if prime(n):
        if i > 1:
            print(n, end=",")
        else:
            print(n, end="")
        i -= 1
    n += 1