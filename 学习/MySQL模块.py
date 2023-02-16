# 导入MySQL驱动：
# import mysql.connector
import pymysql.connections


# 注意把password设为你的root口令：
# conn = mysql.connector.connect(user='root', password='123456aZ', database='test')
conn = pymysql.connect(user='root', password='123456', database='test02')

'''# 使用 cursor() 方法创建一个游标对象
cursor = conn.cursor()
# 如果表存在则删除
cursor.execute("drop table if exists user")
# 创建user表：
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s：
cursor.execute('insert into user (id,name) values (%s,%s)', ['1', 'Michael'])
cursor.rowcount
# 提交事务：
conn.commit()
conn.close()'''
# 运行查询：
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()