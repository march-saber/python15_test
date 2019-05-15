
import pymysql
from API_1.common.config import config


class DoMysql:
    """
    数据库的调用，完成MySQL数据库的交互
    """
    def __init__(self):
        # host = "test.lemonban.com"
        # port = 3306
        # user = "test"
        # password = "test"
        host = config.get('mysql', 'host')
        port = config.get('mysql','port')
        user = config.get('mysql','user')
        password = config.get('mysql','password')
        self.mysql = pymysql.connect(host=host,port=int(port),user=user,password= password) #数据库连接
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 新建游标查询,括号内表示创建一个字典类型游标，返回的数据为字典

    def fetch_one(self,sql):  #单个查询,编写sql语句并执行，查看结果
        self.cursor.execute(sql)   #执行sql语句
        self.mysql.commit() #强制执行最新的
        return self.cursor.fetchone()  #返回获取查询结果集里面最近的一条数据，fetchone返回值为元祖

    def fetch_all(self,sql):  #多个查询，编写sql语句并执行，查看结果
        self.cursor.execute(sql)  #执行sql语句
        return self.cursor.fetchall()  #获取全部结果集

    def close(self):
        self.cursor.close()  #关闭查询界面游标
        self.mysql.close()   #关闭连接

if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one("select max(mobilephone) from future.member") #返回元祖
    print(result)
    mysql.close()

