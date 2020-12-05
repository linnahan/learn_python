a = [65,94,51,95,24]
b = [65,-94,51,95,-24]
c = ['Credit','about','Zoo','bob']

#sorted能实现排序
print(sorted(a))
print(sorted(b))
print(sorted(b,key=abs))
print(sorted(b,key=abs,reverse=True))
print(sorted(c,key=str.lower))

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]
L2 = sorted(L,key=by_name)                      #按名字排序
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)       #按成绩从高到低排序
print(L2)