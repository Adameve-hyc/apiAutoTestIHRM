import json

from app import BASE_DIR
def read_login_func():
    file_dir = BASE_DIR + '/data/login_data.json'
    with open(file_dir, encoding='utf-8') as f:
        login_data = json.load(f)
        json_login_data = list()
        for i in login_data:
            json_login_data.append((i.get('mobile'),
                                    i.get('password'),
                                    i.get('status_code'),
                                    i.get('success'),
                                    i.get('code'),
                                    i.get('message'),
                                    i.get('desc')
                                    ))
        return json_login_data
