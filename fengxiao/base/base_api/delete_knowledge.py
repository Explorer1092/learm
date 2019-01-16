from base.request_list import Request_list
class Delete_knowledge(Request_list):
    def delete_knowledge(self,knowledgelid):
        self.url = "/api/gw/api/v1/knowledge/delete"
        self.data = {"id":knowledgelid}
        s = self.post(self.data)
        return s
if __name__ == "__main__":
    id = 3037
    s = Delete_knowledge()
    d = s.delete_knowledge(id)