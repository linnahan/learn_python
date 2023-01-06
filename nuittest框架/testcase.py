import unittest

a = 50
class TestDemo(unittest.TestCase):  # 右键运行
    '''方法用test开头'''
    def test_method1(self):
        print("测试通过1")
    '''直接将测试函数标记成跳过'''
    @unittest.skip('跳过的原因')
    def test_skip1(self):
        print("测试通过2")
    '''根据条件判断测试函数是否跳过'''
    @unittest.skipIf(a > 30,"a大于30就跳过")
    def test_skip2(self):
        print("测试通过3")

if __name__ == '__main__': # 直接运行
    unittest.main()