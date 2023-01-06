import unittest,time


'''测试夹具'''
class TestLogn(unittest.TestCase):
    def setUp(self) -> None:
        print("2.打开网页")
    def tearDown(self) -> None:
        print("4.关闭网页")
    @classmethod
    def setUpClass(cls) -> None:
        print("1.打开浏览器")
    @classmethod
    def tearDownClass(cls) -> None:
        print("5.关闭浏览器")
    def test_1(self):
        print("3.输入用户名密码aaa")
    def test_2(self):
        print("3.输入用户名密码bbb")
