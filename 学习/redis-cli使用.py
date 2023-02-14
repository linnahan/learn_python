import redis

#连接池：避免每次建立、释放连接的开销。
pools = redis.ConnectionPool(host='192.168.0.222', password=123456,port=6379, decode_responses=True)
r = redis.StrictRedis(connection_pool=pools)

r.set('name', 'hhhh', ex=60, nx=True)  # 设置过期时间为60秒,nx=True表示不存在再set，xxx存在再set
print(r['name'])
print(r.get('name'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型
print(r.keys())     # 列出所有键
r.delete('test001')   #删除key为name得值
print(r.dbsize())    #查看库里有多少key
# r.save()   #强行把数据库保存到硬盘。保存时阻塞
# r.flushdb()   #删除当前数据库的所有数据

# 可以使用pipline实现一次请求指定多个命令
pipe = r.pipeline() # 创建一个管道
pipe.set('name', 'jack')
pipe.set('role', 'sb')
pipe.sadd('faz', 'baz', "bnz")
pipe.incr('num')    # 如果num不存在则vaule为1，如果存在，则value自增1
pipe.execute()