import unittest
from htmltestreport import HTMLTestReport
from nuittest框架.testcase import TestDemo

'''测试报告'''
# 套件
suite = unittest.TestSuite()
suite.addTest(TestDemo("test_method1"))
# 运行
runner = HTMLTestReport("./test_report1.html","测试","无")
runner.run(suite)
