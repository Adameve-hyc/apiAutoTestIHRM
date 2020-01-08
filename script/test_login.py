'''
登录测试接口
'''
import logging
import unittest
from api.login_api import LoginApi
from read_data.read_login import read_login_func
from utils import assert_common
from parameterized import parameterized


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = LoginApi()
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @parameterized.expand(read_login_func())
    def test_login(self, mobile, password, status_code, success, code, message, desc):
        '''测试登录成功接口'''
        response = self.login.post_login(mobile, password)
        json_data = response.json()
        assert_common(self, response, status_code, success, code, message)
        # logging.info(desc)
