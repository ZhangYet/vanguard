from spider import fetch_one_read_page
from parser import ReadPageParser
from PyOrgMode import PyOrgMode


def main():
    base = PyOrgMode.OrgDataStructure()
    base.level = 1
    base.content = 'reading'
    with open('output', 'w') as output:
        for i in range(84):
            offset = i * 15
            print(offset)
            text = fetch_one_read_page(offset)
            r = ReadPageParser(text)
            for record in r.gen_records():
                node = record.gen_node()
                base.root.append(node)
                output.write('{}\n'.format(record))
    base.save_to_file('test.org')


if __name__ == '__main__':
    main()
