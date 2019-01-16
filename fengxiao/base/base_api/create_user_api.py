# coding:utf-8
import requests
from common import get_nowdate
from base.request_list import Request_list

class Create_user(Request_list):
    def __init__(self):
        super(Create_user, self).__init__()
        now_time = get_nowdate.get_nowdate()
        self.acount = now_time+'@vipkid.com.cn'
        print(self.acount)
    def create_user(self):
        self.url = '/api/gw/api/v1/account/createAccount'
        self.data = {"accountType":"STAFF","email":self.acount,"roleId":1}
        # print(data)
        s = self.post(self.data)
        print(s.content)
        return s

if __name__ == '__main__':
    c = Create_user()
    r = c.create_user()