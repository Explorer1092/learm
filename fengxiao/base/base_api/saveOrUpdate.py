# coding:utf-8
from base.request_list import Request_list
class SaveOrUpdateApi(Request_list):
    def saveOrUpdateApi(self,materialid,knowledgeid):
        self.url = "/api/gw/api/v1/question/saveOrUpdate"
        self.data = {"materialId":materialid,"type":2,"id":None,"score":10,"level":0,"knowledgepointIds":[knowledgeid],"degree":"1","description":"{\"id\":0,\"type\":\"CHOICE_SINGLE\",\"analyTxt\":\"asd\",\"title\":{\"text\":\"sfa\",\"image\":\"\",\"audio\":\"\"},\"items\":[{\"cid\":0,\"head\":\"A\",\"field\":{\"text\":\"wer\",\"image\":\"\",\"audio\":\"\"}},{\"cid\":1,\"head\":\"B\",\"field\":{\"text\":\"dgs\",\"image\":\"\",\"audio\":\"\"}},{\"cid\":2,\"head\":\"C\",\"field\":{\"text\":\"gf\",\"image\":\"\",\"audio\":\"\"}}],\"time\":5,\"score\":10,\"answer\":0}","kqrId":None,"eqmId":None,"mqmId":0,"pid":0,"qType":10,"answerAnalysis":"asd","answerTime":1,"url":""}
        s = self.post(self.data)
        print(s.content)
        return s
if __name__ == "__main__":
    knowledgeid = 3039
    materialid = 541
    c = SaveOrUpdateApi()
    s = c.saveOrUpdateApi(materialid,knowledgeid)
