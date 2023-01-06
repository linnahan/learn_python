import unittest,json
from parameterized import parameterized
from nuittest框架.all.app import *
from nuittest框架.all.tools import login


class TestLogn(unittest.TestCase):
    @parameterized.expand(build_add_data())
    def test_1(self,case,name,pd,expect):
        print(f"用例：{case} 用户名：{name} 密码：{pd} 期望结果：{expect}")
        self.assertEqual(expect,login(name,pd))
if __name__ == '__main__':
    unittest.main()