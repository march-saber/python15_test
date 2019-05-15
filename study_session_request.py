import requests

session=requests.sessions.session()
"""session主要是request里面的一种方法，可以不用传cookie来使用"""

#登录
params = {"mobilephone":15717481995,"pwd":123456}
resp = session.request("post",url="http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)


#充值
params1 = {"mobilephone":15717481995,"amount":6666}
resp = session.request("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=params1)
print(resp.status_code)
print(resp.text)
print(resp.cookies)