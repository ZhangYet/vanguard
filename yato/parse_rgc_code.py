# 从 rgcbook 中抽取代码
# 为什么要从 html 中抽取而不是从 markdown 中抽取？
# 因为 markdown 没有结构啊！
import os
from bs4 import BeautifulSoup
from typing import List

base_dir = "/Users/zhangye/Repos/rgraphicscookbook/_book"
rmd_dir = "/Users/zhangye/Repos/rgc_code_examples"


class SectionCodes:
    def __init__(self, section_title: str):
        self.section = section_title
        self.code = []

    def add_code(self, code: str):
        self.code.append(code)


class ChapterCodes:
    def __init__(self, title: str, file_name: str, base_dir="codes/", rmd_dir=rmd_dir):
        self.chapter_title = title
        self.sections: List[SectionCodes] = []
        self.base_dir = base_dir
        self.file_name = file_name
        self.rmd_dir = rmd_dir

    def add_section(self, section: SectionCodes):
        self.sections.append(section)

    def add_sections(self, sections: List[SectionCodes]):
        self.sections = sections

    def output_rmd(self):
        if not os.path.exists(self.rmd_dir):
            os.mkdir(self.rmd_dir)

        file_name = f"{self.rmd_dir}/{self.file_name}.Rmd"
        with open(file_name, "w") as output:
            output.write(f"# {self.chapter_title}\n\n")
            for section in self.sections:
                output.write(f"## {section.section}\n")
                for code in section.code:
                    output.write("```{r}\n")
                    output.write(f'{code}\n\n')
                    output.write("```\n")
                output.write("\n")

    def output_code(self):
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        file_name = f"{self.base_dir}/{self.file_name}.r"
        with open(file_name, "w") as output:
            output.write(f"# {self.chapter_title}\n\n")
            for section in self.sections:
                output.write(f"# {section.section}\n")
                for code in section.code:
                    output.write('# code block\n')
                    output.write(f'{code}\n\n')
                output.write("\n")


class ChapterHtml:
    def __init__(self, text: str, file_name: str):
        self.bs = BeautifulSoup(text, "html.parser")
        self.file_name = file_name

    def parse_chapter(self) -> ChapterCodes:
        cc = ChapterCodes(self.get_chapter_name(), self.file_name)
        cc.add_sections(self.get_sections())
        return cc

    def get_chapter_name(self):
        h1 = self.bs.find("div", class_="section level1").find("h1")
        return h1.text

    def get_sections(self) -> List[SectionCodes]:
        level2 = self.bs.find_all("div", class_="section level2")
        res: List[SectionCodes] = []
        for item in level2:
            section_title = item.find("h2").text
            sc = SectionCodes(section_title)
            codes = item.find_all("code", class_="sourceCode r")
            for code in codes:
                sc.add_code(code.text)
            res.append(sc)
        return res


if __name__ == "__main__":
    for i in range(1, 16):
        chapter = f'chap{i}' if i != 1 else 'rbasics'
        test_html = f"{base_dir}/{chapter}.html"
        with open(test_html) as r:
            text = r.read()
            output_file = f'chap{i:02}'
            ch = ChapterHtml(text, output_file)
            cc = ch.parse_chapter()
            #cc.output_code()
            cc.output_rmd()
