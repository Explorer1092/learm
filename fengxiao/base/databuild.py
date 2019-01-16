import pymysql
import settings
import constants
class Mysql_db:
    '''初始化连接数据库'''
    def __init__(self):
        self.client = pymysql.connect(**settings.mysql_config)
        self.cursor = self.client.cursor() #获取操作游标
        # print(type(self.cursor))

    def select_data(self,sql):
        self.cursor.execute(sql)  #返回数据条数
        # data = self.cursor.fetchone()  #返回第一条数据
        data = self.cursor.fetchall()  #返回所有数据
        print(data)
        self.client.close()
        return data
    def delete_data(self,sql):
        try:
            self.cursor.execute(sql)

            self.client.commit()  #提交修改
            msg = "删除成功！"
        except:
            self.client.rollback()  #发生错误时回滚
            msg = "删除失败执行回滚操作！"
        return print(msg)
        self.client.close()



if __name__ =="__main__":
    sql = constants.sql_list[0]
    # sql = "select * from accont"
    c = Mysql_db()
    s = c.select_data(sql)
    # d = c.delete_data(sql)

