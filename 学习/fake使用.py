import faker

a = faker.Faker("zh-CN")
print(a.name())     # 伪造姓名
print(a.random_int(25,40)) # 随机数
print(a.date_between(start_date = "-10y", end_date = "today").strftime('%Y年%m月%d日')) #伪造日期
print(a.address()) # 伪造地址
print(a.ssn()) # 伪造身份证
print(a.credit_card_number())   # 伪造信用卡号
print(a.email()) # 伪造电子邮箱
print(a.phone_number()) # 伪造手机号码
print(a.password()) # 伪造密码
print(a.company()) # 伪造公司名
print(a.job())  #  伪造职业
print(a.url())  # 伪造url
print(a.uri())  # 伪造uri
print(a.text()) # 伪造文本
print(a.address()[:-6]) # 伪造地址
