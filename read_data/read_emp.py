import json

from app import BASE_DIR


def read_add_emp():
    '''读取添加员工数据'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_add = list()
        data = json.load(f).get('add_emp')
        read_add.append((data.get('username'),
                         data.get('mobile'),
                         data.get('status_code'),
                         data.get('success'),
                         data.get('code'),
                         data.get('message'),
                         data.get('desc')
                         ))
        return read_add


def read_search_emp():
    '''读取查询员工数据'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_search = list()
        data = json.load(f).get('search_emp')
        read_search.append((data.get('status_code'),
                            data.get('success'),
                            data.get('code'),
                            data.get('message'),
                            data.get('desc')
                            ))
        return read_search


def read_update_emp():
    '''读取修改员工数据'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_update = list()
        data = json.load(f).get('update_emp')
        read_update.append((data.get('username'),
                            data.get('status_code'),
                            data.get('success'),
                            data.get('code'),
                            data.get('message'),
                            data.get('desc')
                            ))
        return read_update


def read_delete_emp():
    '''读取删除员工数据'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_delete = list()
        data = json.load(f).get('delete_emp')
        read_delete.append((data.get('status_code'),
                            data.get('success'),
                            data.get('code'),
                            data.get('message'),
                            data.get('desc')
                            ))
        return read_delete


def read_emp_list():
    '''读取查询员工列表size返回条数数据'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_emp_list = list()
        data = json.load(f).get('emp_list')
        for i in data:
            read_emp_list.append((i.get('type'),
                                  i.get('size'),
                                  i.get('status_code'),
                                  i.get('success'),
                                  i.get('code'),
                                  i.get('message'),
                                  i.get('desc')
                                  ))
        return read_emp_list


def read_mobile_find_username():
    '''根据手机号查用户名'''
    file_dir = BASE_DIR + '/data/emp_data.json'
    with open(file_dir, encoding='utf-8') as f:
        read_date = list()
        data = json.load(f).get('mobile_find_username')
        read_date.append((data.get('type'),
                          data.get('size'),
                          data.get('status_code'),
                          data.get('success'),
                          data.get('code'),
                          data.get('message'),
                          data.get('mobile'),
                          data.get('expect'),
                          data.get('desc')
                          ))
        return read_date
