
import unittest
from ddt import ddt,data
from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from API_1.common.config import config
from API_1.common import context
from API_1.common import do_mysql
from API_1.common.context import Context


@ddt     #装饰测试类
class InvestTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'invest')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'login').get_case() #读取文件

    @classmethod   #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        cls.http_request = HttpRequests2()
        cls.mysql = do_mysql.DoMysql()
    # def setUp(self):
    #     self.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_invest(self,case):
        print("开始执行测试：",case.title)
        #在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'PASS')

            #p判断加标成功后，查询数据库，取到loan_id
            if resp.json()['msg'] == '加标成功':
                sql = "select id from future.loan WHERE MemberID = 839 order by id desc limit 1"
                loan_id = self.mysql.fetch_one(sql)[0]
                print('标的ID：',loan_id)
                setattr(Context,"loan_id",str(loan_id))   #添加类属性

        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e

    @classmethod   #变为类方法
    def tearDownClass(cls):
        cls.http_request.close()
    # def tearDown(self):
    #     self.http_request.close()