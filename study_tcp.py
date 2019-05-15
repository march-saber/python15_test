import socket

#创建一个tcp的套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET 指定不同电脑可以通信
# socket.SOCK_STREAM    指定创建tcp套接字

#访问服务器(百度：http形式传输)
# 2.建立连接
s.connect(('www.baidu.com',80))

#3.传输数据（要以bytes形式传输）
#3.1发送数据
s.send(b'hello')

#3.2 接收数据
content = s.recv(2014)

print(content)

s.close()