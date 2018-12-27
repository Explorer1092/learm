# coding:utf-8

import request
import unittest
class Case(unittest.TestCase):
#方法里面才有self，函数里面没有self
 u'''测试类描述'''
 def setUp(self):
  pass
 print("-----前置条件-----")
 def tearDown(self):
  pass
 print('----后置条件------')
 def test_001(self):
  u'''正常用例'''
  pass
  self.assertTrue(True)
 def test_002(self):
  u'''异常用例'''
  pass
  self.assertTrue(False)
if __name__ == "__main__":
 unittest.main()
