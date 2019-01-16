# # coding:utf-8
# import unittest
# import requests
# import json
# from base.base_api.login_api import Login
# class LoginTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#     def test001(self):
#         s = Login().login()
#         code = s.status_code
#         req = s.content
#         s = s.json()    #reponse对象转换成字典
#         print(type(s))
#         mes = s['message']  #用python中取字典value的方式取出message值
#         print(mes)
#         print (str(req,'utf-8'))  #返回中文乱码，对response进行转换
#         self.assertEqual(mes,"请求成功")
#         self.assertEqual(code,200)
#
