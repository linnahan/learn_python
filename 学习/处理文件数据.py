file=open('scores.txt')
results = []
lines=file.read()
file.close()
for line in lines:
    data=line.split()
    sum = 0
    for score in data[1:]:
        sum+=int(score)
    result="%s\t:%d\n"%(data[0],sum)
    results.append(result)
output=open('result.txt','w')
output.writelines(results)
output.close()