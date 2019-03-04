import sys,os
sys.path.append(os.path.dirname(os.path.abspath(".")))
import  unittest
import os
from  testsuites.test_1 import DiscuzSearch
from  testsuites.test_2 import DiscuzSearch1
from  testsuites.test_3 import DiscuzSearch2
from  testsuites.test_5 import DiscuzSearch3
import  HTMLTestRunner
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(DiscuzSearch1))
suite.addTest(unittest.makeSuite(DiscuzSearch2))
suite.addTest(unittest.makeSuite(DiscuzSearch3))
if __name__=='__main__':
    html_report=report_path+r"report.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,
                                         title="单元测试报告",description="用例执行情况")
    runner.run(suite)