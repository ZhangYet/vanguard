from spider import fetch_one_read_page
from parser import ReadPageParser
from settings import OUT_DIR, TOTAL_PAGES


def main():
    for i in range(TOTAL_PAGES):
        offset = i * 15
        print(offset)
        text = fetch_one_read_page(offset, TOTAL_PAGES - i)
        r = ReadPageParser(text)
        for record in r.gen_records():
            title = record.title.replace('/', '_')
            file_name = f'{OUT_DIR}/{title}.org'
            record.save_org(file_name)


if __name__ == '__main__':
    main()
