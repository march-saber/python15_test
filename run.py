import unittest
suite = unittest.TestSuite()

from API_1.testcases.run_cookie import TestCookies
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCookies)) #通过测试类名来加载

#执行
runner = unittest.TextTestRunner()
runner.run(suite)