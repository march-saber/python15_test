import pymysql
from API_1.common.config import config


# from API_1.common import do_mysql
# # mysql = do_mysql.DoMysql()
# # while 1:
# #     new_phone = 15717481995
# #     sql = 'select * from future.member where mobilephone = new_phone'
# #     phone = mysql.fetch_one(sql)[3]



host = config.get('mysql', 'host')
print(host)
port = config.get('mysql','port')
print(port)
user = config.get('mysql','user')
print(user)
password = config.get('mysql','password')
print(password)
mysql = pymysql.connect(host=host,port=int(port),user=user,password= password) #数据库连接
