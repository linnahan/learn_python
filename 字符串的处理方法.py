#字符串的处理方法

#切割指定元素（变列表)
str = 'I\'m a student'
split = str.split(' ')
print(split)

#每个元素中间增加
str = '我是fsg651'
join = ' '.join(str)
print(join)

#去除首位不要的元素
str = '   aa d呵呵dd '
strip = str.strip(' ad')
print(strip)

#记录字符串中‘字符(串)’的出现次数
str = 'gedefgegeef'
count = str.count('ge')
print(count)

#把字符串中的某段字符串换成别的
str = '你是SB'
replace = str.replace('SB','大帅B')
print(replace)

#把字符串格式化输出
str = '哈哈哈'
foramt = '{0:*^20}'.format(str)    #高级实用
print(foramt)