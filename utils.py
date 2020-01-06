'''
公共方法类
'''
import pymysql


def assert_common(self, response, status_code, success, code, message):
    '''
    普通断言
    :param self: 测试类本身
    :param response: 响应
    :param status_code: 响应状态码
    :param success: 响应JSON文件中的success
    :param code: 响应JSON文件中的code
    :param message: 响应JSON文件中的message
    :return:
    '''
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))


class DbUtils():
    def __init__(self, host='182.92.81.159', user='readuser', password='iHRM_user_2019', datebase='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.datebase = datebase

    # 使用with语法with 类名 as 变量，变量接收__enter__的返回值
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.datebase)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
