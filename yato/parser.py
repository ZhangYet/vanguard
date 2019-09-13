import os
from typing import List, Tuple
from bs4 import BeautifulSoup, Tag
from PyOrgMode import PyOrgMode


class Record:

    def __init__(self, title: str, date: str, url: str, comment: str):
        self.title = title
        self.date = date
        self.url = url
        self.comment = comment

    def __repr__(self):
        return f'《{self.title}》 read on {self.date}, comment: {self.comment}'

    def wrap_heading(self) -> str:
        return f'[[{self.url}][{self.title}]]'

    def save_org(self, file_name: str, force: bool = True):
        if os.path.exists(file_name) and not force:
            return
        base = PyOrgMode.OrgDataStructure()
        base.level = 1
        node = PyOrgMode.OrgNode.Element()
        node.heading = self.wrap_heading()
        node.level = 2
        node.tags = ['douban', 'read']
        node.content = self.comment.strip() + '\n'
        base.root.append_clean(node)
        base.save_to_file(file_name)


class ReadPageParser:

    def __init__(self, text: str):
        self.bs = BeautifulSoup(text, 'html.parser')
        self.sub_items = self.bs.find_all('li', class_='subject-item')

    def gen_records(self) -> List[Record]:
        return [gen_record(x) for x in self.sub_items]


def gen_record(item: Tag) -> Record:
    title, url = get_name_and_url(item)
    date = get_date(item)
    comment = get_comment(item)
    return Record(title, date, url, comment)


def get_name_and_url(item: Tag) -> Tuple[str, str]:
    h = item.find('h2')
    a = h.find('a')
    return a.get('title'), a.get('href')


def get_date(item: Tag) -> str:
    info = item.find('span', class_='date')
    d: str = info.text
    return d.split('\n')[0].strip() if d else 'unknown'


def get_comment(item: Tag) -> str:
    info = item.find('p', class_='comment')
    return info.text.strip()
