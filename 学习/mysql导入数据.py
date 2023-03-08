from learn_python.base.小工具 import Easymysql
import pymysql,csv,faker

# 创建mysql连接
db = pymysql.connect(host='192.168.0.222', user='root', password='123456', charset='utf8')
user = Easymysql(db)
# user.execute("create database test05")  # 创建数据库
# db.select_db('test05')  # 切换数据库
# user.create_table('spider',encoding='utf8',style = 'varchar(20)',       # 创建表
#                   title = 'varchar(50)',title_href = 'varchar(100)',
#                   autor = 'varchar(30)',autor_href = 'varchar(100)')
# with open(r'D:\gitlearn\learn_python\data\b.csv','r',encoding='gbk') as f: # 打开文件
#     data = csv.DictReader(f)  # data为字典生成器
#     user.writemany(table='spider',manydata=data)

'''伪造数据'''
db.select_db('test02')  # 切换数据库
user.create_table('faker',encoding='utf8',name = 'varchar(20)',       # 创建表
                  born = 'date',phone = 'bigint(50)',address = 'varchar(100)',
                  job = 'varchar(30)',email = "varchar(50)")
data = []
f = faker.Faker("zh-CN")
for i in range(10000):
    onedata = dict(name = f.name(),born = f.date_between(start_date = "-60y", end_date = "-18y").strftime('%Y-%m-%d'),
                   phone = f.phone_number(),address = f.address()[:-6], #%Y年%m月%d日
                  job = f.job(),email = f.email())
    data.append(onedata)
user.writemany(table='faker',manydata=data)