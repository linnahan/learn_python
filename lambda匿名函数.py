sum=lambda x,y:x+y
print(sum(5,9))

def fn(x):
    return lambda y:x+y
a=fn(8)
print(a(6))