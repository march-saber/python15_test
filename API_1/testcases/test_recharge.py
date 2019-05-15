# -*- coding：utf-8 -*-
import unittest
from ddt import ddt,data
from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from API_1.common.do_mysql import DoMysql

@ddt     #装饰测试类
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'recharge')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'recharge').get_case() #读取文件

    @classmethod  #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        cls.http_request = HttpRequests2()
        cls.mysql = DoMysql()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_recharge(self,case):
        print(case.title)

        #请求之前，判断是否需要执行sql
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print(member['LeaveAmount'])
            before = member['LeaveAmount']

        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        print(actual_code)
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
            # 成功之后，判断是否需要执行SQL
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['LeaveAmount'])
                after = member['LeaveAmount']
                recharge_amount = int(eval(case.data)['amount'])  # 充值金额
                self.assertEqual(before + recharge_amount, after)

        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e

    @classmethod     #变为类方法
    def tearDownClass(cls):
        cls.http_request.close()

