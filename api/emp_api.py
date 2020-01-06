'''
员工列表
'''
import logging
import app
import requests
from api import *
from app import HEADERS


class EmpApi(object):
    def __init__(self):
        self.headers = HEADERS

    def post_add_emp(self, username, mobile):
        '''
        添加员工接口请求
        :param username: 用户名
        :param mobile: 手机号
        :return:
        '''
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-06",
            "formOfEmployment": 1,
            "workNumber": "11",
            "departmentName": "行政中心",
            "departmentId": "1066239766607040512",
            "correctionTime": "2020-01-20T16:00:00.000Z"
        }

        return requests.post(emp_url, json=data, headers=self.headers)

    def get_search_api(self):
        '''查询员工接口'''
        emp_id_url = emp_id + '/' + str(app.EMP_ID)
        return requests.get(emp_id_url, headers=self.headers)

    def put_update_emp(self,username):
        '''修改员工接口'''
        emp_id_url = emp_id + '/' + str(app.EMP_ID)
        data = {'username': username}
        return requests.put(emp_id_url, json=data, headers=self.headers)

    def delete_emp(self):
        '''删除员工'''
        emp_id_url = emp_id + '/' + str(app.EMP_ID)
        return requests.delete(emp_id_url,headers=self.headers)
