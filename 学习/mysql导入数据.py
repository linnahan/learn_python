from 学习.小工具 import Easymysql
import pymysql,csv

# 创建mysql连接
db = pymysql.connect(host='192.168.0.222', user='root', password='123456', database='mysql', charset='utf8')
user = Easymysql(db)
user.execute("create database test02")  # 创建数据库
db.select_db('test02')  # 切换数据库
user.create_table('spider',encoding='utf8',style = 'varchar(20)',       # 创建表
                  title = 'varchar(50)',title_href = 'varchar(100)',
                  autor = 'varchar(30)',autor_href = 'varchar(100)')
with open(r'D:\gitlearn\learn_python\data\b.csv','r',encoding='gbk') as f: # 打开文件
    data = csv.DictReader(f)  # data为字典生成器
    user.writemany(table='spider',manydata=data)