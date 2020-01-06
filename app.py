'''
'''
# 配置文件位置



'''
配置文件
'''
# 配置文件位置
import os
import logging
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = 'http://182.92.81.159'
HEADERS = {"Content-Type":"application/json"}
EMP_ID = 0

def app_logging():
    '''生成日志'''
    # 生成日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置控制台处理器
    sh = logging.StreamHandler()

    # 设置文件处理器
    file_dir = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(file_dir, when='S', interval=1, backupCount=4)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(fh)
    logger.addHandler(sh)
