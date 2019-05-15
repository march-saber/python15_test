import requests



class HttpRequests:
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
            print("抱歉,暂不支持get和post以外的请求方法")

        return resp
    def close(self):
        self.session.close()  # 用完记得关闭，很关键！！！

