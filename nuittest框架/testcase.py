import unittest

class TestDemo(unittest.TestCase):  # 右键运行
    '''方法用test开头'''
    def test_method1(self):
        print("测试通过")

if __name__ == '__main__': # 直接运行
    unittest.main()