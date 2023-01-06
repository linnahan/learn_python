import unittest,json
from parameterized import parameterized
from nuittest框架.all.app import BASE_DIR
from nuittest框架.all.tools import login




data = []
with open(BASE_DIR+"/data/logindata.json","r",encoding= "utf-8") as f:
    da = json.load(f)
    for a,b in da.items():
        data.append((a,b[0],b[1],b[2]))
class TestLogn(unittest.TestCase):
    @parameterized.expand(data)
    def test_1(self,case,name,pd,expect):
        print(f"用例：{case} 用户名：{name} 密码：{pd} 期望结果：{expect}")
        self.assertEqual(expect,login(name,pd))
if __name__ == '__main__':
    unittest.main()