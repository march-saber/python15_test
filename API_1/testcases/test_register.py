import unittest
from API_1.common.http_requests import HttpRequests2
from API_1.common import do_excel
from API_1.common import contants
from API_1.common import do_mysql
from ddt import ddt,data

@ddt     #装饰测试类
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.api_case_file, 'register')
    cases = excel.get_case()
    # cases = do_excel.DoExcel(contants.api_case_file,'login').get_case() #读取文件

    @classmethod   #变为类方法,如果不变为类方法，每运行一个用来就会执行一次该操作
    def setUpClass(cls):
        cls.http_request = HttpRequests2()
    # def setUp(self):
    #     self.http_request = HttpRequests2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)  #装饰测试方法，接收可迭代数据,cases为实例
    def test_register(self,case):
        if case.data.find("register_mobile") > -1:

            sql = 'select max(mobilephone) from future.member'
            #sql = 'select * from future.member where mobilephone = "15717481999"'
            #max_phone = self.mysql.fetch_one(sql)[0]  #查询最大手机号码  ，fetchone返回值为元祖
            phone =self.mysql.fetch_one(sql)[0]
            new_phone = int(phone) + 1

            # if self.mysql.fetch_one(sql) != None:
            #     phone = self.mysql.fetch_one(sql)[3]
            #
            #     new_phone = int(phone) + 1
            #
            #     user = self.mysql.fetch_one('select * from future.member where mobilephone = "new_phone"')
            #     print("请求user:",user)
            #
            #     while new_phone == int(user[3]):
            #         new_phone = new_phone + 1
            #         user = self.mysql.fetch_one('select * from future.member where mobilephone = "new_phone"')
            #         #最大手机号码+1
            #         #max_phone = int(max_phone) + 1
            #         #new_phone = int(new_phone) + 1
            #         #print("最大手机号码：",max_phone)


            print("新手机号码：", new_phone)
            case.data = case.data.replace('register_mobile',str(new_phone))  #替换参数值,replace替换新的字符串，重新返回一个新的字符串

        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAIL')
            raise e

    @classmethod   #变为类方法
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
    # def tearDown(self):
    #     self.http_request.close()