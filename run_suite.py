import time
import unittest
from script.login_get_token import TestGetTkoen
from script.test_emp import TestEmp
from script.test_login import TestLogin
from tools.HTMLTestRunnerCN import HTMLTestReportCN
from app import BASE_DIR

suite = unittest.TestSuite()

# 添加测试套件
suite.addTest(unittest.makeSuite(TestLogin)) # 登录测试
suite.addTest(unittest.makeSuite(TestGetTkoen)) # 令牌
suite.addTest(unittest.makeSuite(TestEmp)) # 员工测试

# file_dir = BASE_DIR + '/report/{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))
file_dir = BASE_DIR + '/report/ihrm.html'
with open(file_dir,'wb') as f:
    runner = HTMLTestReportCN(f,1,'ITMH测试报告','Win8','QAhyc')
    runner.run(suite)