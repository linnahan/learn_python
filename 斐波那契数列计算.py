def fbi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbi(n-1) + fbi(n-2)

n = eval(input())
print(fbi(n))