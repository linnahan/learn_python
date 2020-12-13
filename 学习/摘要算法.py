#摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
import hashlib


#demo:MD5算法
'''MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。'''
md5 = hashlib.md5()
md5.update('我是你爸'.encode('UTF-8'))
md5.update('.'.encode('UTF-8'))
print(md5.hexdigest())

#demo:SHA1算法
'''SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。'''
sha1 = hashlib.sha1()
sha1.update('我是你妈'.encode('UTF-8'))
sha1.update('.'.encode('UTF-8'))
print(sha1.hexdigest())

'''比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。'''


'''由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：'''
def calc_md5(password):
    return get_md5(password + 'the-Salt')
'''经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，
这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？
如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。'''
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())

