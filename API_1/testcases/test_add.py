import unittest
from ddt import ddt,data
from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from API_1.common.config import config
from API_1.common import context


@ddt     #装饰测试类
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'add')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'login').get_case() #读取文件

    @classmethod   #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        cls.http_request = HttpRequests2()
    # def setUp(self):
    #     self.http_request = HttpRequests2()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_add(self,case):
        # case.data = eval(case.data) #转换成字典
        # print(type(case))
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['mobilephone'] = config.get('data','normal_user')  #那到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['pwd'] = config.get('data','normal_pwd')  #那到配置文件里面的值赋值给pwd
        #
        # if  case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':  #has_key判断键是否存在字典，存在返回Ture，否则返回false
        #     case.data['memberId'] = config.get('data','loan_member_id')  #那到配置文件里面的值赋值给mobilephone
        #在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e

    @classmethod   #变为类方法
    def tearDownClass(cls):
        cls.http_request.close()
    # def tearDown(self):
    #     self.http_request.close()