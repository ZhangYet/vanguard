import requests
from settings import USER_NAME, COOKIE, HTML_STORAGE_DIR


URL = 'https://book.douban.com/people/{}/collect'.format(USER_NAME)


# 抓一页读过列表
def fetch_one_read_page(offset: int, save: bool = True) -> str:
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
            with open('{}/{:06d}.html'.format(HTML_STORAGE_DIR, offset), 'w') as output:
                output.write(resp.text)
        return resp.text
    except Exception as e:
        print(e)
