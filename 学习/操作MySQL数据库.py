import pymysql


db = pymysql.connect(host="192.168.0.222",
                     user="root",
                     port=3306,
                     password="123456",
                     database='test01',
                     charset="gbk")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select Cno,Cname from course")
# 使用 fetchone() 方法获取单条数据.
onedata = cursor.fetchone()
# 使用 fetchmany() 方法获取所有数据.
manydata = cursor.fetchmany(2)
# 使用 fetchall() 方法获取所有数据.
data = cursor.fetchall()
print(onedata)
print(manydata)
print(data)

# 创建数据库
cursor.execute("create database if not exists test02")
# 切换数据库
db.select_db("test02")
# 创建表单
cursor.execute("create table spider (id int NOT NULL AUTO_INCREMENT,name varchar(20) character set gbk,PRIMARY KEY (id))")
# 插入一条数据
cursor.execute("insert into spider(name)values ('朱文杰') ")
db.commit() # 插入和修改要对数据库进行提交操作
# 删除表单
# cursor.execute("drop table spider")
# 删除数据库
# cursor.execute("drop database if exists test02")
# 展示数据库
cursor.execute("show databases")
database = cursor.fetchall()
print(database)

# 关闭数据库连接
db.close()
