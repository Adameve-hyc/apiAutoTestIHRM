'''
测试员工界面
'''
import logging
import unittest

import pymysql

import app

from api.emp_api import EmpApi
from read_data.read_emp import *
from script.login_get_token import TestGetTkoen
from utils import assert_common, DbUtils
from parameterized import parameterized


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp = EmpApi()
        cls.test_get_token = TestGetTkoen()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @parameterized.expand(read_add_emp())
    def test_01add_emp(self, username, mobile, status_code, success, code, message, desc):
        '''测试添加员工'''
        response = self.emp.post_add_emp(username, mobile)
        app.EMP_ID = response.json().get('data').get('id')
        # logging.info('获取的员工id{}'.format(app.EMP_ID))
        # logging.info('添加员工')
        assert_common(self, response, status_code, success, code, message)

    @parameterized.expand(read_search_emp())
    def test_02search_emp(self, status_code, success, code, message, desc):
        '''测试查询员工'''
        response = self.emp.get_search_api()
        # logging.info('查询员工')
        assert_common(self, response, status_code, success, code, message)
        self.assertEqual(str(app.EMP_ID), response.json().get('data').get('id'))

    @parameterized.expand(read_update_emp())
    def test_03update_emp(self, username, status_code, success, code, message, desc):
        '''测试修改员工'''
        response = self.emp.put_update_emp(username)
        # logging.info('修改员工')
        assert_common(self, response, status_code, success, code, message)
        with DbUtils() as db_utils:
            sql = 'select username from bs_user where id ={}'.format(app.EMP_ID)
            db_utils.execute(sql)
            mes = db_utils.fetchone()[0]
            self.assertEqual(username, mes)
        # conn = pymysql.connect('182.92.81.159','readuser','iHRM_user_2019','ihrm')
        # cur = conn.cursor()
        # sql = 'select username from bs_user where id ={}'.format(app.EMP_ID)
        # cur.execute(sql)
        # result = cur.fetchone()[0]
        # self.assertEqual(username, result)
        # cur.close()
        # conn.close()

    @parameterized.expand(read_delete_emp())
    def test_04delete_emp(self, status_code, success, code, message, desc):
        '''测试删除员工'''
        response = self.emp.delete_emp()
        # logging.info('删除员工')
        assert_common(self, response, status_code, success, code, message)
        self.assertEqual(None, response.json().get('data'))

    @parameterized.expand(read_emp_list())
    def test_05emp_list(self, type, size, status_code, success, code, message, desc):
        '''测试员工管理列表size返回条数'''
        response = self.emp.find_emp_list(type, size)
        try:
            assert_common(self, response, status_code, success, code, message)
        except AssertionError as e:
            logging.info('员工列表错误')
            raise e
        finally:
            if success:
                num = len(response.json().get('data').get('rows'))
                self.assertEqual(size, num)

    @parameterized.expand(read_mobile_find_username())
    def test_06emp_list(self, type, size, status_code, success, code, message, mobile, expect, desc):
        '''测试员工管理列表根据手机号查询用户名'''
        response = self.emp.find_emp_list(type, size)
        try:
            assert_common(self, response, status_code, success, code, message)
        except AssertionError as e:
            logging.info('员工列表错误')
            raise e
        finally:
            num = response.json().get('data').get('rows')
            for i in num:
                if i.get('mobile') == mobile:
                    self.assertEqual(expect, i.get('username'))
                    logging.info('查询到的用户名称是：{}'.format(i.get('username')))
                    break


if __name__ == '__main__':
    unittest.main()
