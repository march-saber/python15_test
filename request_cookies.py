# 1,扩展之前实现好的http_request，支持传cookies
# 2，完成接口文档中注册，登录，充值的调用

import requests

class HttpRequests:
    def http_requests(self,method,url,param,cookie=None):
        """
        method:请求方法
        url：请求地址
        param：请求参数，为字典格式
        """
        if method.lower()=="get":   #判断注册接口的请求方式
            try:
                resp = requests.get(url,params=param,cookies= cookie)
                #print("响应头：",resp.headers)
                print("响应报文：", resp.text)
                print("响应状态码：", resp.status_code)
                print("响应cookie：", resp.cookies)
                print("请求cookie：", resp.request._cookies)
            except Exception as e:
                print("get请求出错:{}".format(e))
        else:    #默认除了get就为post
            try:
                resp = requests.post(url,data=param,cookies= cookie )
                #print("响应头：", resp.headers)
                print("响应报文：", resp.text)
                print("响应状态码：", resp.status_code)
                print("响应cookie：",resp.cookies)
                print("请求cookie：", resp.request._cookies)
            except Exception as e:
                print("post请求出错:{}".format(e))
        return resp #返回我们response，下次调用

if __name__ == '__main__':
    method = "post"
    url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    param = {"mobilephone":15717481995,"pwd":123456,"reqname":"三月"}
    HttpRequests().http_requests(method=method,url=url,param=param)

    # method = "get"
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    # param = {"mobilephone": 15717481995, "pwd": 123456}
    # resp = HttpRequests().http_requests(method=method, url=url, param=param)
    #
    # method = "get"
    # url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    # param = {"mobilephone": 15717481995, "amount": 1000}
    # resp1 = HttpRequests().http_requests(method=method, url=url, param=param, cookie=resp.cookies)

