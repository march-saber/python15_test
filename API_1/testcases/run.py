import unittest
import HTMLTestRunnerNew
from API_1 import testcases
from API_1.common import contants
# from API_1.testcases import test_register
# from API_1.testcases import test_login


# suite = unittest.TestSuite()
# loaderoader = unittest.TestLoader()
# suite.addTests(loader.loadTestsFromModule(test_register))
# suite.addTests(loader.loadTestsFromModule(test_login))
discover = unittest.defaultTestLoader.discover(start_dir=contants.case_dir,pattern='test_*.py')     #discover查找目录下所有的文件

with open(contants.report_dir + '/report.html','wb+') as file:
    # runner = unittest.TextTestRunner(stream=file,verbosity=3)
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="python case",
                                              description="这是以一个简单的小游戏",
                                              tester="三月")
    runner.run(discover)






