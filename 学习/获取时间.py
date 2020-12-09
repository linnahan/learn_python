#获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)
#获取指定日期和时间
dt = datetime(1998,8,12,12,0)
print(dt)

'''在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的
时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。'''
print(now.timestamp())
print(dt.timestamp())

#str转换为datetime
cday = datetime.strptime('1998-8-12 12:0:0', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))