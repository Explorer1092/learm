import unittest
from base.base_api.save_knowledge import Save_knowledge
from base.base_api.save_material import Save_material
from base.base_api.delete_material import Delete_material
from base.base_api.delete_knowledge import Delete_knowledge
class SaveKnowledge(unittest.TestCase):
    def setUp(self):
        s = Save_material().save_material()
        s = s.json()
        self.materialid = s["data"]["id"]
    def test_001(self):
        s = Save_knowledge().save_knowledge(self.materialid)
        s = s.json()
        self.knowledgeid = s["data"]["id"]
        mes = s['message']
        self.assertEqual(mes,"请求成功")
    def tearDown(self):
        kd = Delete_knowledge().delete_knowledge(self.knowledgeid)
        md = Delete_material().delete_material(self.materialid)