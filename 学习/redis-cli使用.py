import redis
# redis.ConnectionPool(host='192.168.0.222', port=6379, decode_responses=True)
r = redis.StrictRedis(host='192.168.0.222', password="123456",port=6379, decode_responses=True)
r.set('name', 'xiaoqian', ex=3)  # 设置过期时间为3秒
print(r.get('name'))  # xiaoqian
