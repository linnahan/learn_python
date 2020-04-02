def Sort(L) :
    i = 0
    while i<len(L)-1:
        for j , value in enumerate(L[i + 1 :]) :
            if L[i] > value :
                L[i + j + 1] = L[i]
                L[i] = value
            else:
                continue
        i+=1
    return(L)
print(Sort([4,5,3,2,1,1]))
print(Sort([2,5,3,7,4,2]))

#另一种


def new_order(list):
    for i in range(len(list)-1):
        for j in range(0,len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
liebiao= [6,9,1,4,5]
print(new_order(list=liebiao))

'''
def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range( 0,n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        # if list[i] > list[i + 1]:
        #     list[i], list[i + 1] = list[i + 1], list[i]
    print(list)
list=[2,4,6,8,1,3,5,7,9]
bubble_sort(list)
'''