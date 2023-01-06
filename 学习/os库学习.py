import os

# 路径操作
print(os.path.abspath('LICENSE'))  # 返回path在当前系统中的绝对路径
print(os.path.normpath('///'))  # 归一化path的表示形式
print(os.path.relpath('LICENSE'))  # 返回当前程序与文件之间的相对路径
print(os.path.basename('LICENSE'))  # 返回文件名
print(os.path.dirname('abs\\zzzz\\LICENSE'))  # 返回文件路径
print(os.path.exists('LICENSE'))  # 路径存在则返回True,路径损坏返回False
print(os.path.isfile('LICENSE'))  # 判断路径是否为文件
print(os.path.isdir('LICENSE'))  # 判断路径是否为目录
print(os.path.islink('LICENSE'))  # 判断路径是否为链接
print(os.path.getatime('LICENSE'))  # 返回最后一次进入此path的时间。
print(os.path.getmtime('LICENSE'))  # 返回在此path下最后一次修改的时间。
print(os.path.getsize('LICENSE'))  # 返回path的大小,字节为单位
print(os.path.getctime('LICENSE'))  # 返回文件或目录创建时间

# 进程管理
# os.system('C:\\Windows\\system32\\calc.exe')

# 环境参数
os.chdir('D:')  # 修改当前程序操作的路径
print(os.getlogin())  # 获得当前系统登录的信息
print(os.getcwd())  # 返回程序的当前路径
print(os.cpu_count())  # 返回程序当前系统的CPU数量
print(os.urandom(10))  # 获得n个字节长度的随机字符串，通常用于加解密运算
