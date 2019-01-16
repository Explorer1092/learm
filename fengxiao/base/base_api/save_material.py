# coding:utf-8
from base.request_list import Request_list
class Save_material(Request_list):
    def save_material(self):
        self.url = "/api/gw/api/v1/material/save"
        self.data = {"type":0,"stage":0,"unitStage":"1","textbookId":1,"levelId":2,"sequence":"0","name":"测试","introduction":"这是课程简介"}
        s = self.post(self.data)
        print(s.content.decode())
        return s
if __name__ == "__main__":
    c = Save_material()
    s = c.save_material()

