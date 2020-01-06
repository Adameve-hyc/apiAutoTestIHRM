'''
登录测试接口
'''
import logging
import unittest
from api.login_api import LoginApi, HEADERS
from utils import assert_common


class TestGetTkoen(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_add_token(self):
        '''测试登录成功接口'''
        response = self.login.post_login(13800000002, 123456)
        json_data = response.json()
        # 添加token到HEADER_DIR
        token = 'Bearer ' + json_data.get('data')
        HEADERS['Authorization'] = token
        logging.info('获取令牌:{}'.format(token))
        assert_common(self, response, 200, True, 10000, '操作成功') # 断言

