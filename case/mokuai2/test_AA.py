# coding utf-8
import unittest


class Case(unittest.TestCase):
#方法里面才有self，函数里面没有self
 def setUp(self):
  pass
 def tearDown(self):
  pass
 def test_aa(self):
  pass
  self.assertTrue(True)
 def test_bb(self):
  pass
  self.assertTrue(True)
if __name__ == "__main__":
 unittest.main()