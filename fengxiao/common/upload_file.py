import request
import os
#上传文件的方法

s = request.session()
    #取img路径
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'img','1.png')
print(file_path)

        #上传照片
def uploadimage(self,url):

    #照片上传只传name参数
    f = {"localurl":("1.png"),
         "imgFile":("1.png",open(file_path ),'rb','image/png')

         }
    r = s.post(url,files = f)
    print(r.json()['url'])
    return r.json()['url']
if __name__ == "__main__":

    print(file_path)
