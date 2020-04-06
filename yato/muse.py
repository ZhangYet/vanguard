from typing import List
from bs4 import BeautifulSoup
import re
import wget
import requests
import os
import aria2p
import sys
import time

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

base_url = "https://muse.jhu.edu"
chapter_pattern = re.compile(r"/chapter/\d+/pdf")
base_dir = "/Users/zhangye/aria2"

aria_client = aria2p.API(aria2p.Client(host="http://localhost", port=6800, secret=""))


def parse_book_name(text: str) -> str:
    bs = BeautifulSoup(text, "html.parser")
    title: str = bs.find("li", class_="title").text
    clean_title = re.sub("\W+", "_", title)
    return clean_title.replace(" ", "_")


def parse_chapter_uri(text: str) -> List[str]:
    return chapter_pattern.findall(text)


def download(chapter_url: str, out_dir: str):
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    wget.download(chapter_url, out=out_dir)


def download_a_book(url: str):
    html = requests.get(url, headers=headers)
    text = html.text
    book_title = parse_book_name(text)
    chapter_urls = parse_chapter_uri(text)

    download_urls = [f"{base_url}/{uri}" for uri in chapter_urls]
    output_dir = f"{base_dir}/{book_title}"
    os.mkdir(output_dir)
    for url in download_urls:
        file_name = url.split("/")[-2]
        aria_client.add_uris(
            [url], {"dir": output_dir, "out": file_name + ".pdf", "header": headers}
        )
        print(f"add task: {file_name}")


if __name__ == '__main__':
    download_file = sys.argv[1]
    print(download_file)
    with open(download_file) as i:
        for line in i:
            download_a_book(line.strip())
            time.sleep(60) # 最多每分钟下载一本书