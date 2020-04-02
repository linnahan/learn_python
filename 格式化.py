#整数格式化
print(format(8888,'0<10d'))
print(format(8888,'0>10d'))
print(format(8888,'*^10d'))
#浮点数格式化
print(format(15.6856,'.2f'))
print(format(43.98414,'.0f'))
#字符串格式化
print(format('hhhh','*^10'))


a = 123789.456
print('{0:-^20,.2f}'.format(a))     #高级实用

#格式化代入
thing ='lights'
number =50
money =999.88
print('%d %s are %f yuan'%(number,thing,money))