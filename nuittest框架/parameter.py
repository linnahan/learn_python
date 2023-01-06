import unittest
from parameterized import parameterized
def add(a,b):
    return a + b

'''参数化'''
data = [(1,2,3),(2,8,10),(3,5,9),(2,4,6)]
class TestAdd(unittest.TestCase):
    @parameterized.expand(data)
    def test_add(self,a,b,expect):
        print(f"a:{a} b:{b} expect:{expect}")
        self.assertEqual(expect,add(a,b))
if __name__ == '__main__':
    unittest.main()