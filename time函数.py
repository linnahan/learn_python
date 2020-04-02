import time
import datetime

#start = time.perf_counter()
print(time.time())
print(time.ctime())
print(time.gmtime())
#print('{:.6f}'.format(time.perf_counter()-start))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))   #gmtime为UTC时区（0时区），我们为东八区
#time.sleep(0.5)
#print(time.ctime()[11:-5])
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))