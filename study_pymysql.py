import pymysql

#1,建立连接：数据库的连接信息：
host = "test.lemonban.com"
port = 3306
user = "test"
password = "test"
mysql = pymysql.connect(host=host, user=user, password=password, port=port)

#2.新建一个查询页面,游标
cursor = mysql.cursor()

#3.新建一个查询，新建sql查询语句
#sql = 'select max(mobilephone) from future.member' #找到最大的手机号
#sql = 'select * from future.loan limit 10'  #查询前10行
# sql = 'select * from future.member where mobilephone = "15717481995"'
new_phone = "15717481995"
sql = 'select mobilephone from future.member where mobilephone = new_phone'

#4.执行sql,
cursor.execute(sql)

#5.查看结果
result = cursor.fetchone()[0]  # 获取查询结果集里面最近的一条数据返回
# results = cursor.fetchall()  # 获取全部结果集
print(type(result),result)


#6.关闭查询
cursor.close()
#7.关闭数据库
mysql.close()