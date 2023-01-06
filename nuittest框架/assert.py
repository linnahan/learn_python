import unittest

class  TextAssert(unittest.TestCase):
    def text_equal1(self):
        self.assertEqual(10,10) # 用例通过
    def text_equal2(self):
        self.assertEqual(10,11) # 用例不通过
    def text_in1(self):
        self.assertIn("admin","欢迎admin") # 包含 通过

