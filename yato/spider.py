import requests
from settings import USER_NAME, COOKIE, HTML_STORAGE_DIR


URL = 'https://book.douban.com/people/{}/collect'.format(USER_NAME)


def fetch_one_read_page(offset: int, file_index: int, save: bool = True) -> str:
    file_name = '{}/{:04d}.html'.format(HTML_STORAGE_DIR, file_index)
    try:
        with open(file_name) as data:
            return data.read()
    except OSError:
        print('cannot read cache {}, read from www.douban.com'.format(file_name))

    params = {
        'start': offset,
        'sort': 'time',
    }
    headers = {
        'Cookie': COOKIE,
    }
    try:
        resp = requests.get(URL, headers=headers, params=params)
        if save:
            with open(file_name, 'w') as output:
                output.write(resp.text)
        return resp.text
    except Exception as e:
        print(e)
