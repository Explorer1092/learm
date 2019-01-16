import requests
import settings
class Get_token():
    def get_token(self):
        url = settings.base_url+'/api/gw/api/v1/account/admin_login'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
        data = {
            'password': '!mgt9012',
            'username': 'lvzhimeng@vipkid.com.cn',
            'kaptcha': '1234'
        }
        s = requests.post(url,headers,data)
        s = s.json()
        token = s['data']['token']
        print("create token:", token)
        return token
if __name__ == '__main__':
    l = Get_token()
    l.get_token()