from functools import reduce
print(list(map(lambda x,y:x+y,range(1,10),range(1,6))))
print(reduce(lambda x,y:x+y,range(1,101)))