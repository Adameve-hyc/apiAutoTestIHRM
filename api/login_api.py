'''
登录
'''
import requests
from api import *

from app import HEADERS


class LoginApi(object):
    def __init__(self):
        self.headers = HEADERS

    def post_login(self, mobile, password):
        '''
        登录输入的数据
        :param mobile: 登录手机号
        :param password: 登录密码
        :return: 登录接口
        '''
        data = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(login_url, json=data, headers=self.headers)
