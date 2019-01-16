#coding:utf-8
from base.request_list import Request_list
class Delete_material(Request_list):
    def delete_material(self,materialid):
        self.url = "/api/gw/api/v1/material/delete"
        self.data = {"id":materialid}
        s = self.post(self.data)

        return print('删除成功')
if __name__ == "__main__":
    s = 622
    d = Delete_material()
    s = d.delete_material(s)