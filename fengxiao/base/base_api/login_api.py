# coding:utf-8
import requests
import json
from base.request_list import Request_list
import settings
class Login():
    def login(self):
        base_url = settings.base_url
        url = base_url+'/api/gw/api/v1/account/admin_login'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}

        data = {
            'password':'!mgt9012',
            'username':'lvzhimeng@vipkid.com.cn',
            'kaptcha':'1234'
        }
        s = requests.post(url,data,headers)
        print(s.content.decode())
        return s
if __name__ == '__main__':
    l = Login()
    r = l.login()

