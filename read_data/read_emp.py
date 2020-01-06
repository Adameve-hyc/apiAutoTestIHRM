import json

from app import BASE_DIR


def read_add_emp():
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
