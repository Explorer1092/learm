# coding:utf-8
from base.request_list import Request_list
class Save_knowledge(Request_list):
    def save_knowledge(self,materialid):
        self.url = "/api/gw/api/v1/knowledge/save"
        self.data = {"id":None,"materialId":materialid,"name":"知识点名称","difficulty":1,"knowledgeImage":"","caption":"知识点文字","imageUrl":"1.jpg","videoUrl":"","kAudioUrl":"","audioUrl":"1.mp3","description":"{\"id\":0,\"sequence\":1,\"name\":\"知识点名称\",\"difficulty\":1,\"caption\":\"知识点文字\",\"knowledgeImage\":\"\",\"kAudioUrl\":\"\",\"videoUrl\":\"\",\"imageUrl\":\"1.jpg\",\"audioUrl\":\"1.mp3\",\"shapeVideoUrl\":\"1.mp4\",\"refType\":1,\"description\":\"\",\"translate\":\"单词短语翻译\",\"phoneme\":\"\",\"wordType\":\"1\",\"knowledgepointTypeKey\":\"2\",\"knowledgepointTypeString\":\"\",\"reviewType\":0,\"refWrod\":\"\"}","translate":"单词短语翻译","phoneme":"","wordType":"1","type":"2","shapeVideoUrl":"1.mp4","sequence":1,"reviewType":0,"relationId":None}
        s = self.post(self.data)
        return s
if __name__ == "__main__":
    id = 623
    s = Save_knowledge()
    c = s.save_knowledge(id)