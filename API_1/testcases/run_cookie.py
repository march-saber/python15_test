import unittest
from request_cookies import HttpRequests

class TestCookies(unittest.TestCase):

    def test_001(self):
        method = "post"
        url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
        param = {"mobilephone": 15717481995, "pwd": 123456, "reqname": "三月"}
        resp=HttpRequests().http_requests(method=method, url=url, param=param)
        self.assertEqual("20110",resp.json()["code"])
    def test_002(self):
        method = "get"
        url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
        param = {"mobilephone": 15717481995, "pwd": 123456}
        resp = HttpRequests().http_requests(method=method, url=url, param=param)
        self.assertEqual("10001", resp.json()["code"])
    def test_003(self):
        method = "get"
        url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
        param = {"mobilephone": 15717481995, "pwd": 123456}
        resp = HttpRequests().http_requests(method=method, url=url, param=param)

        method = "get"
        url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
        param = {"mobilephone": 15717481995, "amount": 1000}
        resp1 = HttpRequests().http_requests(method=method, url=url, param=param,cookie=resp.cookies)
        self.assertEqual("10001", resp1.json()["code"])
