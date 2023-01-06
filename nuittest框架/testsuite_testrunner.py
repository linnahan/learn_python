import unittest
from nuittest框架.testcase import TestDemo
# 实例化套件对象


suite = unittest.TestSuite()

# 添加用例方法
#suite.addTest(TestDemo("test_method1")) # 发法
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemo)) # 类

# 实例化对象
runner = unittest.TextTestRunner()

# 执行
runner.run(suite)

