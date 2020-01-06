'''
URL
'''

# 日志
from app import app_logging, HOST

app_logging()
# logging.info('调试日志')

# URL
# 登录
login_url = HOST + '/api/sys/login' # 登录

# 员工
emp_url = HOST + '/api/sys/user' # 员工
emp_id = HOST + '/api/sys/user'  # 员工URL后跟id，id在emp_api界面