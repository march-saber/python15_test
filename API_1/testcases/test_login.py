import unittest
from ddt import ddt,data

from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from API_1.common import logger

logger = logger.get_logger(__name__)

@ddt     #装饰测试类
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'login')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'login').get_case() #读取文件

    @classmethod   #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRequests2()
    # def setUp(self):
    #     self.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_login(self,case):
        logger.info("开始测试：{}".format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            logger.error("报错了：{0}".format(e))
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod   #变为类方法
    def tearDownClass(cls):
        logger.info("测试后置处理")
        cls.http_request.close()
    # def tearDown(self):
    #     self.http_request.close()

