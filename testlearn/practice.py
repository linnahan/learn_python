import json
import unittest
from parameterized import parameterized

from tools import add

with open("a.json","r",encoding="utf-8") as f:
    data = json.load(f)
class TestAdd(unittest.TestCase):
    @parameterized.expand(data)
    def test_add(self,a,b,expect):
        print(f"a:{a} b:{b} expect:{expect}")
        self.assertEqual(expect,add(a,b))

if __name__ == '__main__':
    unittest.main()