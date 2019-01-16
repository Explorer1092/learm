#coding:utf-8
import unittest
from base.base_api.save_knowledge import Save_knowledge
from base.base_api.save_material import Save_material
from base.base_api.delete_material import Delete_material
from base.base_api.delete_knowledge import Delete_knowledge
from base.databuild import Mysql_db
from base.base_api.saveOrUpdate import SaveOrUpdateApi
class SaveOrUpdate(unittest.TestCase):
    def setUp(self):
        m = Save_material().save_material()
        self.materialid = m.json()["data"]["id"]
        k = Save_knowledge().save_knowledge(self.materialid)
        self.knowledgeid = k.json()["data"]["id"]
    def test_003(self):
        s = SaveOrUpdateApi().saveOrUpdateApi(self.materialid,self.knowledgeid)
        s = s.json()
        mes = s['message']
        self.assertEqual(mes, "请求成功")
    def tearDown(self):
        sql = "delete from question order by id desc limit 1"
        dq = Mysql_db().delete_data(sql)
        kd = Delete_knowledge().delete_knowledge(self.knowledgeid)
        md = Delete_material().delete_material(self.materialid)
