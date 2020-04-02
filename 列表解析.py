line_1=[1,5,2,9,4,7,8,6]
line_2=[]
for i in line_1:
    if i%2==0:
        line_2.append(i)
print(line_2)
line_3=[i for i in line_1 if i%3==0]
print(line_3)
print([i for i in range(1,101) if i%2==0 and i%3==0])    #要记得加[]号
print(";".join([str(i) for i in range(1,101) if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0]))
print([";".join([str(i) for i in range(1,101) if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0])][0])
print([":".join([str(i) for i in range(1,101) if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0])])


line_1[4]='gdf'
print(line_1)