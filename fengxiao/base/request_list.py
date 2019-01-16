# coding:utf-8
import requests
import settings
from base.get_token import Get_token
class Request_list(object):
    def __init__(self):
        self.url = ''
        self.token = Get_token().get_token()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0","Authorization":self.token}
        self.base_url = settings.base_url
        # print(self.base_url)
        # print(self.headers)
        # print('=================')
    def get(self):
        print("request:", self.headers)
        r = requests.get(url=self.base_url+self.url,headers=self.headers)
        # print(r.text)
        # print(r.status_code)
        return r

    def post(self,data):
        print('----------------')
        print("request:", self.headers)
        r = requests.post(url = self.base_url+self.url,headers = self.headers,json =data )
        # print(r)
        return r

    def delete(self):
        r = requests.delete(url = self.base_url+self.url,headers = self.headers)
        return r

# if __name__=="__main__":
#     a = Request_list()
#     a.url="https://test3-mgt.vipfengxiao.com/api/gw/api/v1/account/admin_login"
#     data = {
#             'password':'lvzhimeng',
#             'username':'lvzhimeng@vipkid.com.cn',
#             'kaptcha':'1234'
#         }
#     r = a.post(data)
#     print(r.content)
