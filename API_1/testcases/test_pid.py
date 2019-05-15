"""
1，实现配置文件类，将接口路径前半段设计到配置文件中，通过配置文件类读取出来
2，在原来http_requests类的request方法中，完成路径的拼接
3，尝试完成投资，添加标的，审核接口的用例"""
import unittest
from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from ddt import ddt,data

@ddt     #装饰测试类
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'pid')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'recharge').get_case() #读取文件

    @classmethod   #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        cls.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_recharge(self,case):
        print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        print(actual_code)
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e

    @classmethod     #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def tearDownClass(cls):
        cls.http_request.close()