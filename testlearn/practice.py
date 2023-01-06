import unittest

from testlearn.tools import add


class TestDemo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2,add(1,1))
    def test_2(self):
        self.assertEqual(4,add(1,2),"哈哈哈哈")
    def test_3(self):
        self.assertEqual(7,add(3,4))
    def test_4(self):
        self.assertEqual(9,add(4,5),"呵呵呵呵呵")
