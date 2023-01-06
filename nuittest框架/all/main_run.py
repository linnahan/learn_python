import unittest
from htmltestreport import HTMLTestReport
from nuittest框架.all.app import BASE_DIR
from nuittest框架.all.case.login_test import TestLogn

suite = unittest.TestLoader().discover(BASE_DIR+"\case","login_test.py")
runner = HTMLTestReport(BASE_DIR+"/report/loginTestReport.html","测试登录","无")
runner.run(suite)
