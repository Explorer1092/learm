import unittest
from base.base_api.save_material import Save_material
from base.base_api.delete_material import Delete_material
class SaveMaterial(unittest.TestCase):
    def setUp(self):
        pass
    def test_002(self):
        s = Save_material().save_material()
        s = s.json()
        mes = s['message']
        self.materialid = s["data"]["id"]
        print(self.materialid)
        self.assertEqual(mes,"请求成功")
    def tearDown(self):
        s = Delete_material().delete_material(self.materialid)
