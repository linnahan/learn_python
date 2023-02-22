import pymongo,csv

myclient = pymongo.MongoClient('mongodb://192.168.0.222:27017/')    # 连接数据库
print(myclient.list_database_names())   # 打印数据库名字
mydb = myclient["the_way_to_flask"]     # 创建数据库
mycol = mydb["spider"]       # 创建集合(数据表)
# mydb = myclient.runoobdb    # 连接数据库
# mycol = mydb.spider     # 连接表

def oneinsert():
    '''增'''
    mycol.insert_one({'num': 123456,'name':'lnh'})     # 插入一个文档(记录)
def manyinsert():
    with open(r'D:\gitlearn\learn_python\data\b.csv','r',encoding='gbk') as f:
        dic = csv.DictReader(f)
        manydic = [d for d in dic]
        mycol.insert_many(manydic)  # 插入多个记录[{}]

def update():
    '''改'''
    mycol.update_many({'style':'都市言情'},{'$set':{'style': '色情刺激'}})

def dell():
    '''删除符合条件的记录'''
    mycol.delete_many({'name':'lnh'})

def find():
    '''查询表'''
    result = mycol.find()
    for re in result:
        print(re)

if __name__ == '__main__':
    manyinsert()