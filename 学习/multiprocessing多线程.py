import multiprocessing
from multiprocessing import dummy
import requests

# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

"""
参数介绍：

    1. group默认为None（目前未使用）
    2. target代表调用对象，即子进程执行的任务
    3. name为进程名称
    4. args调用对象的位置参数元组，args=(value1, value2, ...)
    5. kwargs调用对象的字典，kwargs={key1:value1, key2:value2, ...}
    6. daemon表示进程是否为守护进程，布尔值
　　 　

方法介绍：
　　Process.start() 启动进程，并调用子进程中的run()方法
　　Process.run() 进程启动时运行的方法，在自定义时必须要实现该方法
　　Process.terminate() 强制终止进程，不进行清理操作，如果Process创建了子进程，会导致该进程变成僵尸进程
　　Process.join() 阻塞进程使主进程等待该进程终止
　　Process.kill() 与terminate()相同
　　Process.is_alive() 判断进程是否还存活，如果存活，返回True
　　Process.close() 关闭进程对象，并清理资源，如果进程仍在运行则返回错误
　　
"""


def add(a):
    print("打印%d"%a)
a = dummy.Pool(10)
while True:
    a.map(add,[1,2,3,4,5,6,7,8,9,0])
