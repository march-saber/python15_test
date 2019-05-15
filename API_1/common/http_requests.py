"""
1，完成do_excel类的封装支持读和写，理解Case类的设计
2，结合http_requests完成注册，登录，充值接口的请求
3，尝试引入unittest+ddt 来完成以上接口的测试用例"""

import requests
from API_1.common.config import config
from API_1.common import logger

logger = logger.get_logger(__name__)

class HttpRequests1:
    def request(self,method,url,data=None,json=None,cookie=None):
        """
        method:请求方法
        url：请求地址
        data/json:请求参数
        """
        if type(data) == str:
            data = eval(data)
            print("请求data：", data)

        #拼接请求的url

        url = config.get("api","pre_url") + url   #读取配置文件的前半段
        logger.debug("请求url：{0}".format(url))
        logger.debug("请求data：{0}".format(data))


        if method.lower() == 'get': #判断大小写，发送get请求
            try:
                resp = requests.get(url,params=data,cookies=cookie)
            except Exception as e:
                print("get请求出错：{}".format(e))
        elif method.lower()=="post":
            try:
                if json:
                    resp = requests.post(url, json=json, cookies=cookie)
                else:
                    resp = requests.post(url,data=data,cookies=cookie)
            except Exception as e:
                print("post请求出错：{}".format(e))
        else:
            resp = None
            print('UN-support method')

        print("请求response：", resp.text)
        return resp



class HttpRequests2:
    def __init__(self):
        """打开一个session"""
        self.session = requests.sessions.session()

    def request(self,method,url,data=None,json=None):

        """
        method:请求方法
        url：请求地址
        data/json:请求参数
                """
        if type(data) == str:
            data = eval(data)
            print("请求data：", data)

        # 拼接请求的url
        url = config.get("api", "pre_url") + url  #读取配置文件的前半段
        logger.debug("请求url：{0}".format(url))
        logger.debug("请求data：{0}".format(data))

        if method.lower() == "get":
            try:
                resp = self.session.request("get",url=url,params=data)
            except Exception as e :
                print("get方法有误：{}".format(e))
        elif method.lower() == "post":
            try:
                if json:
                    resp = self.session.request("post",url=url,json=json)
                else:
                    resp = self.session.request("post",url=url,data=data)
            except Exception as e :
                print("post方法有误：{}".format(e))
        else:
            resp = None
            logger.error('UN-support method')
        logger.debug("请求response：", resp.text)

        return resp
    def close(self):
        self.session.close()  # 用完记得关闭，很关键！！！


